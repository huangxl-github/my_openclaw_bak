# 多用户记忆系统 - 完整使用指南

## 🎯 设计理念

**每个对话方 = 独立人格**
- 私聊的人 → 有深度记忆（兴趣、偏好、历史对话）
- 群里的人 → 有基础信息（在哪个群出现、发言风格、被提到过的项目）
- 跨平台同一人 → 能识别出是同一个人（通过 open_id）

---

## 📁 最终文件结构

```
workspace/
├── IDENTITY.md                    # 👤 我的身份（我是谁、性格设定）
│
├── users/                         # 🔥 所有对话对象独立空间
│   │
│   ├── hongxing/                  # 私聊用户示例
│   │   ├── USER.md               # 这个人是谁
│   │   ├── MEMORY.md             # 🧠 长期记忆：兴趣、偏好、重要事件
│   │   └── history/              # 📅 对话历史归档（可选）
│   │       └── 2026-03-09.md    # 当天详细对话记录
│   │
│   ├── zhangsan/                 # 另一个用户
│   │   ├── USER.md
│   │   └── MEMORY.md
│   │
│   │
│   ├── groups/                   # 🏢 群组空间（群聊记忆）
│   │   │
│   │   ├── feishu_ou_xxx/        # 飞书群 "技术交流群"
│   │   │   ├── INFO.md           # 群信息：成员列表、建群目的
│   │   │   └── MEMORY.md         # 群的上下文：讨论过的项目、重要决定
│   │   │
│   │   ├── discord_123456/       # Discord 服务器或频道
│   │   │   └── ...
│   │
│   └── cross_platform/           # 🌐 跨平台用户映射（可选）
│       └── user_mapping.json    # {"open_id": "username"} 关联关系
│
├── memory/                        # 📝 全局对话日志（保留原有结构）
│   └── 2026-03-09.md             # 今日总览（可简化为只记重要事件）
│
└── config/                        # ⚙️ 配置文件
    ├── user_mapping.json         # sender_id → username 映射表
    └── load_rules.md             # 不同场景的加载规则说明
```

---

## 👤 用户类型详解

### **A. 私聊用户（深度记忆）**

例如：`users/hongxing/`

**USER.md** - 档案:
```markdown
# USER.md - hongxing

- **Name**: Hong Xing (黄小明)
- **平台**: 飞书私聊
- **open_id**: ou_d86ffdee05f6281c11d732f7d1284ddb
- **关系**: 主要用户/管理员

## 特点
- 企业级 Java 开发
- RuoYi-Office OA 系统学习
- 对多用户记忆系统感兴趣

## 偏好
- 响应速度重要
- 技术细节要详细但不冗长
```

**MEMORY.md** - 长期记忆:
```markdown
# MEMORY - hongxing 的记忆

_2026-03-09_: 
- 首次询问 RuoYi-Office 开发规范，已分享完整技术栈
- 要求建立多用户记忆系统（已完成框架搭建）
- 需要记住群聊中的发言和互动

_重要信息:_
- 工作：Java 后端开发
- 项目：正在研究 OA 工作流引擎
```

### **B. 群组空间（集体记忆）**

例如：`users/groups/技术交流群/`

**INFO.md**:
```markdown
# INFO - 技术交流群

- **成员**: hongxing, zhangsan, lisi...
- **主题**: Java 开发、开源分享
- **创建于**: 2026-03-01
```

**MEMORY.md**:
```markdown
# MEMORY - 群的上下文

_2026-03-09_: 
- hongxing 询问了 RuoYi-Office 相关问题
- zhangsan 提出了工作流优化建议
```

### **C. 跨平台识别（可选高级功能）**

`config/user_mapping.json`:
```json
{
  "ou_d86ffdee05f6281c11d732f7d1284ddb": {
    "name": "hongxing",
    "platforms": ["feishu"],
    "path": "users/hongxing/"
  },
  "telegram_123456": {
    "name": "hongxing_telegram", 
    "platforms": ["telegram"],
    "path": "users/hongxing/",  // 可能映射到同一个人的不同平台账号
    "linked_to": "hongxing"     // 可选：关联主账号
  }
}
```

---

## 🔄 会话启动流程（自动化逻辑）

```python
# 伪代码示例

def load_context(session):
    """每次会话开始时的加载逻辑"""
    
    # 1. 始终加载基础身份
    load_file("IDENTITY.md")          # 我是谁
    
    # 2. 获取当前对话对象信息
    sender_id = session.sender_id     # "ou_xxxxx"
    platform = session.channel        # "feishu"
    chat_type = session.chat_type     # "direct" or "group"
    
    # 3. 映射到用户名
    username = get_username(sender_id)  # 查 user_mapping.json
    
    # 4. 判断场景并加载对应记忆
    if chat_type == "direct":
        # 私聊场景 - 可以加载深度记忆
        load_file(f"users/{username}/USER.md")
        load_file(f"users/{username}/MEMORY.md")
        
    elif chat_type == "group":
        # 群聊场景 - 只加载群组公共记忆，不泄露个人隐私
        group_id = session.chat_id
        load_file(f"users/groups/{group_id}/INFO.md")
        load_file(f"users/groups/{group_id}/MEMORY.md")
        # ⚠️ 绝不加载 USER.md/MEMORY.md（隐私保护）
        
    # 5. 加载当天的对话记录（可选简化版）
    today = get_today_date()
    load_file(f"memory/{today}.md")    # 全局日志
    
    # 6. 如果是新用户，自动创建档案
    if not file_exists(f"users/{username}/USER.md"):
        create_user_profile(username, sender_id, platform)
```

---

## 🛠️ 自动化操作指南

### **场景 1：私聊首次对话**
```bash
# 系统自动检测并创建
mkdir -p users/新用户名/
echo "创建用户档案..."
```

### **场景 2：群聊首次出现**
```bash
# 记录群里出现过的新成员，但不给深度隐私
# 只在组的 MEMORY.md 记下："张三在 3-9 第一次发言"
```

### **场景 3：用户跨平台（可选）**
```json
{
  "ou_xxx_feishu": "hongxing",      // 飞书账号
  "telegram_yyy": "hongxing_telegram" // 可能是同一个人
}
```

---

## 📊 记忆分级策略

| 文件类型       | 私聊加载 | 群聊加载 | 作用                         |
|----------------|----------|----------|------------------------------ |
| `IDENTITY.md`  | ✅ 是     | ✅ 是     | 我是谁（共享）               |
| `USER.md`      | ✅ 是     | ❌ 否     | 对方是谁（私密档案）         |
| `MEMORY.md`    | ✅ 是     | ❌ 否     | 长期记忆（个人隐私！）       |
| `GROUP.INFO.md`| ❌ 不相关 | ✅ 是     | 群组基本资料                 |
| `GROUP.MEMORY.md`| -      | ✅ 是     | 群聊上下文（共享记忆）       |
| `memory/YYYY-MM-DD.md` | ✅ | ✅        | 今日对话全局记录（可简化）   |

---

## 🚀 下一步执行清单

### **Phase 1: 基础框架**（已完成 ✅）
- [x] 创建 users/目录结构
- [x] 配置主用户 hongxing 档案
- [x] 编写多用户使用文档

### **Phase 2: 完善系统**（进行中 🔄）
- [ ] 创建 group 群组示例目录
- [ ] 建立 user_mapping.json 映射表
- [ ] 测试不同场景下的记忆加载逻辑

### **Phase 3: 自动化扩展**（未来目标 🔮）
- [ ] 自动检测新用户并创建档案
- [ ] 定期整理历史对话归档
- [ ] 跨平台用户关联识别

---

## ⚠️ 重要提醒

1. **隐私保护优先**: 绝不在群聊环境加载私人 MEMORY.md
2. **渐进式建设**: 先用起来，边用边改
3. **手动确认**: 新用户档案先空着，等您补充信息再填
4. **定期清理**: 旧的每日对话记录可归档或压缩

---

**🎯 现在您可以：**
- ✅ 在任何群聊使用我，我会记住群的上下文
- ✅ 私聊时享受深度记忆服务
- ✅ 随时查看/编辑 `users/` 里任何人的档案

需要我帮您完善哪个部分？或者先测试一下现有功能？ 🚀