# Timestamp Logger

Timestamp Logger is a simple GUI application built using Python's Tkinter library that allows you to log entry and exit times at work into an Excel file.

# Features
- Log entry and exit times.
- Prevent logging exit time without an entry time.
- Store timestamps in an Excel file.

- Calculates Duration between Entry and Exit

# Requirements
- Python 3.x
- pandas library (install using pip install pandas)

# How to Use
- Make sure you have Python 3.x installed on your system.

- Install the required pandas library by running the following command in your terminal:

```cmd
pip install pandas
```

- Download or clone this repository to your local machine.

- Navigate to the project directory using your terminal.

- Run the script:

```cmd
python timestamp_logger.py
```
- The GUI window will open, showing fields for "Entry Time" and "Exit Time" along with buttons to log the times.

- Click the "Log Entry" button to log your entry time. This will also enable the "Log Exit" button.

- After you have completed your work, click the "Log Exit" button to log your exit time.

- Timestamps will be stored in an Excel file named timestamp_log.xlsx.

- The "Log Exit" button will be disabled again until you log your next entry time.

# Note
Make sure to keep the timestamp_log.xlsx file in the same directory as the script, as the application will create or update this file to store the timestamps.