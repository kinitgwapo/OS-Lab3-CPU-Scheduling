# RATE MONOTONIC SCHEDULING (RMS)
# Preemptive fixed-priority scheduling

tasks = [
    {"id": "T1", "C": 1, "T": 4, "D": 4},
    {"id": "T2", "C": 1, "T": 5, "D": 5},
    {"id": "T3", "C": 2, "T": 10, "D": 10},
]

SIMULATION_TIME = 20

def key(x):
    return (x["T"], x["id"])

def get_priority(j):
    period = None

    for t in tasks:
        if t["id"] == j["id"]:
            period = t["T"]
            break

    return (period, j["release"], j["id"])

tasks.sort(key=key)

jobs = []
gantt = []

# -------------------- Logic & Functions -------------------- #
def add_segment(pid, start, end):
    # Update previous process status
    if (gantt) and (gantt[-1][0] == pid) and (gantt[-1][2] == start):
        gantt[-1] = (pid, gantt[-1][1], end)

    # Add new process status
    else:
        gantt.append((pid, start, end))

def task_create_release():
    for task in tasks:
        release = 0
        while (release < SIMULATION_TIME):
            jobs.append({
                "id": task["id"],
                "release": release,
                "deadline": release + task["D"],
                "remaining": task["C"],
                "completion": None
            })

            release += task["T"]

def cpu_time_simulation():
    for time in range(SIMULATION_TIME):
        ready = []

        for job in jobs:
            if(job["release"] <= time) and (job["remaining"] > 0) and (job["deadline"] > time):
                ready.append(job)

        if ready:
            running = min(ready, key=get_priority)
            add_segment(running["id"], time, time + 1)
            running["remaining"] -= 1

            if (running["remaining"] == 0):
                running["completion"] = time + 1
        else:
            add_segment("IDLE", time, time + 1)

def task_deadline_status():
    for job in jobs:
        if(job["completion"] is not None) and (job["completion"] <= job["deadline"]):
            job["status"] = "MET"
        elif job["deadline"] <= SIMULATION_TIME:
            job["status"] = "MISSED"
        else:
            job["status"] = "PENDING"

def calculate_utilization(tasks):
    utilization = 0
    for task in tasks:
        utilization += task["C"] / task["T"]

    return utilization

def calculate_rms_bound(n):
    return n * (2 ** (1 / n) - 1)

def format_percentage(value):
    return round(value * 100, 2)

def check_rms_bound(utilization, bound):
    if (utilization <= bound):
        return "PASS\n"

    return "NOT PASSED\n"

# -------------------- Logic & Functions -------------------- #

task_create_release()
cpu_time_simulation()
task_deadline_status()

utilization = calculate_utilization(tasks)
n = len(tasks)
bound = calculate_rms_bound(n)
misses = 0

print(
    "RATE MONOTONIC SCHEDULING\n"
    "Priority Order:", ">" .join(t["id"] for t in tasks), "\n"
    "CPU Utilization:", format_percentage(utilization), "%\n"
    "RMS Sufficient Utilization Bound:", format_percentage(bound), "%\n"
    "Sufficient-Bound Test:", check_rms_bound(utilization, bound)
)

print("GANTT CHART")
for pid, start, end in gantt:
    print(f"| {pid} [{start}-{end}] ", end="")
print("|\n")

print("TASK INSTANCE RESULTS")
print(
    f'{"Task":<10}'
    f'{"Release":<12}'
    f'{"Deadline":<12}'
    f'{"Completion":<14}'
    f'{"Status":<10}'
)

for job in sorted(jobs, key=get_priority):
    if job["status"] == "MISSED":
        misses += 1
    
    completion = job["completion"] if job["completion"] is not None else "-"
    print(
        f'{job["id"]:<10}'
        f'{job["release"]:<12}'
        f'{job["deadline"]:<12}'
        f'{completion:<14}'
        f'{job["status"]:<10}'
    )

print("Deadline Misses:", misses)