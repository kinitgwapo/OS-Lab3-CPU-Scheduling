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