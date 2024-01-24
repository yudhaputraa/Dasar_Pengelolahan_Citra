import psutil
import time
import gpustat

# Monitoring CPU Usage
# while True:
#     cpu_percent = psutil.cpu_percent(interval=1)
#     print(f"CPU Usage: {cpu_percent}%")
#     time.sleep(1)

# Monitoring Memory Usage
# while True:
#     memory_usage = psutil.virtual_memory()
#     print(f"Memory Usage: {memory_usage.percent}%")
#     time.sleep(1)

## Get GPU statistics
gpu_stats = gpustat.GPUStatCollection.new_query()

## Print GPU information
for gpu in gpu_stats.gpus:
    print(f"GPU {gpu.index}: {gpu.name}, Utilization: {gpu.utilization}%")