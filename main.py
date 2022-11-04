
import os, sys
import cpu
import time

filepath = "/proc/stat"

def get_interval(reading1:cpu.CPUReading, reading2:cpu.CPUReading):
    delta_user = reading1.user_time - reading2.user_time
    delta_sys = reading1.sys_time - reading2.sys_time
    delta_idle = reading1.idle_time - reading2.idle_time
    return (delta_user + delta_sys + delta_idle)




open(filepath, "r") as file:
    line = file.readline().split()
    prev = cpu.CPUReading(int(line[1]),int(line[3]), int(line[4]))
    curr = prev
    prev.printCPU()
    print("\n")
    
    for _ in range(3):
        time.sleep(2)
        file.seek(0)
        prev = curr
        line = file.readline().split()
        curr = cpu.CPUReading(int(line[1]),int(line[3]), int(line[4]))
        print(get_interval(curr,prev)/100)
        print('\n')

