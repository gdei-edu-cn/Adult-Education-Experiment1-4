# 实验1：Python环境测试

## 📋 实验目标
- 验证Python是否正确安装
- 测试Python基本功能
- 熟悉Python运行环境

## 🎯 实验内容
运行 `hello_world.py` 程序，测试Python环境是否配置正确。

## 📦 所需软件
- **Python 3.7+** （已安装）
- **文本编辑器** （如VS Code、PyCharm或记事本）

## 🚀 运行步骤

### 方法1：使用VS Code
1. 打开VS Code
2. 打开 `hello_world.py` 文件
3. 按 `Ctrl + F5` 或点击右上角的"运行"按钮

### 方法2：用VS Code终端运行
1. 在VS Code底部点击“终端”或菜单选择“查看”->“终端”
2. 在终端中输入：
   ```
   python hello_world.py
   ```
   如果提示找不到 python，请尝试
   ```
   python3 hello_world.py
   ```
3. 按回车，即可看到运行结果

## ✅ 预期结果
如果Python安装正确，你会看到类似以下的输出：
```
Hello, World!
你好，世界！

=== Python环境信息 ===
Python版本: 3.x.x
Python路径: /usr/bin/python3

🎉 恭喜！Python安装成功，所有测试通过！
```

## ❌ 常见问题

### 问题1：提示"python不是内部或外部命令"
**解决方案**：
- 检查Python是否正确安装
- 尝试使用 `python3` 命令
- 将Python添加到系统环境变量

### 问题2：文件路径错误
**解决方案**：
- 确保在正确的目录下运行命令
- 使用 `dir`（Windows）或 `ls`（Mac/Linux）查看当前目录文件

### 问题3：编码错误
**解决方案**：
- 确保文件保存为UTF-8编码
- 在Windows上可能需要设置编码：`chcp 65001`


