# System Monitor

## Description
A simple application to monitor your system's CPU and memory usage. Provides real-time updates with an option for translation into different languages.

## Resource Consumption
A lightweight and efficient application for monitoring system performance. Designed to be minimally invasive, this application runs smoothly in the background with negligible impact on your system's resources. It provides real-time updates on CPU usage and memory statistics without consuming significant RAM or CPU.

## Installation
To use this app, clone the repository and run the Python script `main.py`.

### Cloning the repository
```bash
git clone https://github.com/s3lectt/system-monitor.git
```

## Installing dependencies

Install the required Python libraries using `pip`:
```bash
pip install pyqt5 psutil googletrans==4.0.0-rc1
```

## Running the project

Navigate to the project directory and run the application:
```bash
python main.py
```

## Features

* Displays real-time CPU usage.
* Shows system memory statistics (total, available, and used memory).
* Translates UI labels to the specified language using Google Translate.
* Supports both English and Portuguese (and potentially other languages).

## Components
### `worker.py`
Contains the Worker class for background tasks, such as fetching CPU and memory usage using psutil. It uses PyQt5 signals to communicate with the main UI.

### `app.py`
Defines the SystemMonitorApp class which sets up the PyQt5 UI, handles real-time updates from the Worker, and performs translations using googletrans. Includes error handling for translation failures with logging.

### `main.py`
The entry point of the application, initializes the PyQt5 application and starts the SystemMonitorApp.

## Usage

### Viewing system statistics
1. Run the application by executing main.py.
2. The application window will display real-time CPU usage and memory statistics.
### Changing language
1. Modify the self.target_language variable in the SystemMonitorApp class in app.py to set the desired language code (e.g., 'pt' for Portuguese or 'en' for English).

## Contributing
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of the changes you made.

Ensure that your code follows the project's style guidelines and is well-tested.

## License
This project is open-source and free to use. Feel free to use, modify, and distribute this code as you wish. There is no warranty for the code, and it is provided "as-is".