class CPUReading:
    def __init__(self, cpu_total={"user": 0, "sys" : 0, "idle" : 0}, cpu0={"user": 0, "sys" : 0, "idle" : 0}, cpu1={"user": 0, "sys" : 0, "idle" : 0}, cpu2={"user": 0, "sys" : 0, "idle" :  0}, cpu3={"user":  0, "sys" :  0, "idle" : 0}, num_interrupts = 0, num_context_switches = 0):
        self.cpu_total = cpu_total
        self.cpu0 = cpu0
        self.cpu1 = cpu1
        self.cpu2 = cpu2
        self.cpu3 = cpu3
        self.num_interrupts = num_interrupts
        self.num_context_switches = num_context_switches

    def print(self):
        print(self.cpu_total)
        print(self.cpu0)
        print(self.cpu1)
        print(self.cpu2)
        print(self.cpu3)
        print(self.num_interrupts)
        print(self.num_context_switches)
