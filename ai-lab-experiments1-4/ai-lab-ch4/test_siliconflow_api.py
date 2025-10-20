# 硅基流动API连通性测试程序
# 简单测试API密钥是否有效，模型是否连通

import requests  # 用于发送HTTP请求

# 配置API相关参数
API_KEY = "sk-oqfienrjzxwlowarsbbgzgbffovxhknumlkfqmrazxayospz"  # 请在此处填入您的硅基流动API密钥
API_URL = "https://api.siliconflow.cn/v1/chat/completions"  # 聊天API地址

def test_api_connection():
    """
    测试API连接是否正常
    发送一个简单的测试请求，验证API密钥和网络连接
    """
    print("🔍 正在测试API连接...")
    
    # 检查API密钥是否已填入
    if not API_KEY:
        print("❌ API密钥为空，请在代码中填入您的API密钥")
        return False
    
    # 设置请求头，包含API密钥和内容类型
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # 构建测试请求数据
    test_data = {
        "model": "Qwen/Qwen2.5-7B-Instruct",  # 使用默认模型
        "messages": [{"role": "user", "content": "你好"}],  # 简单的测试消息
        "stream": False  # 不使用流式输出
    }
    
    try:
        # 发送POST请求到API
        response = requests.post(API_URL, headers=headers, json=test_data, timeout=30)
        
        # 检查响应状态码
        if response.status_code == 200:
            # 解析JSON响应
            result = response.json()
            # 检查响应格式是否正确
            if "choices" in result and len(result["choices"]) > 0:
                reply = result["choices"][0]["message"]["content"]
                print(f"✅ API连接成功！AI回复: {reply}")
                return True
            else:
                print("❌ API响应格式异常")
                return False
        else:
            # 处理HTTP错误
            print(f"❌ HTTP错误: {response.status_code}")
            try:
                error_detail = response.json()
                if "error" in error_detail:
                    print(f"   错误详情: {error_detail['error']}")
            except:
                pass
            return False
            
    except requests.exceptions.Timeout:
        print("❌ 请求超时，请检查网络连接")
        return False
    except requests.exceptions.ConnectionError:
        print("❌ 网络连接失败，请检查网络设置")
        return False
    except Exception as e:
        print(f"❌ 未知错误: {str(e)}")
        return False

# 主程序
if __name__ == "__main__":
    print("硅基流动API连通性测试")
    print("=" * 30)
    
    # 运行连接测试
    success = test_api_connection()
    
    # 显示测试结果
    if success:
        print("\n🎉 测试通过！API连接正常，可以正常使用AI功能")
    else:
        print("\n❌ 测试失败！请检查:")
        print("1. API密钥是否正确")
        print("2. 网络连接是否正常")
        print("3. 账户是否有足够的余额")
