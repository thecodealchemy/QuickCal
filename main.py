import tkinter as tk

def format_number(num):
    # Convert to string with 4 decimal places
    str_num = f"{float(num):.4f}"
    # Remove trailing zeros after decimal point
    str_num = str_num.rstrip('0')
    # Remove decimal point if no decimals left
    if str_num.endswith('.'):
        str_num = str_num[:-1]
    return str_num

def evaluate_expression(event=None):
    try:
        expression = entry.get()
        # Clear the entry if expression is empty
        if not expression:
            return
            
        # Store cursor position and original expression
        cursor_pos = entry.index(tk.INSERT)
        
        # Try to evaluate what we have so far
        result = eval(expression.split("=")[0].strip())
        formatted_result = format_number(result)
        
        # Update display without clearing the entry
        current_text = entry.get()
        if "=" in current_text:
            # If there's already a result, update just the result part
            base_expression = current_text.split("=")[0].strip()
            entry.delete(0, tk.END)
            entry.insert(0, f"{base_expression} = {formatted_result}")
        else:
            # First time showing result
            entry.delete(0, tk.END)
            entry.insert(0, f"{expression} = {formatted_result}")
            
        # Restore cursor position
        entry.icursor(cursor_pos)
        
    except Exception as e:
        # Don't clear entry, just show invalid result
        current_text = entry.get()
        if "=" in current_text:
            # Update just the result part
            base_expression = current_text.split("=")[0].strip()
            entry.delete(0, tk.END)
            entry.insert(0, f"{base_expression} = invalid")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, f"{expression} = invalid")
        entry.icursor(cursor_pos)

root = tk.Tk()
root.title("Real-Time Calculator")
root.overrideredirect(True)  # Remove title bar and window decorations

# Set window dimensions
window_width = 400  # Increased from 300 to 400
window_height = 100

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position coordinates
x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)

# Set window size and position
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

root.resizable(False, False)

# Create a frame to hold the entry horizontally
input_frame = tk.Frame(root)
input_frame.pack(pady=20, padx=10, fill="x")

# Create an input box (Entry widget)
entry = tk.Entry(input_frame, font=("Arial", 14), justify="left", width=40)
entry.pack(side="left", expand=True, fill="x")

# Bind the entry box to evaluate_expression on key release
entry.bind("<KeyRelease>", evaluate_expression)

# Add a function to close window on Escape key
def close_window(event=None):
    root.quit()

def check_focus(event=None):
    if not root.focus_get():
        root.quit()

# Bind focus check to root window
root.bind('<FocusOut>', check_focus)
root.bind('<Escape>', close_window)

# Give initial focus to entry
entry.focus_set()

# Run the application
root.mainloop()