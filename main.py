import sys;
from PyQt5.QtWidgets import QApplication;
from app import SystemMonitorApp;

if __name__ == "__main__":
    app = QApplication (sys.argv);
    ex = SystemMonitorApp ();
    ex.show ();
    sys.exit (app.exec_ ());
