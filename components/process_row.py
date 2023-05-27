import flet as ft
import copy as copy
from components.custom_cell_view import CustomCellView

from utils.app_colors import AppColors
from utils.app_controllers import AppControllers
from utils.app_globals import AppGlobals


class ProcessRow(ft.UserControl):
    def __init__(
        self,
        number,
        arrivalTime,
        burstTime,
    ):
        super().__init__()
        self.number = number
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime

    def buildText(self, value):
        return ft.Text(
            value,
            color=AppColors.black,
            weight=ft.FontWeight.BOLD,
            size=15,
        )

    def copyArray(self, arr):
        new_arr = copy.copy(arr)
        return new_arr

    def editProcessesNumbers(self):
        processes = self.copyArray(AppGlobals.uiProcesses)
        AppGlobals.uiProcesses.clear()

        for i in range(len(processes)):
            oldProcess = processes[i]
            uiProcess = ProcessRow(
                number=i + 1,
                arrivalTime=oldProcess.arrivalTime,
                burstTime=oldProcess.burstTime,
            )
            AppGlobals.uiProcesses.append(uiProcess)

    def onDeleteTapped(self, _):
        AppGlobals.processes.pop(self.number - 1)
        AppGlobals.uiProcesses.pop(self.number - 1)
        self.editProcessesNumbers()
        AppControllers.processesColumnViewRef.current.update()

    def getIcon(self):
        try:
            integer = int(self.arrivalTime)

            return ft.GestureDetector(
                content=ft.CircleAvatar(
                    bgcolor=AppColors.red,
                    content=ft.Icon(ft.icons.DELETE_ROUNDED, color=AppColors.white),
                ),
                on_tap=self.onDeleteTapped,
            )

        except ValueError:
            return ft.Container(width=40)

    def build(self):
        numText = self.buildText(self.number)
        arrTimeText = self.buildText(self.arrivalTime)
        burTimeText = self.buildText(self.burstTime)

        return ft.Row(
            controls=[
                CustomCellView(numText, 50).build(),
                CustomCellView(arrTimeText, None),
                CustomCellView(burTimeText, None),
                # ft.Icon(ft.icons.DELETE_ROUNDED, color=AppColors.white),
                ft.Container(),
                self.getIcon(),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
