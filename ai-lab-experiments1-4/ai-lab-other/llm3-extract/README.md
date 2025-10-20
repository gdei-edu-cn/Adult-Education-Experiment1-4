# LLM实验3：结构化信息抽取为JSON

本实验示范如何从非结构化文本中抽取结构化字段（如人名、公司名、日期、地点等），并输出为JSON，便于后续存储或分析。

## 核心思路

- 通过系统提示明确输出JSON模式与字段说明
- 给定示例（few-shot，可选），提升输出稳定性
- 做最小验证：解析JSON失败时重试一次

## 文件说明

- `json_extractor.py`：主程序，包含提示词、调用封装与JSON解析/重试逻辑。

## 依赖

```bash
pip install requests
```

## 配置

```bash
export SILICONFLOW_API_KEY="sk-..."
```

## 运行示例

```bash
python json_extractor.py --text "2025年10月，小王加入了示例科技，入职地点在上海。负责人是李雷。"
```

## 与实验四的区别

- 专注信息抽取和JSON结构化输出，不涉及聊天或图片。


