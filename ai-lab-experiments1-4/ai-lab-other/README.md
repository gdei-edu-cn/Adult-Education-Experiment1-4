# AI Lab Other（基于硅基流动API的大模型实验）

本目录包含三类与实验四不同方向的LLM应用示例：

- `llm1-translate/` 翻译与语气润色助手
- `llm2-summarize/` 文档摘要器（长文本分段+合并）
- `llm3-extract/` 结构化信息抽取为JSON

均提供完善中文README与详细代码注释，调用方式与 `ai-lab-ch4` 一致（需先配置API Key）。

## 运行前准备

1. 获取硅基流动API密钥，确保账户有余额。
2. 环境依赖：
   ```bash
   pip install requests
   ```
3. 在各实验代码文件内设置 `API_KEY`（或改为从环境变量读取）。

## 快速开始

进入某实验目录，阅读对应 `README.md` 并按其运行命令执行。

# AI Lab Other 实验集

本目录收录若干轻量但完整的NLP实验示例（含代码与详尽中文说明/注释），便于初学者快速上手与扩展。

## 目录结构

- `exp1-sentiment/` 基于情感词典的情感分析
- `exp2-summarization/` 基于词频抽取的文本摘要
- `exp3-keywords/` 基于简易TF-IDF的关键词提取
 - `exp4-caesar/` 凯撒密码：字母循环位移的加/解密与爆破
 - `exp5-textstats/` 文本统计小助手：字符/词/句与Top-K词频
 - `exp6-madlibs/` 趣味填词：交互式搞笑故事生成器

## 运行环境

- Python ≥ 3.7（与项目其余章节一致即可）。
- 仅使用标准库与极少量依赖（如需）。每个实验README会明确说明。

## 快速开始

进入具体实验目录，阅读对应 `README.md`，按说明运行。如：

```bash
cd exp1-sentiment
python sentiment_lexicon.py
```

## 学习建议

- 从可解释的经典方法入手（词典法/词频法/TF-IDF），理解核心思想与实现细节；
- 再对比现代大模型/向量化方案，思考两者优缺点与适用场景；
- 保持可测可复现，便于课堂教学与实验报告撰写。


