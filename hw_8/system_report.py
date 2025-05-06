import subprocess
from datetime import datetime
from collections import defaultdict

def get_ps_aux_output():
    result = subprocess.run(['ps', 'aux'], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip().split('\n')

def parse_ps_output(ps_lines):
    headers = ps_lines[0].split()
    lines = ps_lines[1:]
    total_memory = 0.0
    total_cpu = 0.0
    user_processes = defaultdict(int)
    processes = []
    for line in lines:
        parts = line.split(None, len(headers) - 1)
        if len(parts) < len(headers):
            continue

        user = parts[0]
        cpu = float(parts[2])
        mem = float(parts[3])
        command = parts[10] if len(parts) > 10 else ''

        user_processes[user] += 1
        total_cpu += cpu
        total_memory += mem
        processes.append({
            'user': user,
            'cpu': cpu,
            'mem': mem,
            'command': command
        })
    return user_processes, len(lines), total_memory, total_cpu, processes

def generate_report():
    ps_lines = get_ps_aux_output()
    users_dict, total_proc, mem_sum, cpu_sum, processes = parse_ps_output(ps_lines)
    top_mem_proc = max(processes, key=lambda p: p['mem'], default={'command': ''})
    top_cpu_proc = max(processes, key=lambda p: p['cpu'], default={'command': ''})
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    report_filename = f'report_{now}.txt'

    report_lines = []
    report_lines.append("Отчёт о состоянии системы:")
    report_lines.append("Пользователи системы: " + ', '.join(f"'{u}'" for u in sorted(users_dict.keys())))
    report_lines.append(f"Процессов запущено: {total_proc}")
    report_lines.append("Пользовательских процессов:")
    for user, count in sorted(users_dict.items()):
        report_lines.append(f"{user}: {count}")
    report_lines.append(f"Всего памяти используется: {mem_sum:.1f} mb")
    report_lines.append(f"Всего CPU используется: {cpu_sum:.1f}%")

    mem_name = top_mem_proc['command'][:20]
    cpu_name = top_cpu_proc['command'][:20]
    report_lines.append(f"Больше всего памяти использует: ({mem_name})")
    report_lines.append(f"Больше всего CPU использует: ({cpu_name})")

    report = '\n'.join(report_lines)
    print(report)

    with open(report_filename, 'w') as f:
        f.write(report)

    print(f"\nОтчёт сохранён в файл: {report_filename}")

if __name__ == "__main__":
    generate_report()
    