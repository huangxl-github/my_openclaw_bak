# 🔄 三省六部系统工作流详解

_本文档描述完整的旨意流转链路，供所有 Agent 参考遵循。_

---

## 📊 完整流程图（Mermaid）

```mermaid
sequenceDiagram
    participant 皇上 as 👑皇上<br/>(飞书/GUI)
    participant 太子 as 🎓太子<br/>分拣识别
    participant 中书 as 📜中书省<br/>任务规划
    participant 门下 as 🔍门下省<br/>审核封驳
    participant 尚书 as 📮尚书省<br/>派发汇总
    participant 六部 as ⚙️六部<br/>并行执行

    皇上->>太子：下旨/闲聊
    alt 是闲聊
        太子-->>皇上：直接回复（结束）
    else 是旨意
        太子->>中书：传旨（结构化数据）
        中书->>门下：提交规划方案
        loop 审核-修改循环
            rect rgb(250, 240, 230)
                Note right of 门下：🚫封驳否决权
            end
            alt 封驳
                门下-->>中书：驳回 + 修改意见
                中书->>门下：重新提交规划
            else 准奏
                门下->>尚书：准予通过 ✅
                break
            end
        end
        尚书->>六部：派发子任务
        Note right of 六部：💰户<br/>📝礼<br/>⚔️兵<br/>🔧工<br/>📋吏<br/>(并行执行)
        六部-->>尚书：分阶段交付物
        尚书->>尚书：汇总整合
        尚书-->皇上：回奏完整报告
    end
```

---

## 📝 每个环节的数据格式

### 1️⃣ **太子 → 中书** （旨意封装）

```yaml
edict:
  id: "ED20260310001"          # [自动生成] ED+日期 + 序号
  timestamp: "2026-03-10T20:00:00Z"
  
  intent: "简要意图（≤20 字）"   # 一句话概括核心需求
  summary: "详细描述（≤100 字）"
  
  raw_message: "皇上原始输入"
  
  metadata:
    source: "feishu|gui|telegram"
    channel_id: "om_xxxx"
    urgent: false              # [可选] true=加急
    
  status: {"stage":"taizi_done","next":"zhongshu"}
```

### 2️⃣ **中书 → 门下** （规划方案）

```yaml
plan:
  id: "PLAN-ED20260310001-001"
  edict_ref: "ED20260310001"
  
  overview: |
    [总体规划概述] 
    - 目标：...
    - 策略：...  
    - 预期产出：...
    
  phases:                        # 阶段划分
    - name: "阶段一：需求分析"
      objectives:
        - "理解业务逻辑"
        - "识别核心模块"  
      estimated_time: 30min
      
    - name: "阶段二：代码实现"
      ...

  tasks:                         # 具体任务清单
    - task_id: "T001"
      title: "阅读项目 README"
      description: "提取项目背景、技术栈、依赖关系"
      
      owner: "libu"              # 负责部门（吏部会校验）
      skill_requirement: ["file_read", "web_fetch"]
      
      dependencies: []           # [可选] 前置任务 ID 列表
      estimated_time: 15min
      
      acceptance_criteria: |     # ⚠️ 关键！可验证的标准
        - ✅ 输出技术栈清单（语言、框架、版本）
        - ✅ 识别核心模块路径
        - ✅ 无遗漏重要配置文件

    - "..."                     # ...更多任务
    
  resource_estimate:             # 资源评估
    total_time: "90min"         # 预计总耗时
    parallel_degree: 3          # 可并行度（同时执行数）
    
  risk_assessment:              # ⚠️ 关键！风险预警
    - type: "技术风险"
      description: "依赖版本可能过期"  
      mitigation: "提前检查 npm/yarn 兼容性"
      
    - ...

  status: {"version":1,"stage":"zhongshu_done","next":"menxia"}
```

### 3️⃣ **门下 → 尚书** （审核通过）或**封驳**

#### ✅ 准奏通过：

```yaml
review_approval:
  id: "REVIEW-PLAN20260310001"
  plan_ref: "PLAN-ED20260310001-001"
  
  decision: "APPROVED"          # ✅ APPROVED / 🚫 REJECTED
  
  score: {                      # [可选] 评分明细
    completeness: 95/100
    clarity: 90/100  
    feasibility: 85/100
    overall: 92
  }
  
  comments: |                   # 审核意见（准奏则简短）
    "方案清晰，风险可控，准予下发执行"
    
  signature: {
    reviewer: "menxia_agent_id"
    timestamp: "2026-03-10T20:10:00Z"
    duration: "2min 35s"        # 审核耗时  
  }
```

#### 🚫 **封驳驳回：**

```yaml
review_rejection:
  id: "REVIEW-PLAN20260310001-v1"
  plan_ref: "PLAN-ED20260310001-001"
  
  decision: "REJECTED"          # 🚫 REJECTED
  
  rejection_reasons:            # ⚠️ 必须列明！
    - severity: "CRITICAL"      # ⛔ CRITICAL / ⚠️ MAJOR / ℹ️ MINOR
      task_id: "T003"
      issue: |
        任务描述模糊："进行性能优化"
        
        ❌ 问题：
        1. 无明确量化指标（QPS？延迟？）
        2. 未定义验收标准
        
      required_action: |
        **必须修改**: 
        - 补充具体性能目标（如 P99 延迟 <50ms）  
        - 添加压力测试验证步骤
    
    - severity: "MAJOR"
      area: "risk_assessment"
      issue: "...遗漏..."

  modification_required: true   # 强制要求修改重交
  max_resubmit_remaining: 1     # =2 次则升级仲裁
  
  signature: {
    reviewer: "menxia_agent_id"  
    timestamp: "2026-03-10T20:08:00Z"
    duration: "4min 55s"
  }
```

### 4️⃣ **尚书 → 六部** （任务派发）

```yaml
dispatch_batch:
  id: "DISPATCH-ED20260310001"
  plan_ref: "PLAN-ED20260310001-001" (经门下审核版)
  
  tasks_by_department:          # 按部门分组的任务
  
    libu:                       # 户部收到的任务列表
      - task_id: "T001"
        ...（完整任务描述）...  
        
        dispatch_time: "2026-03-10T20:15:00Z"
        due_time: "2026-03-10T20:45:00Z"  # +estimated_time
        
      - task_id: "T004" 
        ...
        
    minbu:                       # 礼部...
    
# ...更多部门
  
  coordination_requirements:    # ⚠️ 跨部门协作说明
    
    - type: "SEQUENTIAL"         # 顺序依赖
      tasks: ["T001","T002"]     # T001必须先完成→T002才能启动
      reason: "T002需要T001的分析结果作为输入"
    
    - type: "PARALLEL_SAFE"      # 可并行执行的任务组
      tasks: ["T003","T004","T005"]
  
  monitor_config:               # 监控配置
    heartbeat_interval: 2min     # 每 2 分钟检查一次进度  
    timeout_alert_threshold: 80% # >80% 预估时间无进展则告警
```

---

## 📄 **回奏文档结构**（尚书汇总）

最终提交给皇上的完整报告包含：

```markdown
# 📜 【旨意回奏】ED20260310001

> 旨意内容："帮我分析这个项目..."

## ✅ 完成情况概览

| 指标 | 数值 |
|-:---|--:--:-----|  
| **任务总数** | 8 个
| **完成率** | 100% ✅
| **总耗时** | 95min (计划 90min，+5%)
| **交付物数量** | 6 份

## 📦 交付物清单

[每个部门的产出详细链接/路径]

## 🏆 质量自评

- [ ] 任务完成度：⭐⭐⭐⭐️⭐(5/5)  
- [ ] 文档质量：⭐⭐⭐⭐(4/5)
- [ ] 技术达标：⭐⭐⭐⭐⭐(5/5)

**尚书省执事签字**: [Agent ID]  
**回奏时间**: 2026-03-10 21:35

---

👉 **请皇上审阅，如有进一步指示另行下旨！** 🙇
```

---

## 🎯 状态流转机

```mermaid
stateDiagram-v2
    [*] --> TAIZI_ANALYZING
    
    TAIZI_ANALYZING --> CHUAN_ZHI: 是旨意
    TAIZI_ANALYZING --> DIRECT_REPLY: 是闲聊 → [*]
    
    CHUAN_ZHI --> ZHONGSHU_PLANNING
    
    ZHONGSHU_PLANNING --> MENXIA_REVIEW
    
    state MenxiaReviewState <<choice>>
    MENXIA_REVIEW --> MenxiaReviewState
    MenxiaReviewState --> ZHONGSHU_PLANNING: 封驳 → Retry ≤2
    MenxiaReviewState --> SHANGSHU_DISPATCH: 准奏 ✅
    
    SHANGSHU_DISPATCH --> LIUBU_EXECUTING
    
    state SixBureauExecuting <<parallel>>
    LIUBU_EXECUTING --> SixBureauExecuting
    SixBureauExecuting --> SHANGSHU_COLLECT: all done
    
    SHANGSHU_COLLECT --> HUIZOU_TO_EMPEROR --> [*]
```

---

## 🔧 实现建议

1. **使用文件存储中间状态**：
   - `workspace/edict-system/tracks/ED20260310001/`
   - 每个环节输出标准 JSON/YAML
  
2. **Agent 间通信**：
   - Via file-watch + 回调（推荐）  
   - 或 sessions_send（更实时的方案）

3. **进度追踪**：
   - 维护全局状态表 `workspace/status.md`
   - 定期刷新（每分钟 scan 一次各 Agent workspace）

---

*工作流文档版本：v1.0 · Last Updated: 2026-03-10*
