from pyforms_gui.appmanager import start_app
from win32api import GetSystemMetrics
from src.app.UI.MainWindow import MainWindow

if __name__ == '__main__':
    start_app(MainWindow,
              geometry=(int(GetSystemMetrics(0) / 2) - 160,
                        int(GetSystemMetrics(1) / 2) - 200,
                        320,
                        400))
