import flet as ft

from utils.app_colors import AppColors


class CustomCellView(ft.UserControl):
    def __init__(
        self,
        text,
        width=None,
    ):
        super().__init__()
        self.text = text
        self.width = width

    def build(self):
        return ft.Container(
            margin=-6,
            width=200 if self.width == None else self.width,
            height=50,
            content=self.text,
            bgcolor=AppColors.grey,
            padding=0,
            alignment=ft.alignment.center,
            border=ft.border.all(color=AppColors.darkGrey, width=1),
        )
