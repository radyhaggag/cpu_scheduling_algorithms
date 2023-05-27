from flet import SnackBar, Text
from utils.app_globals import AppGlobals


def showSnackBar(str, color):
    AppGlobals.page.snack_bar = SnackBar(Text(str), bgcolor=color, duration=1000)
    AppGlobals.page.snack_bar.open = True
    AppGlobals.page.update()
