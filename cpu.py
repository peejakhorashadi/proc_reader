class CPUReading:
    def __init__(self,usr,sys,idle):
        self.user_time = usr
        self.sys_time = sys
        self.idle_time = idle

    def printCPU(self):
        print(f"time in user mode: {self.user_time/100} seconds\ntime in sys mode: {self.sys_time/100} seconds\ntime in idle mode: {self.idle_time/100} seconds.")