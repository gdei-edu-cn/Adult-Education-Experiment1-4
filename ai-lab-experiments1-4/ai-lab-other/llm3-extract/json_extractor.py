#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
结构化信息抽取：将自由文本转为JSON结构（示例字段：person, company, date, location）。

与实验四不同：专注信息抽取与JSON格式输出。
"""

import json
import requests
import argparse
from typing import Dict


API_URL = "https://api.siliconflow.cn/v1/chat/completions"
# 直接在代码中设置API Key（示例：sk-xxxx）
API_KEY = "sk-请在此处填写你的密钥"
DEFAULT_MODEL = "Qwen/Qwen2.5-7B-Instruct"


SYSTEM_PROMPT = (
    # 约束模型严格输出JSON，并给出固定字段
    "You are an information extraction assistant. Extract fields into JSON strictly. "
    "Required keys: person (string or null), company (string or null), date (string or null), location (string or null). "
    "Return ONLY valid compact JSON without extra text."
)


def call_chat(messages) -> str:
    """调用聊天接口，返回文本结果。"""
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    data = {"model": DEFAULT_MODEL, "messages": messages, "stream": False}
    r = requests.post(API_URL, headers=headers, json=data, timeout=60)
    r.raise_for_status()
    j = r.json()
    return j["choices"][0]["message"]["content"].strip()


def extract_to_json(text: str) -> Dict[str, object]:
    """将输入文本抽取为JSON对象：包含 person/company/date/location 四个键。

    简单稳健性：若首次解析失败，会在原对话上追加约束并重试一次。
    """
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Text:\n{text}"},
    ]
    out = call_chat(messages)
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        # 简单重试一次，提醒只输出JSON
        messages.append({"role": "assistant", "content": out})
        messages.append({"role": "user", "content": "Return ONLY valid JSON per schema."})
        out2 = call_chat(messages)
        return json.loads(out2)


def main():
    parser = argparse.ArgumentParser(description="结构化信息抽取为JSON")
    parser.add_argument("--text", type=str, default="2025年10月，小王加入了示例科技，入职地点在上海。负责人是李雷。")
    args = parser.parse_args()

    if not API_KEY:
        print("❌ 请先设置环境变量 SILICONFLOW_API_KEY 或在代码中填写 API_KEY")
        return

    data = extract_to_json(args.text)
    print(json.dumps(data, ensure_ascii=False, separators=(",", ":")))

    # 交互：逐行输入文本，立即返回JSON
    print("\n进入交互模式(输入 exit 退出)：")
    while True:
        line = input("> ").strip()
        if not line or line.lower() == "exit":
            break
        obj = extract_to_json(line)
        print(json.dumps(obj, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()


