import tkinter as tk
from datetime import datetime
import pandas as pd
import os

# Function to log timestamp and update Excel
def log_timestamp(entry_exit):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if entry_exit == "entry":
        entry_var.set(timestamp)
        exit_var.set("")
        exit_button.config(state=tk.NORMAL)
    elif entry_exit == "exit":
        exit_var.set(timestamp)
        entry_time = entry_var.get()
        exit_time = exit_var.get()
        in_time = datetime.strptime(entry_time, "%Y-%m-%d %H:%M:%S")
        out_time = datetime.strptime(exit_time, "%Y-%m-%d %H:%M:%S")
        
        # Calculate the duration
        duration = out_time - in_time
        duration_hours = duration.seconds // 3600
        duration_minutes = (duration.seconds // 60) % 60
        duration_seconds = duration.seconds % 60
        
        duration_var.set(f"{duration_hours} hours {duration_minutes} minutes {duration_seconds} seconds")
        exit_button.config(state=tk.DISABLED)
        df = pd.DataFrame({"Entry Time": [entry_time], "Exit Time": [exit_time], "Duration": [f"{duration_hours}h {duration_minutes}m {duration_seconds}s"]})
        if not pd.DataFrame(df).empty:
            if not os.path.exists("timestamp_log.xlsx"):
                df.to_excel("timestamp_log.xlsx", index=False)
            else:
                existing_df = pd.read_excel("timestamp_log.xlsx")
                updated_df = existing_df.append(df, ignore_index=True)
                updated_df.to_excel("timestamp_log.xlsx", index=False)
        root.after(3000, root.quit)  # Quit the app after 3 seconds

# Main GUI window
root = tk.Tk()
root.title("Timestamp Logger")

# Labels and entry widgets
entry_label = tk.Label(root, text="Entry Time:")
entry_label.grid(row=0, column=0, padx=10, pady=10)
entry_var = tk.StringVar()
entry_entry = tk.Entry(root, textvariable=entry_var, state="readonly")
entry_entry.grid(row=0, column=1, padx=10, pady=10)

exit_label = tk.Label(root, text="Exit Time:")
exit_label.grid(row=1, column=0, padx=10, pady=10)
exit_var = tk.StringVar()
exit_entry = tk.Entry(root, textvariable=exit_var, state="readonly")
exit_entry.grid(row=1, column=1, padx=10, pady=10)

duration_label = tk.Label(root, text="Duration:")
duration_label.grid(row=2, column=0, padx=10, pady=10)
duration_var = tk.StringVar()
duration_entry = tk.Entry(root, textvariable=duration_var, state="readonly")
duration_entry.grid(row=2, column=1, padx=10, pady=10)

# Log buttons
entry_button = tk.Button(root, text="Log Entry", command=lambda: log_timestamp("entry"))
entry_button.grid(row=3, column=0, padx=10, pady=10)

exit_button = tk.Button(root, text="Log Exit", command=lambda: log_timestamp("exit"), state=tk.DISABLED)
exit_button.grid(row=3, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
