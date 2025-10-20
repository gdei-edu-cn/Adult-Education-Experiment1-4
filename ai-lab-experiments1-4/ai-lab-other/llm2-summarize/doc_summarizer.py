#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文档摘要器（分段总结 + 合并），基于硅基流动API。

支持摘要风格：
- concise: 简要
- detailed: 详细
- bullet: 要点列表

与实验四不同：专注摘要流程，不提供多功能菜单。
"""

import argparse
import requests
from typing import List


API_URL = "https://api.siliconflow.cn/v1/chat/completions"
# 直接在代码中设置API Key（示例：sk-xxxx）
API_KEY = "sk-请在此处填写你的密钥"
DEFAULT_MODEL = "Qwen/Qwen2.5-7B-Instruct"


def call_chat(messages, model: str = DEFAULT_MODEL) -> str:
    """调用模型获取回复文本。"""
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"model": model, "messages": messages, "stream": False}
    r = requests.post(API_URL, headers=headers, json=data, timeout=60)
    r.raise_for_status()
    j = r.json()
    return j["choices"][0]["message"]["content"].strip()


def split_text(text: str, max_len: int = 800) -> List[str]:
    """粗略分段：按固定长度切片，避免上下文过长。"""
    parts: List[str] = []
    start = 0
    while start < len(text):
        end = min(start + max_len, len(text))
        parts.append(text[start:end])
        start = end
    return parts


def summarize_chunk(chunk: str, style: str) -> str:
    """对单段文本生成小结，样式由 style 控制。"""
    style_hint = {
        "concise": "Provide a concise summary in 2-3 sentences.",
        "detailed": "Provide a detailed summary in 5-7 sentences.",
        "bullet": "Provide bullet-point key takeaways.",
    }.get(style, "Provide a concise summary in 2-3 sentences.")

    msgs = [
        {"role": "system", "content": "You are a helpful summarization assistant."},
        {"role": "user", "content": f"{style_hint}\nText:\n{chunk}"},
    ]
    return call_chat(msgs)


def summarize_document(text: str, style: str) -> str:
    """分段-合并策略的整体摘要：
    1) 拆分文本；2) 每段小结；3) 合并小结得到最终摘要。
    """
    chunks = split_text(text)
    partials = [summarize_chunk(c, style) for c in chunks]
    joiner = "\n\n".join(partials)

    # 合并阶段
    style_hint = {
        "concise": "Combine the following partial summaries into a concise final summary.",
        "detailed": "Combine and elaborate into a detailed final summary.",
        "bullet": "Merge into a clean bullet list of key points.",
    }.get(style, "Combine into a concise final summary.")

    msgs = [
        {"role": "system", "content": "You are a helpful summarization assistant."},
        {"role": "user", "content": f"{style_hint}\nPartial summaries:\n{joiner}"},
    ]
    return call_chat(msgs)


def main():
    parser = argparse.ArgumentParser(description="文档摘要器（分段+合并）")
    parser.add_argument("--text", type=str, default="人工智能正在改变世界。许多行业借助AI提高效率...（此处省略长文示例）")
    parser.add_argument("--style", type=str, choices=["concise", "detailed", "bullet"], default="bullet")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL)
    args = parser.parse_args()

    if not API_KEY:
        print("❌ 请先设置环境变量 SILICONFLOW_API_KEY 或在代码中填写 API_KEY")
        return

    result = summarize_document(args.text, args.style)
    print(result)

    # 交互模式：空行触发一次摘要生成，便于粘贴多段长文本
    print("\n进入交互模式，粘贴长文本(输入 exit 退出)：")
    buf: List[str] = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip().lower() == "exit":
            break
        if not line.strip():
            long_text = "\n".join(buf)
            buf.clear()
            if not long_text.strip():
                continue
            print(summarize_document(long_text, args.style))
            print("\n(继续输入或 exit 退出)")
        else:
            buf.append(line)


if __name__ == "__main__":
    main()


