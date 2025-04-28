from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel;
from worker import Worker, WorkerSignals;
from googletrans import Translator;
import logging;

class SystemMonitorApp (QWidget):

    def __init__(self):

        super().__init__();
        
        self.target_language = 'en'; # pt for portuguese
        
        self.translator = Translator();
        
        self.translations = {
            'CPU Usage': '',
            'Memory': '',
            'Total Memory': '',
            'Available Memory': '',
            'Used Memory': '',
        };
        
        self.update_translations();
        self.initUI();
        
        self.signals = WorkerSignals();
        self.signals.cpu_usage.connect(self.update_cpu_label);
        self.signals.memory_info.connect(self.update_memory_label);
        
        self.worker = Worker(self.signals);
        self.worker.start();
        
    def initUI(self):
        
        self.setWindowTitle(self.translations['Memory']);
        self.setGeometry(100, 100, 400, 200);
        
        layout = QVBoxLayout();
        
        self.cpu_label = QLabel(self.translations['CPU Usage'] + ': N/A', self);
        layout.addWidget(self.cpu_label);
        
        self.memory_label = QLabel(self.translations['Memory'] + ': N/A', self);
        layout.addWidget(self.memory_label);
        
        self.setLayout(layout);
    
    def update_translations(self):

        for key in self.translations.keys():
            try:
                self.translations[key] = self.translator.translate(key, dest=self.target_language).text;
            except Exception as e:
                logging.error(f"Error translating text '{key}' to language '{self.target_language}': {e}")
                self.translations[key] = key;
    
    def update_cpu_label(self, cpu_percent):

        self.cpu_label.setText(f"{self.translations['CPU Usage']}: {cpu_percent}%");
    
    def update_memory_label(self, memory_info):

        total_memory, available_memory, used_memory = memory_info;
        self.memory_label.setText (
            f"{self.translations['Total Memory']}: {total_memory:.2f} GB\n"
            f"{self.translations['Available Memory']}: {available_memory:.2f} GB\n"
            f"{self.translations['Used Memory']}: {used_memory:.2f} GB"
        );
    
    def closeEvent(self, event):

        self.worker.stop();
        event.accept();
