from typing import Dict, List
from algorithms import Process, Slice

def compute_metrics(procs: List[Process], timeline: List[Slice]) -> Dict[str, float]:
    arrival = {p.pid: p.arrival for p in procs}
    burst = {p.pid: p.burst for p in procs}

    first_start: Dict[str, int] = {}
    completion: Dict[str, int] = {}

    for sl in timeline:
        if sl.pid not in first_start:
            first_start[sl.pid] = sl.start
        completion[sl.pid] = sl.end

    waiting = {}
    turnaround = {}
    response = {}

    for pid in arrival:
        turnaround[pid] = completion[pid] - arrival[pid]
        waiting[pid] = turnaround[pid] - burst[pid]
        response[pid] = first_start[pid] - arrival[pid]

    n = len(procs)
    return {
        "avg_waiting": round(sum(waiting.values()) / n, 2),
        "avg_turnaround": round(sum(turnaround.values()) / n, 2),
        "avg_response": round(sum(response.values()) / n, 2),
    }

def gantt_text(timeline: List[Slice]) -> str:
    parts = []
    for sl in timeline:
        parts.append(f"[{sl.start}-{sl.end}:{sl.pid}]")
    return " ".join(parts)
