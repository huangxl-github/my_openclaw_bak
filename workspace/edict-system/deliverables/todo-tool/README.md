# 📝 TodoList CLI - 命令行待办事项管理工具

一个轻量级的命令行待办事项管理工具，支持增删改查、标记完成等功能。

---

## ✨ Features

- ✅ 快速添加/查看/删除任务  
- 🏷️ 支持优先级标记（高/中/低）
- ⏰ 可设置截止时间
- 💾 数据持久化存储（JSON）
- 🔍 按状态过滤（待办/已完成）

---

## 🚀 Quick Start

```bash
# 添加任务
todo add "写代码" --priority high --due "2026-03-15"

# 查看所有任务  
todo list

# 标记完成
todo done 1

# 删除任务
todo delete 2
```

---

## 🛠️ 安装

将脚本保存为 `todo.py`，然后：

```bash
python todo.py --help
```

或使用别名（~/.bashrc / .zshrc）:
```bash
alias todo="python ~/tools/todo.py"
```
