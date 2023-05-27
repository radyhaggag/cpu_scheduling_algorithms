class RoundRobinScheduler:
    def __init__(self, processes, timeQuantum):
        self.processes = processes
        self.numOfProcess = len(processes)
        self.averageWaitingTime = None
        self.averageTurnAroundTime = None
        self.timeQuantum = timeQuantum

        self.remaining_burst_time = []
        self.waiting_time = []
        self.turnaround_time = []
        self.total_time = 0

    def prepareProcesses(self):
        self.remaining_burst_time = [process["burstTime"] for process in self.processes]
        self.waiting_time = [0] * len(self.processes)
        self.turnaround_time = [0] * len(self.processes)
        self.total_time = 0

    def executeProcesses(self):
        while True:
            all_processes_completed = True

            # Execute each process for the given time quantum or until completion
            for i in range(self.numOfProcess):
                if self.remaining_burst_time[i] > 0:
                    all_processes_completed = False

                    if self.remaining_burst_time[i] > self.timeQuantum:
                        self.total_time += self.timeQuantum
                        self.remaining_burst_time[i] -= self.timeQuantum
                    else:
                        self.total_time += self.remaining_burst_time[i]
                        self.turnaround_time[i] = (
                            self.total_time - self.processes[i]["arrivalTime"]
                        )
                        self.waiting_time[i] = (
                            self.turnaround_time[i] - self.processes[i]["burstTime"]
                        )
                        self.remaining_burst_time[i] = 0

            if all_processes_completed:
                break

    def calcAverageWaitingTime(self):
        avg_waiting_time = sum(self.waiting_time) / self.numOfProcess
        return avg_waiting_time

    def calcAverageTurnAroundTime(self):
        avg_turnaround_time = sum(self.turnaround_time) / self.numOfProcess
        return avg_turnaround_time

    def run(self):
        self.prepareProcesses()
        self.executeProcesses()
        self.averageWaitingTime = self.calcAverageWaitingTime()
        self.averageTurnAroundTime = self.calcAverageTurnAroundTime()
        print("#" * 10, "Final result of Round Robin", "#" * 10)
        print("Average Waiting Time (AVWT): ", self.averageWaitingTime)
        print("Average Turn Around Time (AVTAT): ", self.averageTurnAroundTime)
        return self.averageWaitingTime, self.averageTurnAroundTime
