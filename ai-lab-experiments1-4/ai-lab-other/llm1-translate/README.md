# LLM实验1：翻译与语气润色助手（基于硅基流动API）

本实验构建一个“翻译+语气控制”的小工具：支持中英互译，并可选择语气风格（正式、口语、友好、学术等）。

## 核心思路

- 以系统提示词约束风格，结合用户指令和文本，调用聊天补全接口返回译文。
- 提供简单命令行参数与交互模式。

## 文件说明

- `translate_tone.py`：主程序，包含翻译、语气模板与调用封装。

## 依赖

```bash
pip install requests
```

## 配置

- 打开 `translate_tone.py`，将 `API_KEY` 设置为你的密钥，或在运行前设置环境变量：
  ```bash
  export SILICONFLOW_API_KEY="sk-..."
  ```

## 运行示例

```bash
python translate_tone.py --text "今天天气很好" --direction zh2en --tone formal
python translate_tone.py --text "This is awesome!" --direction en2zh --tone friendly
```

也可直接运行进入交互模式：

```bash
python translate_tone.py
```

## 注意

- 与实验四不同：本实验专注“翻译+语气”而非通用助理。
- 长文本将自动分段处理并合并结果（简化版）。


