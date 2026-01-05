# cat > README.md << 'EOF'
# OS Scheduling Simulator

A lightweight scheduling simulator implementing classic CPU scheduling algorithms:
- FCFS
- SJF (non-preemptive)
- Priority (non-preemptive)
- Round Robin

## Run

```bash
python3 src/simulate.py --algo fcfs
python3 src/simulate.py --algo sjf
python3 src/simulate.py --algo priority
python3 src/simulate.py --algo rr --quantum 2os-scheduling-simulator