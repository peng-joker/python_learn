## hand_crafted_AI_agent

### 概述

一个轻量的命令行 AI Agent 示例，基于 `pydantic-ai` 框架与可插拔工具机制构建。当前集成 DeepSeek 兼容的 OpenAI 风格接口，通过简单的文件操作工具（读取、列出、重命名）与本地 `test/` 目录交互。

### 目录结构

```
hand_crafted_AI_agent/
├─ main.py          # 程序入口：模型与 Agent 初始化、对话循环
├─ tools.py         # 工具实现：read_file / list_files / rename_file
├─ test/            # 演示用文件目录（操作作用域）
│  ├─ a.php
│  ├─ b.py
│  ├─ c.js
│  ├─ d.css
│  ├─ e.c
│  └─ f.go
└─ README.md
```

### 运行原理

- 使用 `dotenv` 加载环境变量 `DEEPSEEK_API_KEY` 与 `base_url`。
- 通过 `OpenAIModel` + `OpenAIProvider` 指定模型（示例为 `deepseek-chat`）和服务端地址/密钥。
- 构建 `Agent`，注册工具：
  - `tools.read_file(name)`：读取 `test/` 内指定文件内容。
  - `tools.list_files()`：递归列出 `test/` 内所有文件（相对路径）。
  - `tools.rename_file(name, new_name)`：将 `test/` 内文件重命名/移动到新路径（仍限定在 `test/` 目录内）。
- 进入命令行循环，持续读取用户输入，输出 Agent 回复。

### 先决条件

- 已安装 Python（建议 3.9+）。
- 可访问的类 OpenAI 接口（例如 DeepSeek 兼容接口），并具备 API Key。

### 安装

```bash
# 1) 创建虚拟环境（可选）
python -m venv .venv && source .venv/bin/activate

# 2) 升级 pip
python -m pip install -U pip

# 3) 安装依赖
pip install pydantic-ai python-dotenv
```

> 说明：导入包名为 `pydantic_ai`，对应的 PyPI 包名是 `pydantic-ai`。

### 配置

在项目根目录创建 `.env` 文件（或通过系统环境变量设置）：

```ini
DEEPSEEK_API_KEY=你的_API_Key
base_url=你的_模型服务_base_url
```

示例（仅作占位，请按你的实际服务地址填写）：

```ini
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxx
base_url=https://api.your-deepseek-compatible-endpoint/v1
```

### 运行

```bash
python main.py
```

运行后，终端会提示 `Input:`，直接输入指令/问题即可。对话历史将被保留在会话内存中。

### 可用工具（当前）

- **read_file(name: str) -> str**：
  - 读取 `test/` 目录下 `name` 指定的文件内容。
  - 失败时返回错误信息字符串。

- **list_files() -> list[str]**：
  - 递归列出 `test/` 目录内所有文件的相对路径。

- **rename_file(name: str, new_name: str) -> str**：
  - 将 `test/` 内文件重命名/移动为 `new_name`。
  - 内置防护：若新路径不在 `test/` 目录内会直接报错，避免越权移动。
  - 若上级目录不存在，会自动创建所需的父级目录。

> 工具的根工作目录由 `tools.py` 中的 `base_dir = Path("./test")` 指定。

### 示例

- 查看有哪些演示文件：

```text
Input: 列出 test 目录下的所有文件
```

- 读取某个文件：

```text
Input: 读取文件 b.py 的内容
```

- 重命名/移动文件（仍在 `test/` 内）：

```text
Input: 把 c.js 重命名为 scripts/c.min.js
```

### 常见问题排查

- **认证失败（401/403）**：检查 `.env` 中 `DEEPSEEK_API_KEY` 是否正确；确认 `base_url` 可用且与模型提供方匹配。
- **网络错误/超时**：确认网络连通性与代理设置；检查服务端状态。
- **文件相关错误**：
  - 读取失败：确认 `test/` 目录下目标文件存在、名称正确。
  - 重命名失败：`new_name` 必须仍位于 `test/` 目录中。
- **编码问题**：跨平台文件编码可能导致读取异常，必要时手动调整文件编码为 UTF-8。

### 扩展与定制建议

- 新增更多实用工具：如搜索、统计、批量处理等。
- 增强对话体验：加入流式输出、错误重试策略、调用日志等。
- 支持多模型/多提供方：通过配置切换不同模型或服务端。
- 权限与安全：对高风险操作增加确认与审计。

### 许可证

仓库当前未包含许可证文件。若需开源分发，请新增相应的 `LICENSE` 并在此处注明。


