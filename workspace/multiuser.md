# multiuser.md - 多用户支持指南

## 🎯 核心原则

1. **每个用户有独立空间**: `users/<用户名>/` 目录
2. **私密信息隔离**: 不同用户的 MEMORY.md 绝对不交叉
3. **上下文自动选择**: 根据 sender_id 决定加载哪个配置

---

## 📁 文件结构

```
workspace/
├── IDENTITY.md              # 我的身份（全局）
├── USER.md                  # 主用户/默认用户
├── MEMORY.md                # 主用户的长期记忆
│
├── users/                   # 所有其他用户独立空间
│   ├── hongxing/           # 飞书用户示例
│   │   ├── IDENTITY.md     # （可选）个性化设定
│   │   ├── USER.md         # 这个人是谁 👈 关键！
│   │   └── MEMORY.md       # 他的记忆（私密，仅在私聊加载）
│   │
│   ├── zhangsan/
│   │   └── ...
│
└── memory/                  # 每日对话日志保留原始结构
    └── 2026-03-09.md       # (可考虑按用户拆分)
```

---

## 🔐 加载规则（会话启动时）

### **场景 A：私聊**

```
if 消息来自 users/用户名/:
    1. 读取 workspace/IDENTITY.md     ← 我是谁
    2. 读取 users/用户名/USER.md     ← 关于这个人
    3. 读取 users/用户名/MEMORY.md   ← 这个人的记忆（私密！）
    4. 读取 memory/YYYY-MM-DD.md      ← 当天对话记录
    
if 消息来自主用户（默认 USER.md）:
    1. 读取 workspace/IDENTITY.md
    2. 读取 workspace/USER.md  
    3. 读取 workspace/MEMORY.md
    4. 读取 memory/YYYY-MM-DD.md
```

### **场景 B：群聊**

```
if 群聊环境:
    1. 读取 workspace/IDENTITY.md     ← 我是谁
    2. ✖️ 跳过 USER.md/MEMORY.md      ← 保护隐私！
    3. 可选：检查是否有 users/<用户名>/ 的群组配置
    
⚠️ 群聊中绝不加载私人记忆文件，只保持基础身份和当天日志
```

---

## 💡 实现建议

### **方案一：简单版（推荐先试这个）**

1. 在 `users/` 目录为每个用户提供独立文件夹
2. 每次对话开始时检查：
   - 如果 `USER.md` 存在 → 加载主用户配置
   - 如果有对应用户名 → 切换到 `users/<用户名>/` 的上下文

**优点**: 
- 改动最小，现有逻辑不用大改
- 支持逐步扩展

### **方案二：彻底版（未来优化）**

1. 创建一个 `user_mapping.json`:
```json
{
  "ou_d86ffdee05f6281c11d732f7d1284ddb": {
    "username": "hongxing",
    "platform": "feishu",
    "path": "users/hongxing/"
  }
}
```

2. 在 session startup 时根据 sender_id 动态加载路径
3. 所有配置文件都基于相对路径，用户目录隔离

**优点**:
- 更灵活支持跨平台（飞书、Telegram、Discord 等）
- 更容易做权限控制

---

## 🚀 下一步行动

### **立即可以做的：**
1. ✅ 创建 `users/` 目录结构
2. ✅ 为当前用户提供示例配置
3. ✅ 测试新逻辑是否正常工作

### **需要用户确认的：**
1. 👤 您的用户名想叫啥？（用于创建文件夹）
2. 📂 现有 MEMORY.md 要不要迁移到新结构？（保持主用户模式也可以）
3. 🔐 哪些平台算"私聊"可以加载记忆？

---

**建议：先做简单版！用起来再说。**
