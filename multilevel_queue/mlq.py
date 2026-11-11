from collections import deque

# MULTILEVEL QUEUE SCHEDULING
# Queue 1: Round Roben; Queue 2: FCFS

processes = [
    {"pid": "P1", "arrival": "0", "burst": "5", "queue": "1", "remaining": 5, "completion": None},
    {"pid": "P2", "arrival": "1", "burst": "4", "queue": "1", "remaining": 4, "completion": None},
    {"pid": "P3", "arrival": "0", "burst": "6", "queue": "2", "remaining": 6, "completion": None},
    {"pid": "P4", "arrival": "2", "burst": "3", "queue": "2", "remaining": 3, "completion": None},
    {"pid": "P5", "arrival": "3", "burst": "2", "queue": "1", "remaining": 2, "completion": None}
]

QUANTUM = 2

def key(p):
    return (p["arrival"], p["pid"])

processes.sort(key=key)

q1 = deque()
q2 = deque()
current_q1 = None
current_q2 = None
quantum_left = 0
time = 0
index = 0
gantt = []
total_tat = 0
total_wt = 0

print(
    "MULTILEVEL QUEUE SCHEDULING\n"
    "Queue 1: Round Robin (Quantum = 2ms)\n"
    "Queue 2: FCFS\n"
    "\nGANTT CHART\n"
)

print(
    "PROCESS PERFORMANCE"
    "PID\\tAT\\tBT\\tCT\\tTAT\\tWT"
)

n = len(processes)
print(
    "Average Turnaround Time:",
    round(total_tat / n, 2),
    "ms"
    "\n"
    "Average Waiting Time:",
    round(total_wt / n, 2),
    "ms"
)

# -------------------- Logic & Functions -------------------- #
def add_segment(pid, start, end):
    # Update previous process status
    if (gantt) and (gantt[-1][0] == pid) and (gantt[-1][2] == start):
        gantt[-1] = (pid, gantt[-1][1], end)

    # Add new process status
    else:
        gantt.append((pid, start, end))

while True:
    unfinished = False
    for p in processes:
        if p["remaining"] > 0:
            unfinished = True
            break
    if not unfinished:
        break


# -------------------- Logic & Functions -------------------- #