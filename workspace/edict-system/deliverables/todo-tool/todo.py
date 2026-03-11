#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📝 TodoList CLI - 命令行待办事项管理工具
三省六部制系统交付物 #1
"""

import json, sys, os
from datetime import datetime, date
from pathlib import Path

DATA_FILE = Path.home() / ".todolist.json"

def load():
    """加载数据"""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save(tasks):
    """保存数据"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
    print("✅ 已保存到磁盘")

def add_task(description, priority="medium", due_date=None):
    """添加任务"""
    tasks = load()
    task_id = len(tasks) + 1
    
    new_task = {
        "id": task_id,
        "description": description,
        "priority": priority.upper(),
        "due_date": due_date or None,
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    
    tasks.append(new_task)
    save(tasks)
    print(f"✅ 任务 #{task_id} 已添加：{description}")
    if priority: print(f"   🚨 优先级：{priority.upper()}")
    if due_date: print(f"   ⏰ 截止：{due_date}")

def list_tasks(status="all", priority=None):
    """列出任务"""
    tasks = load()
    
    if not tasks:
        print("📭 暂无待办事项")
        return
    
    print("\n📋" + "="*60)
    print(f"{'ID':<5} {'优先级':<10} {'状态':<12} {'任务':<30} {'截止':<12}")
    print("-"*60)
    
    for task in tasks:
        if status != "all" and task["status"] != status:
            continue
        if priority and task["priority"] != priority.upper():
            continue
        
        # 图标映射
        p_map = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}
        s_map = {"pending": "⏳待办", "done": "✅已完成"}
        
        p_icon = p_map.get(task["priority"], "⚪")
        s_status = s_map.get(task["status"], task["status"])
        due = task.get("due_date") or "-"
        
        print(f"{task['id']:<5} {p_icon}{task['priority']:<8} {s_status:<12} "
              f"{task['description'][:28]:<30} {due:<12}")
    
    print("="*60 + "\n")
    
    # 统计摘要
    pending = len([t for t in tasks if t["status"] == "pending"])
    done = len([t for t in tasks if t["status"] == "done"])
    print(f"📊 总计：{len(tasks)} | ⏳待办：{pending} | ✅已完成：{done}\n")

def mark_done(task_id):
    """标记任务完成"""
    tasks = load()
    
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"❌ 任务 #{task_id} 不存在")
        return
    
    if task["status"] == "done":
        print(f"⚠️ 任务 #{task_id} 已完成")
        return
    
    task["status"] = "done"
    task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    save(tasks)
    print(f"✅ 任务 #{task_id} 已标记为完成：{task['description']}")

def delete_task(task_id):
    """删除任务"""
    tasks = load()
    
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        print(f"❌ 任务 #{task_id} 不存在")
        return
    
    tasks.pop(tasks.index(task))
    save(tasks)
    print(f"🗑️ 任务 #{task_id} 已删除：{task['description']}")

def summary():
    """显示统计摘要"""
    tasks = load()
    
    if not tasks:
        print("📭 暂无待办事项\n")
        return
    
    pending = [t for t in tasks if t["status"] == "pending"]
    done = [t for t in tasks if t["status"] == "done"]
    high_priority = [t for t in pending if t["priority"] == "HIGH"]
    
    print("\n📊" + "="*50)
    print(f"{'总任务数:':<20} {len(tasks)}")
    print(f"{'待办数量:':<20} {len(pending)}")
    print(f"{'已完成:':<20} {len(done)}")
    print(f"{'高优先级待办:':<20} {len(high_priority)}")
    
    if pending:
        completion_rate = round(len(done) / len(tasks) * 100, 1)
        # 进度条可视化
        progress_bar = "█" * int(completion_rate/5) + "░" * (20 - int(completion_rate/5))
        print(f"\n📈 完成度：[{progress_bar}] {completion_rate}%")
    
    if high_priority:
        print("\n⚠️ 高优先级待办:")
        for t in high_priority:
            print(f"   🔴 #{t['id']} {t['description']}")
    
    print("="*50 + "\n")

def main():
    """主命令行入口"""
    if len(sys.argv) < 2:
        print("\n📝 TodoList CLI - 三省六部制系统交付物 #1\n")
        print("用法：todo.py <命令> [选项]\n")
        print("命令:")
        print("  add <描述>      --priority <high|medium|low>  --due <YYYY-MM-DD>")
        print("  list            [--status <pending|done>]     [--priority <level>]")
        print("  done <ID>")
        print("  delete <ID>")
        print("  summary")
        print("\n示例:\n")
        print("  todo.py add \"写周报\" --priority high --due 2026-03-15")
        print("  todo.py list --status pending")
        print("  todo.py done 1")
        return
    
    cmd = sys.argv[1].lower()
    
    if cmd == "add":
        if len(sys.argv) < 3:
            print("❌ 用法：todo.py add <任务描述>")
            return
        
        # 解析参数
        args = sys.argv[3:4]
        
        description = sys.argv[2]
        priority = "medium"
        due = None
        
        i = 4
        while i < len(sys.argv):
            if sys.argv[i] == "--priority" and i+1 < len(sys.argv):
                priority = sys.argv[i+1].lower()
                i += 2
            elif sys.argv[i] == "--due" and i+1 < len(sys.argv):
                due = sys.argv[i+1]
                i += 2
            else:
                i += 1
        
        add_task(description, priority, due)
    
    elif cmd == "list":
        status = "all"
        priority = None
        
        for i, arg in enumerate(sys.argv[2:]):
            if arg == "--status" and i+1 < len(sys.argv[2:]):
                status = sys.argv[i+3]
            elif arg == "--priority" and i+1 < len(sys.argv[2:]):
                priority = sys.argv[i+3]
        
        list_tasks(status, priority)
    
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("❌ 用法：todo.py done <任务ID>")
            return
        
        try:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        except ValueError:
            print("❌ 任务 ID 必须是数字")
    
    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("❌ 用法：todo.py delete <任务ID>")
            return
        
        try:
            task_id = int(sys.argv[2])
            delete_task(task_id)
        except ValueError:
            print("❌ 任务 ID 必须是数字")
    
    elif cmd == "summary":
        summary()
    
    else:
        print(f"❌ 未知命令：{cmd}")
        print("运行 ./todo.py 查看帮助")

if __name__ == "__main__":
    main()
