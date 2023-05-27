class FCFScheduler:
    def __init__(self, processes):
        self.processes = processes
        self.numOfProcess = len(processes)

    def prepareProcesses(self):
        for i in range(self.numOfProcess):
            self.processes[i]["completionTime"] = 0

    def printProcesses(self):
        print("*" * 75)
        for i in range(self.numOfProcess):
            print(self.processes[i])
        print("*" * 75)

    def sortProcessesByArrivalTime(self):
        self.processes.sort(key=lambda process: process["arrivalTime"])

    def sortProcessesByBurstTime(self):
        self.processes.sort(key=lambda process: process["burstTime"])

    def calcCompletionTime(self):
        self.sortProcessesByArrivalTime()
        executeProgress = self.processes[0]["arrivalTime"]
        for i in range(self.numOfProcess):
            if executeProgress < self.processes[i]["arrivalTime"]:
                executeProgress = (
                    self.processes[i]["arrivalTime"] + self.processes[i]["burstTime"]
                )
            else:
                executeProgress += self.processes[i]["burstTime"]
            completionTime = executeProgress
            self.processes[i]["completionTime"] = completionTime

    def calcTurnAroundTimeAndWaitingTime(self):
        for i in range(self.numOfProcess):
            tat = self.processes[i]["completionTime"] - self.processes[i]["arrivalTime"]
            self.processes[i]["turnAroundTime"] = tat
            wt = tat - self.processes[i]["burstTime"]
            self.processes[i]["waitingTime"] = wt

    def calcAverageWaitingTime(self):
        avWt = 0
        for i in range(self.numOfProcess):
            avWt += self.processes[i]["waitingTime"]
        return avWt / self.numOfProcess

    def calcAverageTurnAroundTime(self):
        avTat = 0
        for i in range(self.numOfProcess):
            avTat += self.processes[i]["turnAroundTime"]
        return avTat / self.numOfProcess

    def run(self):
        self.prepareProcesses()
        self.calcCompletionTime()
        self.calcTurnAroundTimeAndWaitingTime()

        print("#" * 10, "Final result of FCFS", "#" * 10)
        self.printProcesses()
        averageWaitingTime = self.calcAverageWaitingTime()
        averageTurnAroundTime = self.calcAverageTurnAroundTime()
        return averageWaitingTime, averageTurnAroundTime
