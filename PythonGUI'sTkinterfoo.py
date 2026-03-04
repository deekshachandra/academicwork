import tkinter as tk
from tkinter import filedialog

############################## event handlers #######################################

#event handler for the 'Select text file' button
def get_text_file():
  filename = filedialog.askopenfilename(title = "Select a text file")
  text_file_entry.delete(0, tk.END)
  text_file_entry.insert(0, filename)

#event handler for the 'Close' button
def close_it():
  exit(0)

#event handler for the 'Display' button
def display_it():
  #clear the display_textbox
  display_textbox.delete("1.0", tk.END)

  #read text from the file listed in the file_textbox
  my_file = text_file_entry.get()
  try:
    fi = open(my_file, "r")
  except:
    display_textbox.insert("1.0", "Error opening text file...")
    return() #Note: return(), not exit()
  my_string = fi.read()
  display_textbox.insert("1.0", my_string)

################################# main #########################################

#create the root window
window = tk.Tk()
window.title("Simple Tkinter example")

#three frames:
text_file_frame = tk.Frame(master = window)
display_frame = tk.Frame(master = window)
display_close_frame = tk.Frame(master = window)

text_file_frame.pack(side = tk.TOP, fill = tk.BOTH)
display_frame.pack(side = tk.TOP, fill = tk.BOTH)
display_close_frame.pack(side = tk.TOP)

#button for picking the files
text_file_button = tk.Button(master = text_file_frame, text = "Select text file", command = get_text_file)

#entry for the file paths
text_file_entry = tk.Entry(master = text_file_frame, width = 100)

text_file_button.pack(side = tk.LEFT)
text_file_entry.pack(side = tk.LEFT)

#textbox for displaying things
display_textbox = tk.Text(master = display_frame, width = 113, height = 25)
display_textbox.pack(side = tk.LEFT, fill = tk.Y)

#scrollbar for the display textbox
scrollbar = tk.Scrollbar(master = display_frame)
scrollbar.pack(side = tk.LEFT, fill = tk.Y)

#associate the scrollbar with the listbox
display_textbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = display_textbox.yview) 

#two buttons, each with its own event_handler
display_button = tk.Button(text = "Display", master = display_close_frame, command = display_it)
close_button = tk.Button(text = "Close", master = display_close_frame, command = close_it)

display_button.pack(side = tk.LEFT)
close_button.pack(side = tk.LEFT)

#start the main event manager
window.mainloop()