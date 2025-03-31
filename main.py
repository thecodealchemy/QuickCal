import tkinter as tk
from tkinter import ttk
import math

def format_number(num):
    # Convert to string with 4 decimal places
    str_num = f"{float(num):.4f}"
    # Remove trailing zeros after decimal point
    str_num = str_num.rstrip('0')
    # Remove decimal point if no decimals left
    if str_num.endswith('.'):
        str_num = str_num[:-1]
    return str_num

def replace_operators(expression):
    """
    Replace the caret operator (^) with double asterisk (**) for exponentiation.
    Also, replace 'pi' with math.pi.
    """
    expression = expression.replace('^', '**')
    expression = expression.replace('pi', 'math.pi')
    return expression

def evaluate_expression(event=None):
    try:
        expression = entry.get()
        # Clear the entry if expression is empty
        if not expression.strip():
            return

        # Store cursor position and original expression
        cursor_pos = entry.index(tk.INSERT)

        # Replace operators and add math functions
        processed_expression = replace_operators(expression)

        # Evaluate the expression
        result = eval(processed_expression.split("=")[0].strip())
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

    except ZeroDivisionError:
        # Handle division by zero
        current_text = entry.get()
        if "=" in current_text:
            base_expression = current_text.split("=")[0].strip()
            entry.delete(0, tk.END)
            entry.insert(0, f"{base_expression} = division by zero")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, f"{expression} = division by zero")
        entry.icursor(cursor_pos)
    except Exception as e:
        # Handle other exceptions
        current_text = entry.get()
        if "=" in current_text:
            base_expression = current_text.split("=")[0].strip()
            entry.delete(0, tk.END)
            entry.insert(0, f"{base_expression} = invalid")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, f"{expression} = invalid")
        entry.icursor(cursor_pos)

def on_escape(event=None):
    root.quit()

def on_focus_out(event=None):
    if not root.focus_get():
        root.quit()

# Initialize the main window
root = tk.Tk()
root.title("Advanced Calculator")
root.overrideredirect(True)  # Remove title bar and window decorations

# Set window dimensions
window_width = 400
window_height = 60  # Reduced height for minimal design

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position coordinates
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

# Set window size and position
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Make the window semi-transparent (0.9 opacity)
root.attributes('-alpha', 0.9)

root.resizable(False, False)

# Configure dark theme
root.configure(bg='#2e2e2e')  # Dark background

# Create a frame to hold the entry horizontally
input_frame = tk.Frame(root, bg='#2e2e2e')
input_frame.pack(pady=0, padx=0, fill="both", expand=True)  # Removed unnecessary padding

# Create an input box (Entry widget) with dark theme
entry = tk.Entry(input_frame, font=("Arial", 16), justify="left", bg='#3c3c3c', fg='#ffffff', insertbackground='#ffffff', borderwidth=0, highlightthickness=0)
entry.pack(side="left", fill="both", expand=True, padx=10, pady=10)  # Adjusted padding for minimal gaps

# Bind the entry box to evaluate_expression on key release
entry.bind("<KeyRelease>", evaluate_expression)

# Bind the Escape key to close the window
root.bind('<Escape>', on_escape)

# Bind focus out to close the window
root.bind('<FocusOut>', on_focus_out)

# Give initial focus to entry
entry.focus_set()

# Run the application
root.mainloop()