import tkinter as tk

def on_click(button_text):
    current_text = entry.get()

    # Check if the last character is an operation
    last_char_is_operator = current_text[-1:] in ['+', '-', '*', '/']

    if button_text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text in ['+', '-', '*', '/']:
        # Check if the last character is not an operation
        if not last_char_is_operator:
            entry.insert(tk.END, button_text)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Offline Calculator")
root.geometry("300x450")  # Set initial window size
root.resizable(False, False)  # Disable window resizing

# Entry widget to display the current input and result
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Create and place buttons in the grid
row_val = 1
col_val = 0

for button_text in buttons:
    tk.Button(root, text=button_text, width=4, height=2,
              command=lambda text=button_text: on_click(text), font=("Arial", 14)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure column and row weights for resizing
for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i+1, weight=1)

# Label to display your name
your_name_label = tk.Label(root, text="Made By M Harsha Deepan (AKA Shoelayz)", font=("Arial", 12))
your_name_label.grid(row=row_val+1, column=0, columnspan=4, pady=5)

# Label for copyright information
copyright_label = tk.Label(root, text=" Copyright ©M Harsha Deepan 2024", font=("Arial", 10))
copyright_label.grid(row=row_val+2, column=0, columnspan=4, pady=5)

# Run the main loop
root.mainloop()
