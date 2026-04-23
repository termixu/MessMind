import subprocess
import time

ports = [5000, 5001, 5002]
processes = []

for i, port in enumerate(ports):
    proc = subprocess.Popen([
        "python", "messmind/main.py",
        "--node_id", str(i),
        "--port", str(port),
        "--config", "config/nodes.yaml"
    ])
    processes.append(proc)
    time.sleep(2)

# Ждать Ctrl+C
try:
    for p in processes:
        p.wait()
except KeyboardInterrupt:
    for p in processes:
        p.terminate()
