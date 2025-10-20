# 实验6：连接硅基流动api，实现一个集成多功能的AI个人助理
# 功能包括：智能聊天、图片生成、情感分析

import requests  # 用于发送HTTP请求
import json      # 用于处理JSON数据
import base64    # 用于base64编码（虽然当前代码中未使用）

# 配置API相关参数
API_KEY = ""  # 硅基流动API密钥
API_URL = "https://api.siliconflow.cn/v1/chat/completions"  # 聊天对话API地址
IMAGE_GENERATION_URL = "https://api.siliconflow.cn/v1/images/generations"  # 图片生成API地址

def call_ai_api(messages, model="Qwen/Qwen2.5-7B-Instruct"):
    """
    调用AI聊天API进行对话
    
    参数:
        messages: 对话消息列表，格式为[{"role": "user", "content": "..."}]
        model: 使用的AI模型，默认为Qwen2.5-7B-Instruct
    
    返回:
        API响应的JSON数据
    """
    # 设置请求头，包含API密钥和内容类型
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 构建请求数据
    data = {
        "model": model,        # 指定使用的AI模型
        "messages": messages,  # 对话历史
        "stream": False       # 不使用流式输出
    }
    
    # 发送POST请求到API
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()  # 返回JSON格式的响应

def generate_image_function():
    """
    图片生成功能
    使用AI模型根据用户描述生成图片
    """
    # 获取用户输入的图片描述
    prompt = input("请输入图片描述（例如：一只在星空下跳舞的猫）: ")
    
    # 让用户选择图片尺寸
    print("\n请选择图片尺寸:")
    print("1. 1024x1024 (默认)")
    print("2. 512x512")
    print("3. 256x256")
    size_choice = input("请选择 (1-3): ").strip()
    
    # 尺寸选项映射
    size_options = {
        "1": "1024x1024",
        "2": "512x512", 
        "3": "256x256"
    }
    size = size_options.get(size_choice, "1024x1024")  # 默认使用1024x1024
    
    # 设置请求头
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 尝试不同的图片生成模型（按优先级排序）
    models_to_try = [
        "stabilityai/stable-diffusion-xl-base-1.0",  # Stable Diffusion XL
        "runwayml/stable-diffusion-v1-5",            # Stable Diffusion v1.5
        "black-forest-labs/FLUX.1-schnell",          # FLUX快速模型
        "black-forest-labs/FLUX.1-dev"               # FLUX开发模型
    ]
    
    # 依次尝试每个模型
    for model in models_to_try:
        print(f"\n尝试使用模型: {model}")
        
        # 构建图片生成请求数据
        data = {
            "model": model,           # 指定图片生成模型
            "prompt": prompt,         # 图片描述
            "size": size,            # 图片尺寸
            "n": 1,                  # 生成图片数量
            "response_format": "url"  # 返回格式为URL
        }
        
        print("正在生成图片，请稍候...")
        try:
            # 发送图片生成请求，设置60秒超时
            response = requests.post(IMAGE_GENERATION_URL, headers=headers, json=data, timeout=60)
            
            # 检查响应状态
            if response.status_code == 200:
                result = response.json()
                # 检查返回数据是否有效
                if "data" in result and len(result["data"]) > 0:
                    image_url = result["data"][0]["url"]
                    print(f"\n🎨 图片生成成功！")
                    print(f"🔗 图片URL: {image_url}")
                    
                    # 询问是否要下载图片
                    download = input("是否下载图片？(y/n, 默认n): ").strip().lower()
                    if download == 'y' or download == 'yes':
                        download_image(image_url, prompt)
                    return  # 成功生成，退出函数
            else:
                print(f"模型 {model} 失败: {response.status_code}")
                # 如果不是400错误，直接退出（可能是认证问题）
                if response.status_code != 400:
                    break
                    
        except requests.exceptions.Timeout:
            print(f"模型 {model} 请求超时")
            continue  # 尝试下一个模型
        except Exception as e:
            print(f"模型 {model} 出错: {e}")
            continue  # 尝试下一个模型
    
    print("\n❌ 所有模型尝试失败，请检查API密钥或网络连接")

def download_image(image_url, prompt):
    """
    下载生成的图片到本地
    
    参数:
        image_url: 图片的URL地址
        prompt: 图片描述，用于生成文件名
    """
    try:
        # 下载图片
        response = requests.get(image_url, timeout=30)
        if response.status_code == 200:
            # 检测图片格式
            content = response.content
            if content.startswith(b'\xff\xd8'):
                ext = '.jpg'
            elif content.startswith(b'\x89PNG'):
                ext = '.png'
            elif content.startswith(b'GIF87a') or content.startswith(b'GIF89a'):
                ext = '.gif'
            elif content.startswith(b'RIFF') and b'WEBP' in content[:12]:
                ext = '.webp'
            else:
                ext = '.png'  # 默认使用png
            
            # 生成安全的文件名：使用时间戳 + 描述前10个字符
            import time
            timestamp = int(time.time())
            # 处理中文和特殊字符，保留字母数字和中文字符
            safe_prompt = "".join(c for c in prompt[:10] if c.isalnum() or '\u4e00' <= c <= '\u9fff')
            if not safe_prompt:  # 如果没有有效字符，使用默认名称
                safe_prompt = "generated_image"
            
            filename = f"{safe_prompt}_{timestamp}{ext}"
            
            # 以二进制写入模式保存图片
            with open(filename, 'wb') as f:
                f.write(content)
            print(f"✅ 图片已保存为: {filename}")
        else:
            print(f"❌ 下载图片失败: {response.status_code}")
    except Exception as e:
        print(f"❌ 保存图片时出错: {e}")

def chat_function():
    """
    智能聊天功能
    与AI进行连续对话，支持上下文记忆
    """
    print("\n💬 聊天模式（输入'返回'退出聊天）")
    messages = []  # 存储对话历史
    
    while True:
        # 获取用户输入
        user_input = input("你: ")
        if user_input == '返回':
            break  # 退出聊天模式
        
        # 将用户消息添加到对话历史
        messages.append({"role": "user", "content": user_input})
        
        # 调用AI API获取回复
        result = call_ai_api(messages)
        reply = result["choices"][0]["message"]["content"]
        
        # 显示AI回复
        print(f"AI: {reply}")
        
        # 将AI回复添加到对话历史，保持上下文
        messages.append({"role": "assistant", "content": reply})

def analyze_emotion_function():
    """
    情感分析功能
    分析用户输入文本的情感倾向
    """
    # 获取用户输入的文本
    text = input("请输入要分析情感的文本: ")
    
    # 构建情感分析请求
    messages = [{"role": "user", "content": f"分析这段话的情感: {text}"}]
    
    # 调用AI API进行情感分析
    result = call_ai_api(messages)
    analysis = result["choices"][0]["message"]["content"]
    
    # 显示分析结果
    print(f"\n🎭 情感分析: {analysis}")

# 主程序入口
if __name__ == "__main__":
    # 显示程序标题
    print("🤖 我的AI个人助理")
    print("=" * 40)
    
    # 主循环：持续显示菜单并处理用户选择
    while True:
        # 显示功能菜单
        print("\n请选择功能:")
        print("1. 智能聊天")
        print("2. 图片生成")
        print("3. 情感分析")
        print("4. 退出程序")
        
        # 获取用户选择
        choice = input("请输入选择 (1-4): ")
        
        # 根据用户选择调用相应功能
        if choice == '1':
            chat_function()  # 智能聊天
        elif choice == '2':
            generate_image_function()  # 图片生成
        elif choice == '3':
            analyze_emotion_function()  # 情感分析
        elif choice == '4':
            print("再见！感谢使用AI助理！")
            break  # 退出程序
        else:
            print("输入错误，请重新选择！")  # 无效输入提示