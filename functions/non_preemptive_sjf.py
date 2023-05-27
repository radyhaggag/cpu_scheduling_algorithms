class SJFNonPreemptiveScheduler:
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
        self.processes.sort(
            key=lambda process: (process["arrivalTime"], process["burstTime"])
        )

    def sortProcessesByBurstTime(self):
        self.processes.sort(key=lambda process: process["burstTime"])

    def getCurrentExecutionIndex(self, executionProgress):
        minBurstTime = float("inf")  # set to a large value initially
        minBurstTimeIndex = -1  # set to an invalid index initially

        # Loop over the list of dictionaries and find the minimum burstTime and its index
        for index, process in enumerate(self.processes):
            if (
                process["completionTime"] == 0
                and process["burstTime"] < minBurstTime
                and process["arrivalTime"] <= executionProgress
            ):
                minBurstTime = process["burstTime"]
                minBurstTimeIndex = index

        return minBurstTimeIndex

    def calcCompletionTime(self):
        self.sortProcessesByArrivalTime()
        executeProgress = self.processes[0]["arrivalTime"]
        for _ in range(self.numOfProcess):
            currentExecuteIndex = self.getCurrentExecutionIndex(executeProgress)
            if executeProgress < self.processes[currentExecuteIndex]["arrivalTime"]:
                executeProgress = (
                    self.processes[currentExecuteIndex]["arrivalTime"]
                    + self.processes[currentExecuteIndex]["burstTime"]
                )
            else:
                executeProgress += self.processes[currentExecuteIndex]["burstTime"]
            completionTime = executeProgress
            self.processes[currentExecuteIndex]["completionTime"] = completionTime

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

        print("#" * 10, "Final result of Non-Preemptive SJF", "#" * 10)
        self.printProcesses()
        averageWaitingTime = self.calcAverageWaitingTime()
        averageTurnAroundTime = self.calcAverageTurnAroundTime()
        return averageWaitingTime, averageTurnAroundTime
