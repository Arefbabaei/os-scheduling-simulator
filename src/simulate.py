import csv
import argparse
from pathlib import Path
from algorithms import Process, fcfs, sjf_nonpreemptive, priority_nonpreemptive, round_robin
from metrics import compute_metrics, gantt_text

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

def load_processes(csv_path: Path):
    procs = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            procs.append(Process(
                pid=row["pid"],
                arrival=int(row["arrival"]),
                burst=int(row["burst"]),
                priority=int(row["priority"]),
            ))
    return procs

def main():
    parser = argparse.ArgumentParser(description="OS Scheduling Simulator")
    parser.add_argument("--data", default=str(DATA / "sample_processes.csv"))
    parser.add_argument("--algo", choices=["fcfs","sjf","priority","rr"], default="fcfs")
    parser.add_argument("--quantum", type=int, default=2)
    args = parser.parse_args()

    procs = load_processes(Path(args.data))

    if args.algo == "fcfs":
        timeline = fcfs(procs)
    elif args.algo == "sjf":
        timeline = sjf_nonpreemptive(procs)
    elif args.algo == "priority":
        timeline = priority_nonpreemptive(procs)
    else:
        timeline = round_robin(procs, quantum=args.quantum)

    print("Gantt:", gantt_text(timeline))
    print("Metrics:", compute_metrics(procs, timeline))

if __name__ == "__main__":
    main()
