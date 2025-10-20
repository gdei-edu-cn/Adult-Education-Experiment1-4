#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
翻译与语气润色助手（硅基流动API）

功能：
- 中英互译：--direction zh2en / en2zh
- 语气风格：--tone formal|informal|friendly|academic
- 自动分段：对较长文本做简单分段，逐段翻译后合并

与实验四不同：本工具专注“翻译+语气控制”，而非综合助理。
"""

import argparse
import requests
from typing import List


API_URL = "https://api.siliconflow.cn/v1/chat/completions"
# 直接在此处填写你的硅基流动 API Key（示例：sk-xxxx）。请妥善保管，勿提交到公共仓库。
API_KEY = ""
# 默认聊天模型，可在命令行参数里覆盖
DEFAULT_MODEL = "Qwen/Qwen2.5-7B-Instruct"


TONE_SYSTEM_PROMPTS = {
    # 正式：适合公文/邮件/报告
    "formal": "You are a professional translator. Translate accurately with a formal tone.",
    # 口语：更随意、贴近日常表达
    "informal": "You are a casual translator. Translate with a relaxed, informal tone.",
    # 友好：亲切友善，语气柔和
    "friendly": "You are a friendly translator. Use warm and approachable tone.",
    # 学术：更严谨、术语更规范
    "academic": "You are an academic translator. Translate rigorously with academic tone.\n",
}


def call_chat_api(messages, model: str = DEFAULT_MODEL):
    """调用硅基流动聊天补全接口，返回模型回复文本。

    参数：
        messages: 聊天历史（system/user/assistant）
        model:    使用的模型名称

    返回：
        模型生成的文本内容（字符串）
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "messages": messages,
        "stream": False,
    }
    resp = requests.post(API_URL, headers=headers, json=data, timeout=60)
    resp.raise_for_status()
    j = resp.json()
    return j["choices"][0]["message"]["content"].strip()


def chunk_text(text: str, max_len: int = 600) -> List[str]:
    """将较长文本按长度粗略切片，避免超长上下文。

    说明：
    - 为简化演示，按固定长度切；实际可按句号/段落更智能地切分。
    """
    chunks: List[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_len, len(text))
        chunks.append(text[start:end])
        start = end
    return chunks


def translate(text: str, direction: str, tone: str) -> str:
    """执行翻译并控制语气风格。

    - 根据 direction 决定中英方向；
    - 使用 system 提示控制整体语气风格；
    - 对长文本分段翻译后拼接。
    """
    if tone not in TONE_SYSTEM_PROMPTS:
        tone = "formal"
    system_prompt = TONE_SYSTEM_PROMPTS[tone]

    if direction == "zh2en":
        user_prompt = f"Translate the following Chinese into English with the specified tone. Text:\n{text}"
    elif direction == "en2zh":
        user_prompt = f"请将以下英文翻译成中文，并遵循指定语气风格。文本：\n{text}"
    else:
        raise ValueError("direction must be zh2en or en2zh")

    # 长文本分段，逐段翻译再合并，降低超长导致的失败概率
    parts = chunk_text(text)
    outputs: List[str] = []
    for part in parts:
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt.replace(text, part)},
        ]
        outputs.append(call_chat_api(messages))
    return "".join(outputs)


def main():
    parser = argparse.ArgumentParser(description="翻译与语气润色助手")
    parser.add_argument("--text", type=str, default="今天天气很好，我们去公园散步吧。")
    parser.add_argument("--direction", type=str, choices=["zh2en", "en2zh"], default="zh2en")
    parser.add_argument("--tone", type=str, choices=list(TONE_SYSTEM_PROMPTS.keys()), default="formal")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL)
    args = parser.parse_args()

    if not API_KEY:
        print("❌ 请先设置环境变量 SILICONFLOW_API_KEY 或在代码中填写 API_KEY")
        return

    result = translate(args.text, args.direction, args.tone)
    print(result)

    # 交互模式：持续读取用户输入并翻译
    print("\n进入交互模式(输入 exit 退出)：")
    while True:
        line = input("> ").strip()
        if not line or line.lower() == "exit":
            break
        print(translate(line, args.direction, args.tone))


if __name__ == "__main__":
    main()


