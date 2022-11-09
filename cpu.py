class CPUReading:
    def __init__(self,cpu_total, cpu0, cpu1, cpu2, cpu3, num_interrupts, num_context_switches):
        self.cpu_total = cpu_total
        self.cpu0 = cpu0
        self.cpu1 = cpu1
        self.cpu2 = cpu2
        self.cpu3 = cpu3
        self.num_interrupts = num_interrupts
        self.num_context_switches = num_context_switches

    def print(self):
        print(self.cpu_total)