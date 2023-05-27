import flet as ft
import copy
from components.custom_cell_view import CustomCellView
from components.show_snackbar import showSnackBar
from functions.fcfs import FCFScheduler
from functions.non_preemptive_sjf import SJFNonPreemptiveScheduler
from functions.preemptive_sjf import SJFPreemptiveScheduler
from functions.round_robin import RoundRobinScheduler
from utils.app_colors import AppColors
from utils.app_globals import AppGlobals
from utils.app_operations import AppOperations

from utils.app_strings import AppStrings


class SelectOperationSection(ft.UserControl):
    def build(self):
        operations = [
            AppOperations.firstComeFirstServed,
            AppOperations.shortestJobFirstPreemptive,
            AppOperations.shortestJobFirstNonPreemptive,
            AppOperations.roundRobin,
        ]
        operationsDropdown = ft.Dropdown(
            width=450,
            hint_text=AppStrings.selectTheOperation,
            options=[ft.dropdown.Option(operation) for operation in operations],
        )

        avWtMessage = CustomCellView(
            ft.Text(
                AppStrings.avWtMessage,
                color=AppColors.black,
                weight=ft.FontWeight.BOLD,
                size=15,
            ),
            350,
        )
        avTatMessage = CustomCellView(
            ft.Text(
                AppStrings.avTatMessage,
                color=AppColors.black,
                weight=ft.FontWeight.BOLD,
                size=15,
            ),
            350,
        )
        avWtMessageValueRef = ft.Ref[ft.Text]()
        avTatMessageValueRef = ft.Ref[ft.Text]()
        avWtMessageValue = CustomCellView(
            ft.Text(
                "ـــــــــ",
                color=AppColors.black,
                weight=ft.FontWeight.BOLD,
                size=18,
                ref=avWtMessageValueRef,
            ),
            100,
        )
        avTatMessageValue = CustomCellView(
            ft.Text(
                "ـــــــــ",
                color=AppColors.black,
                weight=ft.FontWeight.BOLD,
                size=18,
                ref=avTatMessageValueRef,
            ),
            100,
        )

        def onStartClicked(self):
            if len(AppGlobals.processes) == 0:
                return
            if operationsDropdown.value == AppOperations.shortestJobFirstPreemptive:
                processes = copy.deepcopy(AppGlobals.processes)
                scheduler = SJFPreemptiveScheduler(processes)
                avWt, aTat = scheduler.run()
                avWtMessageValue.text.value = round(avWt, 2)
                avTatMessageValue.text.value = round(aTat, 2)
                avTatMessageValueRef.current.update()
                avWtMessageValueRef.current.update()

            elif operationsDropdown.value == AppOperations.firstComeFirstServed:
                processes = copy.deepcopy(AppGlobals.processes)
                scheduler = FCFScheduler(processes)
                avWt, aTat = scheduler.run()
                avWtMessageValue.text.value = round(avWt, 2)
                avTatMessageValue.text.value = round(aTat, 2)
                avTatMessageValueRef.current.update()
                avWtMessageValueRef.current.update()

            elif (
                operationsDropdown.value == AppOperations.shortestJobFirstNonPreemptive
            ):
                processes = copy.deepcopy(AppGlobals.processes)
                scheduler = SJFNonPreemptiveScheduler(processes)
                avWt, aTat = scheduler.run()
                avWtMessageValue.text.value = round(avWt, 2)
                avTatMessageValue.text.value = round(aTat, 2)
                avTatMessageValueRef.current.update()
                avWtMessageValueRef.current.update()

            elif operationsDropdown.value == AppOperations.roundRobin:

                def close_dlg(e):
                    dlg.open = False
                    AppGlobals.page.update()
                    if (
                        quantumField.value.isdigit() != True
                        or len(quantumField.value) == 0
                    ):
                        showSnackBar("Invalid quantum value", ft.colors.RED)

                    else:
                        processes = copy.deepcopy(AppGlobals.processes)
                        scheduler = RoundRobinScheduler(
                            processes, int(quantumField.value)
                        )
                        avWt, aTat = scheduler.run()

                        avWtMessageValue.text.value = round(avWt, 2)
                        avTatMessageValue.text.value = round(aTat, 2)
                        avTatMessageValueRef.current.update()
                        avWtMessageValueRef.current.update()

                quantumField = ft.TextField(
                    hint_text="Enter the quantum value",
                    width=150,
                    height=50,
                    color=AppColors.black,
                    keyboard_type=ft.KeyboardType.NUMBER,
                    autofocus=True,
                )
                dlg = ft.AlertDialog(
                    modal=True,
                    title=ft.Text("Quantum value"),
                    on_dismiss=lambda e: print("Dialog dismissed!"),
                    content=quantumField,
                    actions=[ft.TextButton("Done", on_click=close_dlg)],
                    actions_alignment=ft.MainAxisAlignment.END,
                )
                AppGlobals.page.dialog = dlg
                dlg.open = True
                AppGlobals.page.update()

        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    operationsDropdown,
                    ft.ElevatedButton(
                        AppStrings.startCalc,
                        width=450,
                        color=AppColors.white,
                        bgcolor=AppColors.red,
                        height=50,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(
                                radius=10,
                            )
                        ),
                        on_click=onStartClicked,
                    ),
                    ft.Container(),
                    ft.Container(
                        width=300, bgcolor=AppColors.black, height=1, padding=10
                    ),
                    ft.Container(),
                    ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    avWtMessage.build(),
                                    avWtMessageValue,
                                ],
                            ),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    avTatMessage.build(),
                                    avTatMessageValue,
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
