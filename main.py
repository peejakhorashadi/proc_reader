# import os
# import sys
import time
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation


from cpu import CPUReading


PROC_FILEPATH = "/proc/stat"
INTERVAL_TIME = 1

def get_interval(reading1:CPUReading, reading2:CPUReading):
    delta_user = reading2.cpu_total["user"] - reading1.cpu_total["user"]
    delta_sys = reading2.cpu_total["sys"] - reading1.cpu_total["sys"]
    delta_idle = reading2.cpu_total["idle"] - reading1.cpu_total["idle"]
    return (delta_user + delta_sys + delta_idle)/100

def get_cpu_stats(x:CPUReading, y:CPUReading, interval:float):
    cpu_diff = {
        "user": 0,
        "sys": 0,
        "idle": 0
    }
    cpu_diff["user"] = (y["user"]- x["user"])/interval
    cpu_diff["sys"] = (y["sys"]- x["sys"])/interval
    cpu_diff["idle"] = (y["idle"]- x["idle"])/interval
    return cpu_diff

def get_util_stats(reading1:CPUReading, reading2:CPUReading, interval:float):

    """returns a list of dictionaries with keys:[user,sys,idle]
    each index of list represents cpu utilization of [total,cpu0,cpu1,cpu2,cpu3]"""

    cpu_util_array = []
    cpu_util_array.append(get_cpu_stats(reading1.cpu_total, reading2.cpu_total, interval))
    cpu_util_array.append(get_cpu_stats(reading1.cpu0, reading2.cpu0, interval))
    cpu_util_array.append(get_cpu_stats(reading1.cpu1, reading2.cpu1, interval))
    cpu_util_array.append(get_cpu_stats(reading1.cpu2, reading2.cpu2, interval))
    cpu_util_array.append(get_cpu_stats(reading1.cpu3, reading2.cpu3, interval))
    cpu_util_array.append((reading2.num_interrupts- reading1.num_interrupts)/interval)
    cpu_util_array.append((reading2.num_context_switches- reading1.num_context_switches)/interval)
    # cpu_util_array --> array with [cpu_total,cpu0,cpu1,cpu2,cpu3,interrupts,context switches]
    return cpu_util_array


def get_proc_stat_data(filename):
    proc_file.seek(0)
    cpu_array = []
    num_intr = 0
    num_context_switches = 0
    for line in filename:
        if(line.startswith("cpu")):
            split_line = line.split()
            cpu_array.append ({
                "user": int(split_line[1]),
                "sys" : int(split_line[3]),
                "idle" : int(split_line[4])})
        if (line.startswith("intr")):
            split_line = line.split()
            num_intr = int(split_line[1])
        if(line.startswith("ctxt")):
            split_line = line.split()
            num_context_switches = int(split_line[1])


    return CPUReading(cpu_array[0],cpu_array[1],cpu_array[2], cpu_array[3], cpu_array[4], num_intr, num_context_switches)


with open(PROC_FILEPATH, "r", encoding='UTF-8') as proc_file:
    #initial cpu reading
    prev = get_proc_stat_data(proc_file)
    curr = prev
    #cpu_utilization --> [total, cpu0, cpu1, cpu2, cpu3]
    cpu_util = []
    inter= 0
    for _ in range(3):
        time.sleep(INTERVAL_TIME)
        prev = curr
        curr = get_proc_stat_data(proc_file)
        inter = get_interval(prev,curr)
        cpu_stats_array = get_util_stats(prev,curr, inter)
        print(f"cpu stats are: {cpu_stats_array[0:5]}")
        print(f"number of interupts:{cpu_stats_array[5]}")
        print(f"number of context switches {cpu_stats_array[6]}")
        



