import tkinter as tk
from math import pi

# Calculator state
state = {
    "x1": 0,
    "y1": 0,
    "negative": False,
    "operation": None,  # "add", "sub", "mul", "div"
    "final": 0,
}

# Functions
def set_value(value):
    if state["operation"] is None:  # Update x1
        state["x1"] = state["x1"] * 10 + value
        if state["negative"]:
            state["x1"] = -abs(state["x1"])
        update_display(state["x1"])
    else:  # Update y1
        state["y1"] = state["y1"] * 10 + value
        update_display(f"{state['x1']} {get_op_symbol()} {state['y1']}")

def toggle_sign():
    state["negative"] = not state["negative"]
    if state["operation"] is None:
        state["x1"] = -state["x1"]
        update_display(state["x1"])
    else:
        state["y1"] = -state["y1"]
        update_display(f"{state['x1']} {get_op_symbol()} {state['y1']}")

def set_operation(op):
    if state["operation"] is None:
        state["operation"] = op
        update_display(f"{state['x1']} {get_op_symbol()}")
    else:
        calculate()
        state["operation"] = op

def calculate():
    if state["operation"] == "add":
        state["final"] = state["x1"] + state["y1"]
    elif state["operation"] == "sub":
        state["final"] = state["x1"] - state["y1"]
    elif state["operation"] == "mul":
        state["final"] = state["x1"] * state["y1"]
    elif state["operation"] == "div":
        state["final"] = state["x1"] / state["y1"] if state["y1"] != 0 else "Error"
    update_display(state["final"])
    clear_state()

def clear_state():
    state.update({"x1": 0, "y1": 0, "negative": False, "operation": None, "final": 0})
    update_display(0)

def delete_last_digit():
    if state["operation"] is None:
        state["x1"] //= 10
        update_display(state["x1"])
    else:
        state["y1"] //= 10
        update_display(f"{state['x1']} {get_op_symbol()} {state['y1']}")

def update_display(value):
    output_text.set(str(value))

def get_op_symbol():
    return {"add": "+", "sub": "-", "mul": "x", "div": "÷"}.get(state["operation"], "")

# GUI Setup
root = tk.Tk()
root.title("Full Calculator")
root.geometry("400x600")

# Display
output_text = tk.StringVar()
output_text.set("0")
output = tk.Label(root, bg="grey", textvariable=output_text, font=("Arial", 24))
output.place(x=0, y=0, width=400, height=100)

# Button definitions
buttons = [
    {"text": "1", "pos": (0, 200), "command": lambda: set_value(1)},
    {"text": "2", "pos": (101, 200), "command": lambda: set_value(2)},
    {"text": "3", "pos": (202, 200), "command": lambda: set_value(3)},
    {"text": "4", "pos": (0, 301), "command": lambda: set_value(4)},
    {"text": "5", "pos": (101, 301), "command": lambda: set_value(5)},
    {"text": "6", "pos": (202, 301), "command": lambda: set_value(6)},
    {"text": "7", "pos": (0, 402), "command": lambda: set_value(7)},
    {"text": "8", "pos": (101, 402), "command": lambda: set_value(8)},
    {"text": "9", "pos": (202, 402), "command": lambda: set_value(9)},
    {"text": "0", "pos": (101, 503), "command": lambda: set_value(0)},
    {"text": "+", "pos": (303, 200), "command": lambda: set_operation("add")},
    {"text": "-", "pos": (303, 301), "command": lambda: set_operation("sub")},
    {"text": "x", "pos": (303, 402), "command": lambda: set_operation("mul")},
    {"text": "÷", "pos": (303, 503), "command": lambda: set_operation("div")},
    {"text": "=", "pos": (202, 503), "command": calculate},
    {"text": "C", "pos": (101, 100), "command": clear_state},
    {"text": "⌫", "pos": (202, 100), "command": delete_last_digit},
    {"text": "π", "pos": (0, 100), "command": lambda: set_value(int(pi))},
    {"text": "+/-", "pos": (0, 503), "command": toggle_sign},
]

# Create buttons dynamically
for btn in buttons:
    tk.Button(
        root, text=btn["text"], font=("Arial", 26, "bold"),
        bg="lightblue", fg="white", command=btn["command"]
    ).place(x=btn["pos"][0], y=btn["pos"][1], width=100, height=100)

# Footer Label
made_by = tk.Label(root, bg="black", text="Made By Bull", font=("Arial", 12), fg="white")
made_by.place(x=303, y=100, width=100, height=100)

root.mainloop()
