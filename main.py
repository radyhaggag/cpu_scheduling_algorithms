import flet as ft
from components.process_row import ProcessRow
from components.process_view_section import ProcessViewSection
from components.processes_input_section import ProcessesInputSection
from components.select_operation_section import SelectOperationSection
from utils.app_colors import AppColors
from utils.app_globals import AppGlobals

from utils.app_strings import AppStrings


def main(page: ft.Page):
    page.title = AppStrings.appName
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = AppColors.white
    page.window_width = 850
    page.window_height = 850
    # page.window_resizable = False
    AppGlobals.page = page
    themeMode = ft.ThemeMode(value=ft.ThemeMode.LIGHT)
    page.theme_mode = themeMode
    # page ui
    page.add(
        ProcessViewSection(),  # Column view of process
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        ft.Container(height=10),
                        ProcessesInputSection(),
                        ft.Container(height=35),
                        SelectOperationSection(),
                    ]
                ),
                ft.Container(width=40),
            ],
        ),
    )


ft.app(target=main)
