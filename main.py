import os, sys, time, cpu

PROC_FILEPATH = "/proc/stat"
INTERVAL_TIME = 2

# def get_interval(reading1:cpu.CPUReading, reading2:cpu.CPUReading):
#     delta_user = reading1.user_time - reading2.user_time
#     delta_sys = reading1.sys_time - reading2.sys_time
#     delta_idle = reading1.idle_time - reading2.idle_time
#     return (delta_user + delta_sys + delta_idle)




with open(PROC_FILEPATH, "r", encoding='UTF-8') as proc_file:
    for line in proc_file:
        if(line.startswith("cpu")):
            print(line)

    # prev = cpu.CPUReading(line[0],int(line[1]),int(line[3]), int(line[4]))
    # curr = prev
    # prev.printCPU()
    # print("\n")
    
    # for _ in range(3):
    #     time.sleep(INTERVAL_TIME)
    #     proc_file.seek(0)
    #     prev = curr
    #     line = proc_file.readline().split()
    #     curr = cpu.CPUReading(line[0],int(line[1]),int(line[3]), int(line[4]))
    #     print(line)
    #     print(get_interval(curr,prev)/100)
    #     print('\n')

