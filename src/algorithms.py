from dataclasses import dataclass
from typing import List, Dict, Tuple
from collections import deque

@dataclass
class Process:
    pid: str
    arrival: int
    burst: int
    priority: int

@dataclass
class Slice:
    pid: str
    start: int
    end: int

def fcfs(procs: List[Process]) -> List[Slice]:
    procs = sorted(procs, key=lambda p: (p.arrival, p.pid))
    t = 0
    timeline: List[Slice] = []
    for p in procs:
        if t < p.arrival:
            t = p.arrival
        start = t
        t += p.burst
        timeline.append(Slice(p.pid, start, t))
    return timeline

def sjf_nonpreemptive(procs: List[Process]) -> List[Slice]:
    remaining = sorted(procs, key=lambda p: (p.arrival, p.pid))
    t = 0
    timeline: List[Slice] = []
    ready: List[Process] = []

    while remaining or ready:
        while remaining and remaining[0].arrival <= t:
            ready.append(remaining.pop(0))
        if not ready:
            t = remaining[0].arrival
            continue
        ready.sort(key=lambda p: (p.burst, p.arrival, p.pid))
        p = ready.pop(0)
        start = t
        t += p.burst
        timeline.append(Slice(p.pid, start, t))
    return timeline

def priority_nonpreemptive(procs: List[Process]) -> List[Slice]:
    remaining = sorted(procs, key=lambda p: (p.arrival, p.pid))
    t = 0
    timeline: List[Slice] = []
    ready: List[Process] = []

    while remaining or ready:
        while remaining and remaining[0].arrival <= t:
            ready.append(remaining.pop(0))
        if not ready:
            t = remaining[0].arrival
            continue
        ready.sort(key=lambda p: (p.priority, p.arrival, p.pid))  # lower = higher priority
        p = ready.pop(0)
        start = t
        t += p.burst
        timeline.append(Slice(p.pid, start, t))
    return timeline

def round_robin(procs: List[Process], quantum: int) -> List[Slice]:
    t = 0
    timeline: List[Slice] = []

    procs = sorted(procs, key=lambda p: (p.arrival, p.pid))
    remaining = {p.pid: p.burst for p in procs}

    q = deque()
    i = 0
    n = len(procs)

    while q or i < n:
        # add arrived processes
        while i < n and procs[i].arrival <= t:
            q.append(procs[i].pid)
            i += 1

        if not q:
            t = procs[i].arrival
            continue

        pid = q.popleft()
        p = next(p for p in procs if p.pid == pid)

        start = t
        run = min(quantum, remaining[pid])
        t += run
        remaining[pid] -= run

        timeline.append(Slice(pid, start, t))

        # add newly arrived during execution
        while i < n and procs[i].arrival <= t:
            q.append(procs[i].pid)
            i += 1

        if remaining[pid] > 0:
            q.append(pid)

    return timeline

    def enqueue_arrivals(up_to_time: int):
        nonlocal i
        while i < len(procs_sorted) and procs_sorted[i].arrival <= up_to_time:
            q.append(procs_sorted[i].pid)
            i += 1

    if procs_sorted:
        t = procs_sorted[0].arrival
        enqueue_arrivals(t)

    while q or i < len(procs_sorted):
        if not q:
            t = procs_sorted[i].arrival
            enqueue_arrivals(t)

        pid = q.popleft()
        run = min(quantum, remaining_burst[pid])
        start = t
        t += run
        remaining_burst[pid] -= run
        timeline.append(Slice(pid, start, t))

        enqueue_arrivals(t)

        if remaining_burst[pid] > 0:
            q.append(pid)

