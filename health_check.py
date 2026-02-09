import psutil
import shutil

def check_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free_space=du.free/du.total*100
    return free_space>20

def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    return usage <75

if not check_disk_usage("/") or not check_cpu_usage():
    print("Error,Check disk or cpu ")
else:
    print("Everything is working properly!")