import tkinter as tk
import pyodbc
from tkinter import filedialog
import os
import sqlite3

############################## event handlers #######################################

#Event handler for the 'SQL script file' button
def get_script_file():

    filename = filedialog.askopenfilename(title = "Select a SQL script file")
    sql_script_textbox.delete(0, tk.END)
    sql_script_textbox.insert(0, filename)

#Event handler for the 'Database file' button
def get_db_file():
    filename = filedialog.askopenfilename(title = "Select an Ms-Access database file")
    db_textbox.delete(0, tk.END)
    db_textbox.insert(0, filename)

#Event handler for the 'Close' button
def close_it():
    exit(0)


def run_it():
    sql_display_listbox.delete(0, tk.END)

    db_path = db_textbox.get().strip()
    script_path = sql_script_textbox.get().strip()

    if not os.path.isfile(db_path):
        sql_display_listbox.insert(tk.END, f"Invalid DB path: '{db_path}'")
        return
    if not os.path.isfile(script_path):
        sql_display_listbox.insert(tk.END, f"Invalid script path: '{script_path}'")
        return

    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()

            with open(script_path, 'r') as f:
                sql_script = f.read()

            sql_commands = [cmd.strip() for cmd in sql_script.split(';') if cmd.strip()]

            for command in sql_commands:
                # Display command nicely
                for line in command.split('\n'):
                    sql_display_listbox.insert(tk.END, line.strip())
                sql_display_listbox.insert(tk.END, '')  # Blank line

                cursor.execute(command)

            conn.commit()
            sql_display_listbox.insert(tk.END, "Execution complete.")
    except Exception as e:
        sql_display_listbox.insert(tk.END, f"Error: {e}")

#Setting file name to the database path within the function
 

################################# main #########################################

#Create the root window
window = tk.Tk()
window.title("SQL interpreter for Ms-Access")

#Four frames:
header_frame = tk.Frame(master = window)
sql_script_frame = tk.Frame(master = window)
db_frame = tk.Frame(master = window)
sql_display_frame = tk.Frame(master = window)
run_close_frame = tk.Frame(master = window)

header_frame.pack(side = tk.TOP, fill = tk.BOTH)
sql_script_frame.pack(side = tk.TOP, fill = tk.BOTH)
db_frame.pack(side = tk.TOP, fill = tk.BOTH)
sql_display_frame.pack(side = tk.TOP, fill = tk.BOTH)
run_close_frame.pack(side = tk.TOP)

#Text to fill the header
label_text = "Note: assumes 32-bit Python(3), 32-bit Ms-Access, pyodbc, Ms-Access driver"

header_label = tk.Label(master = header_frame, text = label_text, justify = tk.LEFT)
header_label.pack(side = tk.LEFT)

#Two buttons for picking the files
sql_script_button = tk.Button(master = sql_script_frame, text = "SQL script file", command = get_script_file)
db_button = tk.Button(master = db_frame, text = "Database file", command = get_db_file)

#Two text boxes for the file paths
sql_script_textbox = tk.Entry(master = sql_script_frame, width = 100)
db_textbox = tk.Entry(master = db_frame, width = 100)

sql_script_button.pack(side = tk.LEFT)
db_button.pack(side = tk.LEFT)
sql_script_textbox.pack(side = tk.LEFT)
db_textbox.pack(side = tk.LEFT)

#Listbox for displaying things
sql_display_listbox = tk.Listbox(master = sql_display_frame, width = 113, height = 25)
sql_display_listbox.pack(side = tk.LEFT, fill = tk.Y)

#Scrollbar for the listbox
scrollbar = tk.Scrollbar(master = sql_display_frame)
scrollbar.pack(side = tk.LEFT, fill = tk.Y)

#Associate the scrollbar with the listbox
sql_display_listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = sql_display_listbox.yview) 

#Two buttons, each with its own event_handler
run_button = tk.Button(text = "Run", master = run_close_frame, command = run_it)
close_button = tk.Button(text = "Close", master = run_close_frame, command = close_it)

run_button.pack(side = tk.LEFT)
close_button.pack(side = tk.LEFT)

window.mainloop()