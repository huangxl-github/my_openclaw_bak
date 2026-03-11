"""📝 ToDo List CLI - 三省六部系统交付 #2"""
import click, json, os
from colorama import Fore, Style, init
from datetime import datetime as dt

init(autoreset=True)
DATA = "~/.todo.json"

def load():
    path = os.path.expanduser(DATA)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except: return []

def save(tasks):
    path = os.path.expanduser(DATA)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2, default=str)

@click.group()
def cli(): """主入口"""
    pass

@cli.command()
@click.argument('description')
@click.option('--priority', '-p', type=click.Choice(['high','medium','low']), default='medium')
@click.option('--due', '-d', type=click.DateTime(formats=['%Y-%m-%d']))
def add(description, priority, due):
    """添加任务"""
    tasks = load()
    task_id = len(tasks)+1
    new_task = {
        'id': task_id,'desc':description,'pry':priority,'due':dt.strftime(due,'%Y-%m-%d') if due else '-',
        'status':'pending','created':dt.now().strftime('%Y-%m-%d %H:%M')}
    tasks.append(new_task); save(tasks)
    emoji = {'high':'🔴','medium':'🟡','low':'🟢'}
    click.echo(f"{Fore.GREEN}✅ {Style.BRIGHT}任务 #{task_id} 已添加:{description}{Style.RESET_ALL}")
    click.echo(f"   {emoji.get(priority,'⚪')}优先级:{priority.upper()} | ⏰截止:{new_task['due']}")

@cli.command()
@click.option('--status', '-s', type=click.Choice(['pending','done','all']), default='all')
def list_tasks(status):
    """列出任务"""
    tasks = load()
    if not tasks: click.echo(f"{Fore.YELLOW}📭暂无待办事项{Style.RESET_ALL}"); return
    
    click.echo(f"\n{Fore.CYAN}{'ID':<5}{'优先级':<10}{'状态':<12}{'任务':<35}{'截止':<12}{Style.RESET_ALL}")
    click.echo("-"*75)
    for t in tasks:
        if status!='all' and t['status']!=status: continue
        pmap={'HIGH':'🔴','MEDIUM':'🟡','LOW':'🟢'}
        s=t['status']; st=Fore.GREEN+'✅已完成'+Style.RESET_ALL if s=='done' else Fore.YELLOW+'⏳待办'+Style.RESET_ALL
        click.echo(f"{t['id']:<5}{pmap.get(t['pry'],'⚪')}{t['pry']:<8} {st:<12} {Style.BRIGHT}{t['desc']}:{Style.RESET_ALL:<30} {t['due']}")
    
    pending=len([x for x in tasks if x['status']=='pending'])
    click.echo(f"\n{Fore.CYAN}📊总计:{len(tasks)} | ⏳待办:{pending} | ✅已完成:{len(tasks)-pending}{Style.RESET_ALL}")

@cli.command()
@click.argument('task_id', type=int)
def done(task_id):
    """标记完成"""
    tasks = load()
    t=next((x for x in tasks if x['id']==task_id),None)
    if not t: click.echo(f"{Fore.RED}❌任务#{task_id}不存在{Style.RESET_ALL}"); return
    t['status']='done'; t['completed']=dt.now().strftime('%Y-%m-%d %H:%M'); save(tasks)
    click.echo(f"{Fore.GREEN}✅任务 #{task_id} 已完成:{t['desc']}{Style.RESET_ALL}")

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """删除任务"""
    tasks = load()
    t=next((x for x in tasks if x['id']==task_id),None)
    if not t: click.echo(f"{Fore.RED}❌任务#{task_id}不存在{Style.RESET_ALL}"); return
    tasks.remove(t); save(tasks)
    click.echo(f"{Fore.YELLOW}🗑️ 任务 #{task_id} 已删除:{t['desc']}{Style.RESET_ALL}")

@cli.command()
def summary(): """统计摘要"""
    from rich.console,table import Console,Table; c=Console()
    tasks = load(); pending=[x for x in tasks if x['status']=='pending']; done_t=[x for x in tasks if x['status']=='done']
    if not tasks: click.echo("📭暂无任务"); return
    
    rate=round(len(done_t)/len(tasks)*100,1) if tasks else 0
    bar="█"*int(rate/5)+"░"*(20-int(rate/5))
    
    c.print(f"[bold cyan]{'='*60}[/]")
    c.print(f"[cyan]📊任务概览 (数据时间:{dt.now().strftime('%Y-%m-%d %H:%M')})")
    c.print(f"{'总任务数:':<20} [white bold]{len(tasks)}[/)")
    c.print(f"{'待办数量:':<20} [yellow]{pending} len([/])")
    c.print(f"{'已完成:':<20} [green]{len(done_t)}[/)"]
    c.print(f"[bold]📈完成度:[/] [{bar}] [magenta]{rate}%[/]")

if __name__=='__main__': cli()
