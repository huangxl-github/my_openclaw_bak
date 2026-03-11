# OpenClaw Skills 完全指南  
## 📚 好用技能目录 & 安装教程

**版本**: 2026.3.7  
**更新日期**: 2026-03-09  
**作者**: Your AI Assistant  

---

## 🎯 什么是 Skill？

**Skill（技能）** 是 OpenClaw 的能力扩展模块，让 AI 助手获得特定领域的专业操作能力。就像手机 APP 一样，一个 skill = 一个功能模块。

### 💡 **为什么需要 Skills？**
- ✅ **开箱即用**：不用自己开发复杂逻辑，直接调现成工具
- ✅ **标准化流程**：每个 skill 都遵循最佳实践
- ✅ **扩展性强**：可以从 clawhub.com 下载更多 community skills
- ✅ **场景丰富**：从文件处理到设备控制一网打尽

---

## 📦 当前已安装 Skills（共 8+2 个）

### **🏠 系统内置 Skills**（位于 `node_modules\openclaw\skills`）

| # | Skill 名称 | 功能描述 | 适用场景 | 推荐指数 |
|--:|---------|---------|------|:-:|
| 1 | **coding-agent** | 调用 Codex/Claude/Pi 等 AI 写代码代理 | 复杂编程任务、PR 审查、重构大项目 | ⭐⭐⭐⭐⭐ |
| 2 | **healthcheck** | 自动安全扫描（防火墙/更新/SSH） | VPS/服务器定期巡检、风险管控 | ⭐⭐⭐⭐ |
| 3 | **nano-pdf** | PDF 智能编辑与文本提取 | 修改合同/报告、批量处理文档 | ⭐⭐⭐⭐ |
| 4 | **skill-creator** | 创建自定义 Skills 框架 | 开发个人专用扩展模块 | ⭐⭐⭐ |
| 5 | **video-frames** | FFmpeg 视频切帧/提取片段 | GIF 制作、短视频素材截取 | ⭐⭐⭐⭐ |
| 6 | **weather** | 查询天气（WTTR.IN） | 出行提醒、生活助手 | ⭐⭐⭐ |

---

### **📱 Feishu Extension**（位于 `.openclaw\extensions\feishu`）

| # | Skill 名称 | 功能描述 | 依赖环境 | 推荐指数 |
|--:|---------|---------|------|:-:|
| 7 | **feishu-doc** | 飞书文档读写/表格编辑 | 已登录企业账号 | ⭐⭐⭐⭐⭐ |
| 8 | **feishu-drive** | 飞书云盘文件管理 | - | ⭐⭐⭐⭐ |
| 9 | **feishu-perm** | 权限共享与协作人管理 | - | ⭐⭐⭐ |
| 10| **feishu-wiki** | 知识百科导航/创建 | 已建知识库 | ⭐⭐⭐⭐ |

---

## 🔥 Top 5 强烈推荐 Skills

### 🥇 #1：**coding-agent**（编程代理）

**一句话卖点：**  
> "自己写代码太慢？让 Codex/Claude Code/Pi Agent 替你干！"

#### ✨ **核心能力**
- 自动搭建项目脚手架
- 生成完整功能模块
- 审查 PR / Debug 报错日志
- 重构大型遗留代码

#### 🔧 **安装方式**（已预装）
```powershell
# 确认存在
Test-Path "C:\Users\huangxiaolong\AppData\Roaming\npm\node_modules\openclaw\skills\coding-agent"
```

#### 📖 **使用示例**
> 直接说需求即可：
> 
> - "用 Python 写一个爬虫抓股票数据"
> - "帮我优化这段 SQL 查询效率"
> - "Review 这个 PR，找出潜在 bug"
> - "重构 user-service 模块，提取到独立微服务"

#### 💰 **价值体现**
- ⏱️ **节省时间**: 50% 重复劳动自动化  
- 🎯 **代码质量**: AI 遵循最佳实践 + 社区模式  
- 🧠 **技术学习**: 看懂生成的优秀代码就是成长  

---

### 🥈 #2：**nano-pdf**（PDF 编辑）

**一句话卖点：**  
> "Word 能改，PDF 为什么不能？用它直接编辑 PDF！"

#### ✨ **核心能力**
- 文字增删/替换/高亮
- 添加注释与批注
- 提取文本转 Markdown
- 合并/拆分 PDF（CLI）

#### 🔧 **安装方式**（需要补充依赖）
```powershell
# 检查是否已装 nano-pdf CLI
nano-pdf --version

# 如果缺失则安装（npm 或 brew）
npm install -g @artificialio/nano-pdf-cli
# 或者
brew install nano-pdf
```

#### 📖 **使用示例**
> - "把合同第 3 页的价格改成¥50,000"
> - "提取这份 PDF 里所有的表格数据"
> - "把这个 PDF 转成 Markdown"
> - "删除报告最后两页的附录"

#### 💰 **价值体现**
- 📄 **处理效率**: 省去"PDF → Word → 改完 → 再转回 PDF"的痛苦流程  
- 🎨 **专业度提升**: 输出格式完美，无排版错乱  
- 💼 **商务场景**: 合同/发票快速修改  

---

### 🥉 #3：**feishu-doc**（飞书文档管理）

**一句话卖点：**  
> "不用切到浏览器，直接命令行操作飞书文档！"

#### ✨ **核心能力**
- 创建/写入/追加文档内容
- 插入表格、图片、富文本
- 批量更新多人协作文件
- 上传附件（合同/报告）

#### 🔧 **安装方式**（已预装，需登录飞书权限）
```powershell
# 确认位置
Get-Content "C:\Users\huangxiaolong\.openclaw\extensions\feishu\skills\feishu-doc\SKILL.md"
```

#### 📖 **使用示例**
> - "创建一个文档《周报_2026-03-09》并填入这些内容..."
> - "在 `docx/xxx` 文档末尾追加一段总结"
> - "上传这张截图到 Feishu Docs"
> - "读取知识库里的需求文档，提取关键事项"

#### 💰 **价值体现**
- 🔄 **跨平台整合**: 飞书机器人 + AI 助手无缝联动  
- 🤖 **自动化场景**: 日报/周报定时推送  
- 📊 **知识库构建**: 把聊天沉淀成结构化文档  

---

### #4：**healthcheck**（系统安全巡检）

**一句话卖点：**  
> "服务器多久没更新了？自动跑一遍安全检查！"

#### ✨ **核心能力**
- 检查系统补丁/漏洞更新
- 防火墙规则审核
- SSH 配置加固建议
- 定期定时任务执行

#### 🔧 **安装方式**（已预装）
```powershell
# Linux/macOS 运行
openclaw run healthcheck --target=host --level=full

# Windows 环境（功能有限但可检查软件更新）
Get-HotFix | Where-Object {$_.HotFixID -like "KB*"} 
```

#### 📖 **使用示例**
> - "每周日晚上扫描一次服务器"  
> - "报告这台机器有哪些安全漏洞"  
> - "自动执行系统更新补丁（谨慎！）"  

#### 💰 **价值体现**
- 🔒 **风险预防**: 提前发现被忽视的安全隐患  
- 📅 **合规满足**: 审计/等保要求可追溯日志  
- ⏰ **省心事**: 设置定时任务无人值守运行  

---

### #5：**video-frames**（视频帧提取）

**一句话卖点：**  
> "从视频里精准抽一帧 GIF？30 秒搞定！"

#### ✨ **核心能力**
- 指定时间点截取帧（jpg/gif）
- 视频片段剪辑（5s/10s 短视频）
- 批量处理多段素材
- FFmpeg 封装，性能极佳

#### 🔧 **安装方式**
```powershell
# 检查 FFmpeg 是否已装
ffmpeg -version

# 没安装则下载（Windows）
Invoke-WebRequest -Uri "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip" -OutFile "ffmpeg.zip"
```

#### 📖 **使用示例**
> - "把第 2 分 15 秒的画面截成 GIF，时长 3 秒"  
> - "从这个 YouTube 视频里抽 10 帧关键画面拼图"  
> - "生成短视频片段（从 0:45 到 1:30）"  

#### 💰 **价值体现**
- 🎬 **内容创作**: 做教程/表情包超方便  
- ⚡ **效率提升**: FFmpeg 原生速度极快  
- 📱 **自媒体必备**: 一键生成短视频素材  

---

## 📋 安装方式总览（通用）

### **方法一：命令行自动安装**
```bash
# 从 clawhub.com 下载 community skills
openclaw skill install <skill_name>

# 或从 GitHub 克隆
git clone https://github.com/openclaw/openclaw-skills.git ~/.local/share/openclaw/skills/
```

### **方法二：手动安装**
```powershell
# Windows 目标路径
$destPath = "C:\Users\您的用户名\AppData\Roaming\npm\node_modules\openclaw\skills"

# 下载技能源码
New-Item -ItemType Directory -Force -Path "$destPath\<skill_name>"

# 验证 SKILL.md 存在
Test-Path "$destPath\<skill_name>\SKILL.md"
```

### **方法三：Feishu 扩展插件**
1. 在 GitHub 克隆扩展仓库  
2. 移动到 `.openclaw\extensions\feishu\skills\`  
3. 重启 OpenClaw Gateway  

```powershell
# Feishu skill 路径示例
$feishuSkillsPath = "C:\Users\您的用户名\.openclaw\extensions\feishu\skills"
Copy-Item ".\下载的技能文件夹\$feishuSkillsPath" -Recurse
```

### **安装后验证**
```bash
# 查看技能列表
openclaw skills list

# 查看特定 skill 详情  
openclaw skills show nano-pdf
```

---

## 🌟 每个场景推荐 Skills 组合

### 👨‍💻 **编程开发类任务**
```yaml
必备组合:
  - coding-agent      <-- 主力 AI 写代码
  + nano-pdf         <-- 阅读英文 PDF 技术文档
  + feishu-doc       <-- 保存项目笔记到飞书
```

### 🏢 **企业办公类任务**
```yaml
推荐配置:
  - feishu-doc       <-- 创建/编辑飞书文档
  - feishu-drive     <-- 云盘备份管理
  + healthcheck      <-- 定期服务器巡检
```

### 🎬 **内容创作类任务** 
```yaml
视频制作:
  - video-frames     <-- 精准截取画面
  + nano-pdf        <-- 提取 PDF 素材
  + weather         <-- 生成天气预报图表
```

### 🔐 **运维/安全类任务**
```yaml
服务器管理:
  - healthcheck      <-- 安全检查核心
  + coding-agent    <-- 写自动化部署脚本
```

---

## ⚠️ 注意事项 & 常见问题

### 🛑 **依赖问题**
- `nano-pdf` 需要安装独立 CLI 工具  
- `video-frames` 依赖 FFmpeg（Windows 需手动装）  
- `healthcheck` 部分功能仅 Linux/macOS 可用  

### 🔐 **权限问题**
Feishu Skills 需要先配置飞书企微账号权限：  
```yaml
1. 在飞书开放平台创建应用
2. 获取 app_id 和 secret
3. 写入环境变量:
   setx FEISHU_APP_ID "xxx"
   setx FEISHU_APP_SECRET "yyy"
4. 重启 Gateway
```

### 📦 **版本兼容性**
部分 Skill 可能依赖特定 OpenClaw 版本：  
- 当前环境：OpenClaw 2026.3.7  
- 如遇报错，尝试升级 core: `openclaw self-update`  

---

## 🔗 获取更多 Skills

### 🌐 **官方资源站**
- **技能市场**: https://clawhub.com（社区分享）  
- **官方文档**: https://docs.openclaw.ai/skills  
- **示例仓库**: https://github.com/openclaw/examples-skill  

### 📥 **安装第三方 community skills**
```bash
# 示例：安装 weather 扩展
openclaw skill install weather

# 或从 gitHub clone 到指定目录
cd ~/.local/share/openclaw/skills
git clone https://github.com/example/weather-skill.git
```

### 🛠️ **自己动手写 custom skill**
使用 `skill-creator` 技能引导创建：  
```markdown
1. 定义技能名称：my-custom-tool
2. 编写 SKILL.md（描述功能）
3. 添加实现脚本（Python/Node/Bash）
4. 测试验证 → 提交到 clawhub.com 分享！
```

---

## 📚 附录：Skill 文件结构说明

每个 skill 的标准目录树：  
```bash
skills/<skill_name>/
├── SKILL.md           # 👈 必须文件（功能描述 + 使用示例）
├── package.json       # （可选）Node 依赖声明
├── bin/              # CLI 工具脚本
│   └── tool.sh       # 实际执行的命令
├── templates/        # （可选）代码模板文件夹  
└── README.md         # （可选）补充说明文档
```

**关键点**: `SKILL.md` 是 AI 理解技能功能的唯一入口——必须详细！

---

## 💡 小结 & 建议

### ✅ **立即可用的 Skills**（今天就能玩）
1. **coding-agent** — 编程任务首选  
2. **nano-pdf** — 文档编辑神器  
3. **feishu-doc** — 飞书协作必备  

### 🚀 **进阶配置项**
4. **healthcheck** — 安全巡检专家（需 Linux）  
5. **video-frames** — 视频帧提取工具  

### 🔮 **未来可期**
- 持续关注 clawhub.com：每周都有新技能上线  
- 提交自己的 skill 到社区：帮助他人也能获得反馈！

---

## 📧 联系方式 / 问题反馈

如有安装问题或需要定制开发：  
- GitHub Issues: https://github.com/openclaw/openclaw/issues  
- Discord 社区：https://discord.gg/clawd  
- 国内交流群：见 README  

---

🎯 **一句话总结**：  
> Skills = OpenClaw 的插件市场。想干啥装就干啥，效率翻倍不是梦！

---
*本文档由 AI Assistant 整理编写，供 hongxing 参考使用。如有遗漏或错误请反馈修正。*