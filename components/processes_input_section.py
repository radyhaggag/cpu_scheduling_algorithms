import flet as ft
from components.process_row import ProcessRow

from utils.app_colors import AppColors
from utils.app_controllers import AppControllers
from utils.app_globals import AppGlobals
from utils.app_strings import AppStrings


class ProcessesInputSection(ft.UserControl):
    def build(self):
        def onAddClicked(self):
            if len(burstTimeTextBox.value) == 0:
                return
            elif (
                len(arrivalTimeTextBox.value) != 0
                and arrivalTimeTextBox.value.isdigit() == False
            ) or burstTimeTextBox.value.isdigit() == False:
                return

            arrTime = (
                0
                if len(arrivalTimeTextBox.value) == 0
                else int(arrivalTimeTextBox.value)
            )

            uiProcess = ProcessRow(
                number=len(AppGlobals.uiProcesses) + 1,
                arrivalTime=arrTime,
                burstTime=burstTimeTextBox.value,
            )
            AppGlobals.uiProcesses.append(uiProcess)

            process = {
                "arrivalTime": arrTime,
                "burstTime": int(burstTimeTextBox.value),
                "waitingTime": 0,
                "turnAroundTime": 0,
            }

            AppGlobals.processes.append(process)
            print(AppGlobals.processes)
            arrivalTimeTextBox.value = ""
            burstTimeTextBox.value = ""
            burstTimeTextBox.update()
            arrivalTimeTextBox.update()
            AppControllers.processesColumnViewRef.current.update()

        arrivalTimeTextBox = ft.TextField(
            hint_text=AppStrings.arrivalTime,
            width=150,
            height=50,
            color=AppColors.black,
            keyboard_type=ft.KeyboardType.NUMBER,
            autofocus=True,
        )
        burstTimeTextBox = ft.TextField(
            hint_text=AppStrings.burstTime,
            width=150,
            height=50,
            color=AppColors.black,
        )

        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        arrivalTimeTextBox,
                        burstTimeTextBox,
                        ft.ElevatedButton(
                            AppStrings.add,
                            width=125,
                            color=AppColors.white,
                            bgcolor=AppColors.red,
                            height=50,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(
                                    radius=10,
                                ),
                            ),
                            on_click=onAddClicked,
                        ),
                    ],
                ),
            ],
        )
