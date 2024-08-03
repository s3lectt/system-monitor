import psutil;
import threading;
from PyQt5.QtCore import QThread, pyqtSignal, QObject;

class WorkerSignals (QObject):

    cpu_usage = pyqtSignal (float);
    memory_info = pyqtSignal (tuple);

class Worker (QThread):

    def __init__ (self, signals):

        super ().__init__ ();

        self.signals = signals;
        self._stop_event = threading.Event ();

    def run (self):
        while not self._stop_event.is_set ():

            cpu_percent = psutil.cpu_percent (interval=1);
            
            memory_info = psutil.virtual_memory ();
            total_memory = memory_info.total /  (1024 ** 3);
            available_memory = memory_info.available /  (1024 ** 3);
            used_memory = memory_info.used /  (1024 ** 3);
            
            self.signals.cpu_usage.emit (cpu_percent);
            self.signals.memory_info.emit ((total_memory, available_memory, used_memory));

    def stop (self):

        self._stop_event.set ();
        self.wait ();
