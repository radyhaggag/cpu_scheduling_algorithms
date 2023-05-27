class SJFPreemptiveScheduler:
    def __init__(self, processes):
        self.processes = processes
        self.numOfProcess = len(processes)
        self.finalExecutionTime = self.getExecutionTime()
        self.averageWaitingTime = None
        self.averageTurnAroundTime = None

    def prepareProcesses(self):
        for i in range(self.numOfProcess):
            self.processes[i]["remainingTime"] = self.processes[i]["burstTime"]
            self.processes[i]["endTime"] = []
            self.processes[i]["isDone"] = False

    def printProcesses(self):
        print("*" * 75)
        for i in range(self.numOfProcess):
            print(self.processes[i])
        print("*" * 75)

    def sortProcessesByArrivalTime(self):
        self.processes.sort(key=lambda process: process["arrivalTime"])

    def sortProcessesByRemainingTime(self):
        self.processes.sort(key=lambda process: process["remainingTime"])

    def getCurrentExecutionIndex(self, executionProgress):
        minRemainingTime = float("inf")  # set to a large value initially
        minRemainingTimeIndex = -1  # set to an invalid index initially

        # Loop over the list of dictionaries and find the minimum remainingTime and its index
        for index, process in enumerate(self.processes):
            if (
                process["remainingTime"] > 0
                and process["remainingTime"] < minRemainingTime
                and process["arrivalTime"] <= executionProgress
            ):
                minRemainingTime = process["remainingTime"]
                minRemainingTimeIndex = index

        return minRemainingTimeIndex

    def checkIfAllDone(self):
        for i in range(self.numOfProcess):
            if self.processes[i]["remainingTime"] != 0:
                return False
            else:
                self.processes[i]["isDone"] = True

        return True

    def getExecutionTime(self):
        count = 0
        for i in range(self.numOfProcess):
            count += self.processes[i]["burstTime"]
        return count

    def calcWaitingTime(self):
        self.sortProcessesByArrivalTime()
        executeProgress = self.processes[0]["arrivalTime"]
        currentExecuteIdx = self.getCurrentExecutionIndex(executeProgress)
        lastExecuteIdx = currentExecuteIdx

        for _ in range(self.finalExecutionTime - executeProgress):
            self.checkIfAllDone()

            executeProgress += 1
            self.processes[currentExecuteIdx]["remainingTime"] -= 1

            lastExecuteIdx = currentExecuteIdx
            currentExecuteIdx = self.getCurrentExecutionIndex(executeProgress)

            if self.processes[currentExecuteIdx]["remainingTime"] == 0:
                self.processes[lastExecuteIdx]["endTime"].append(executeProgress)
                break

            if currentExecuteIdx != lastExecuteIdx:
                self.processes[lastExecuteIdx]["endTime"].append(executeProgress)
                if self.processes[currentExecuteIdx]["waitingTime"] == 0:
                    if (
                        self.processes[currentExecuteIdx]["remainingTime"]
                        == self.processes[currentExecuteIdx]["burstTime"]
                    ):
                        waitingTime = (
                            executeProgress
                            - self.processes[currentExecuteIdx]["arrivalTime"]
                        )
                        self.processes[currentExecuteIdx]["waitingTime"] = waitingTime
                    else:
                        lastExecuteTime = self.processes[currentExecuteIdx]["endTime"][
                            -1
                        ]
                        waitingTime = executeProgress - lastExecuteTime
                        self.processes[currentExecuteIdx]["waitingTime"] = waitingTime

                else:
                    lastExecuteTime = self.processes[currentExecuteIdx]["endTime"][-1]
                    waitingTime = self.processes[currentExecuteIdx]["waitingTime"] + (
                        executeProgress - lastExecuteTime
                    )
                    self.processes[currentExecuteIdx]["waitingTime"] = waitingTime

    def calcAverageWaitingTime(self):
        avWt = 0
        for i in range(self.numOfProcess):
            avWt += self.processes[i]["waitingTime"]
        return avWt / self.numOfProcess

    def calcAverageTurnAroundTime(self):
        avTat = 0
        for i in range(self.numOfProcess):
            self.processes[i]["turnAroundTime"] = (
                self.processes[i]["waitingTime"] + self.processes[i]["burstTime"]
            )
            avTat += self.processes[i]["turnAroundTime"]
        return avTat / self.numOfProcess

    def executeProcesses(self):
        self.prepareProcesses()
        self.calcWaitingTime()
        self.averageWaitingTime = self.calcAverageWaitingTime()
        self.averageTurnAroundTime = self.calcAverageTurnAroundTime()

    def run(self):
        self.executeProcesses()
        print("#" * 10, "Final result of Preemptive SJF", "#" * 10)
        self.printProcesses()
        return self.averageWaitingTime, self.averageTurnAroundTime
