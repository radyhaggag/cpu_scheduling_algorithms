import flet as ft
from components.process_row import ProcessRow
from utils.app_colors import AppColors
from utils.app_controllers import AppControllers

from utils.app_globals import AppGlobals
from utils.app_strings import AppStrings


class ProcessViewSection(ft.UserControl):
    def build(self):
        return ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        AppStrings.allProcessesView,
                        color=AppColors.red,
                        size=20,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Container(),
                    # Add main table headers
                    ProcessRow(
                        "#",
                        AppStrings.arrivalTime,
                        AppStrings.burstTime,
                    ).build(),
                    ft.Column(
                        ref=AppControllers.processesColumnViewRef,
                        controls=AppGlobals.uiProcesses,
                    ),
                ],
            ),
        )
