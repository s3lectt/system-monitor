import sys;
from PyQt5.QtWidgets import QApplication, QMessageBox;
from app import SystemMonitorApp;

def main():

    app = QApplication(sys.argv);

    try:
        ex = SystemMonitorApp();
        ex.show();
        sys.exit(app.exec_());
    except Exception as error:
        error_box = QMessageBox();
        error_box.critical(None, 'Application Error', f'An error ocurred:\n{str(error)}');
        sys.exit(1);


if __name__ == '__main__':
    main();
