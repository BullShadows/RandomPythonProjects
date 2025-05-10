import tkinter as tk
from math import pi
# Store the original positions in a dictionary
original_positions = {}

# Set the value of x1 when a button is pressed
x1 = 0
y1 = 0
negative = False
add = False
sub = False
mul = False
div = False
final = 0
def addtog():
    global add
    global sub
    global mul
    global div
    add = True
    sub = False
    mul = False
    div = False
    if len(str(x1))>=15:
        output_text.set((f"{x1:.15E}+"))  # Update the StringVar
    else:
        output_text.set((str(x1),"+"))
    if negative:
        if len(str(x1))>=15:
            output_text.set((f"-{x1:.15E}+"))  # Update the StringVar
        else:
            output_text.set(("-",str(x1),"+"))

def subtog():
    global add
    global sub
    global mul
    global div
    add = False
    sub = True
    mul = False
    div = False
    if len(str(x1))>=15:
        output_text.set((f"{x1:.15E}-"))  # Update the StringVar
    else:
        output_text.set((str(x1),"-"))
    if negative:
        if len(str(x1))>=15:
            output_text.set((f"-{x1:.15E}-"))  # Update the StringVar
        else:
            output_text.set(("-",str(x1),"-"))

def multog():
    global add
    global sub
    global mul
    global div
    add = False
    sub = False
    mul = True
    div = False
    if len(str(x1))>=15:
        output_text.set((f"{x1:.15E}x"))  # Update the StringVar
    else:
        output_text.set((str(x1),"x"))
    if negative:
        if len(str(x1))>=15:
            output_text.set((f"-{x1:.15E}x"))  # Update the StringVar
        else:
            output_text.set(("-",str(x1),"x"))

def divtog():
    global add
    global sub
    global mul
    global div
    add = False
    sub = False
    mul = False
    div = True
    if len(str(x1))>=15:
        output_text.set((f"{x1:.15E}÷"))  # Update the StringVar
    else:
        output_text.set((str(x1),"÷"))
    if negative:
        if len(str(x1))>=15:
            output_text.set((f"-{x1:.15E}÷"))  # Update the StringVar
        else:
            output_text.set(("-",str(x1),"÷"))
#addingnumvar = None
#addingnumvar2 = "0"
def delete_last_digit(numdx,numdy):
    global x1
    global y1
    global add
    global sub
    global mul
    global div
    if add == False and sub == False and mul == False and div == False:
        if numdx is None or numdx == 0:  # If x is None or 0, return None
            x1=0
        else:
            x_str = str(numdx)  # Convert to string
            x_str = x_str[:-1]  # Remove the last character
            x1 = int(x_str) if x_str else 0  # Convert back to int, or return 0 if empty
        if len(str(x1))>=15:
            output_text.set((f"{x1:.15E}"))  # Update the StringVar
        else:
            output_text.set((str(x1)))
        if negative:
            if len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}"))  # Update the StringVar
            else:
                output_text.set(("-",str(x1)))
    elif add == True or sub == True or mul == True or div == True:
        if numdy is None or numdy == 0:  # If x is None or 0, return None
            y1=0
        else:
            x_str = str(numdy)  # Convert to string
            x_str = x_str[:-1]  # Remove the last character
            y1 = int(x_str) if x_str else 0  # Convert back to int, or return 0 if empty
        if len(str(y1))>=15:
            output_text.set((f"{y1:.15E}"))  # Update the StringVar
        else:
            output_text.set((str(y1)))
        if negative:
            if len(str(y1))>=15:
                output_text.set((f"-{y1:.15E}"))  # Update the StringVar
            else:
                output_text.set(("-",str(y1)))

def set_value(value):
    global y1
    global x1
    #global addingnumvar
    #global addingnumvar2
    if add == False and sub == False and mul == False and div == False:
        #addingnumvar = value
        #addingnumvar2 = value
        x1 = x1*10 +value
        #if x1!=None:
            #x1 = x1*10 + addingnumvar2
        #if not (0 <= value <= 9):  # Ensure digit is a single digit (0-9)
        #    x1 = value
        #elif value !=None:
        #    x1 = x1*10 +value
        #return x * 10 + digit  # Shift existing digits left and add the new digit
        if len(str(x1))>=15:
            output_text.set((f"{x1:.15E}"))  # Update the StringVar
        else:
            output_text.set(str(x1))
        if negative:
            if len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}"))  # Update the StringVar
            else:
                output_text.set(("-",str(x1)))

    elif add == True or sub == True or mul == True or div == True:
        y1 = y1*10+value
    #if y1 == None:
    #    y1 = value
    #elif y1 != None:
    #    x1 = value

    if add == True:
        if negative:
            if len(str(y1))>=15 and len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}+{y1:.15E}"))
            elif len(str(y1))>=15 and len(str(x1))<=15:
                output_text.set((f"-{x1}+{y1:.15E}"))
            elif len(str(y1))<=15 and len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}+{y1}"))
            else:
                output_text.set(("-",str(x1),"+",str(y1)))
        else:
            if len(str(y1))>=15 and len(str(x1))>=15:
                output_text.set((f"{x1:.15E}+{y1:.15E}"))
            elif len(str(y1))>=15 and len(str(x1))<=15:
                output_text.set((f"{x1}+{y1:.15E}"))
            elif len(str(y1))<=15 and len(str(x1))>=15:
                output_text.set((f"{x1:.15E}+{y1}"))
            else:
                output_text.set((str(x1),"+",str(y1)))
        
    elif sub == True:
        if negative:
            if len(str(y1))>=15 and len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}-{y1:.15E}"))
            elif len(str(y1))>=15 and len(str(x1))<=15:
                output_text.set((f"-{x1}-{y1:.15E}"))
            elif len(str(y1))<=15 and len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}-{y1}"))
            else:
                output_text.set(("-",str(x1),"-",str(y1)))
        else:
            if len(str(y1))>=15 and len(str(x1))>=15:
                output_text.set((f"{x1:.15E}-{y1:.15E}"))
            elif len(str(y1))>=15 and len(str(x1))<=15:
                output_text.set((f"{x1}-{y1:.15E}"))
            elif len(str(y1))<=15 and len(str(x1))>=15:
                output_text.set((f"{x1:.15E}-{y1}"))
            else:
                output_text.set((str(x1),"-",str(y1)))
    elif mul == True:
        if negative:
            if len(str(y1))>=15 and len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}x{y1:.15E}"))
            elif len(str(y1))>=15 and len(str(x1))<=15:
                output_text.set((f"-{x1}x{y1:.15E}"))
            elif len(str(y1))<=15 and len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}x{y1}"))
            else:
                output_text.set(("-",str(x1),"x",str(y1)))
        else:
            if len(str(y1))>=15 and len(str(x1))>=15:
                output_text.set((f"{x1:.15E}x{y1:.15E}"))
            elif len(str(y1))>=15 and len(str(x1))<=15:
                output_text.set((f"{x1}x{y1:.15E}"))
            elif len(str(y1))<=15 and len(str(x1))>=15:
                output_text.set((f"{x1:.15E}x{y1}"))
            else:
                output_text.set((str(x1),"x",str(y1)))
    elif div == True:
        if negative:
            if len(str(y1))>=15 and len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}÷{y1:.15E}"))
            elif len(str(y1))>=15 and len(str(x1))<=15:
                output_text.set((f"-{x1}÷{y1:.15E}"))
            elif len(str(y1))<=15 and len(str(x1))>=15:
                output_text.set((f"-{x1:.15E}÷{y1}"))
            else:
                output_text.set(("-",str(x1),"÷",str(y1)))
        else:
            if len(str(y1))>=15 and len(str(x1))>=15:
                output_text.set((f"{x1:.15E}÷{y1:.15E}"))
            elif len(str(y1))>=15 and len(str(x1))<=15:
                output_text.set((f"{x1}÷{y1:.15E}"))
            elif len(str(y1))<=15 and len(str(x1))>=15:
                output_text.set((f"{x1:.15E}÷{y1}"))
            else:
                output_text.set((str(x1),"÷",str(y1)))


def signer():
    global negative
    negative = not negative
def clearfunc():
    output_text.set(" ")
    global y1
    global x1
    global add
    global sub
    global mul
    global div
    global negative
    x1 = 0
    y1 = 0
    negative = False
    add = False
    sub = False
    mul = False
    div = False
def equalfunc():
    global y1
    global x1
    global add
    global sub
    global mul
    global div
    global negative
    global final
    if add and not negative:
        final = x1+y1
    elif add and negative:
        final = -x1+y1
    if sub and not negative:
        final = x1-y1
    elif sub and negative:
        final = -x1-y1
    if mul and not negative:
        final = x1*y1
    elif mul and negative:
        final = -x1*y1
    if div and not negative:
        final = x1/y1
    elif div and negative:
        final = -x1/y1
    if len(str(final))>=35:
        output_text.set((f"{final:.35E}"))
    else:
        output_text.set(final)    
    x1 = 0
    y1 = 0
    negative = False
    add = False
    sub = False
    mul = False
    div = False


# Hover function
def on_hover(event, button, shadow):
    button.place(x=original_positions[button][0] + 2, y=original_positions[button][1] + 2)
    shadow.place(x=original_positions[shadow][0] + 2, y=original_positions[shadow][1] + 2)
    button.config(bg="#A0C9DB")  # Change button color on hover

# Leave function
def on_leave(event, button, shadow):
    button.place(x=original_positions[button][0], y=original_positions[button][1])
    shadow.place(x=original_positions[shadow][0], y=original_positions[shadow][1])
    button.config(bg="lightblue")  # Revert button color

root = tk.Tk()
root.title("Calc")
root.geometry("400x600")

# All the Numbers
# Button 1
shadow1 = tk.Label(root, bg="black")
shadow1.place(x=0, y=200, width=102, height=102)
original_positions[shadow1] = (0, 200)

button1 = tk.Button(
    root,
    text="1",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    width=1,
    height=1,
    command=lambda: set_value(1)
)
button1.place(x=0, y=200, width=100, height=100)
original_positions[button1] = (0, 200)

# Button 2
shadow2 = tk.Label(root, bg="black")
shadow2.place(x=101, y=200, width=102, height=102)
original_positions[shadow2] = (101, 200)

button2 = tk.Button(
    root,
    text="2",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(2)
)
button2.place(x=101, y=200, width=100, height=100)
original_positions[button2] = (101, 200)

# Button 3
shadow3 = tk.Label(root, bg="black")
shadow3.place(x=202, y=200, width=102, height=102)
original_positions[shadow3] = (202, 200)

button3 = tk.Button(
    root,
    text="3",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(3)
)
button3.place(x=202, y=200, width=100, height=100)
original_positions[button3] = (202, 200)

# Button 4
shadow4 = tk.Label(root, bg="black")
shadow4.place(x=0, y=301, width=102, height=102)
original_positions[shadow4] = (0, 301)

button4 = tk.Button(
    root,
    text="4",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(4)
)
button4.place(x=0, y=301, width=100, height=100)
original_positions[button4] = (0, 301)

# Button 5
shadow5 = tk.Label(root, bg="black")
shadow5.place(x=101, y=301, width=102, height=102)
original_positions[shadow5] = (101, 301)

button5 = tk.Button(
    root,
    text="5",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(5)
)
button5.place(x=101, y=301, width=100, height=100)
original_positions[button5] = (101, 301)

# Button 6
shadow6 = tk.Label(root, bg="black")
shadow6.place(x=202, y=301, width=102, height=102)
original_positions[shadow6] = (202, 301)

button6 = tk.Button(
    root,
    text="6",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(6)
)
button6.place(x=202, y=301, width=100, height=100)
original_positions[button6] = (202, 301)

# Button 7
shadow7 = tk.Label(root, bg="black")
shadow7.place(x=0, y=402, width=102, height=102)
original_positions[shadow7] = (0, 402)

button7 = tk.Button(
    root,
    text="7",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(7)
)
button7.place(x=0, y=402, width=100, height=100)
original_positions[button7] = (0, 402)

# Button 8
shadow8 = tk.Label(root, bg="black")
shadow8.place(x=101, y=402, width=102, height=102)
original_positions[shadow8] = (101, 402)

button8 = tk.Button(
    root,
    text="8",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(8)
)
button8.place(x=101, y=402, width=100, height=100)
original_positions[button8] = (101, 402)

# Button 9
shadow9 = tk.Label(root, bg="black")
shadow9.place(x=202, y=402, width=102, height=102)
original_positions[shadow9] = (202, 402)

button9 = tk.Button(
    root,
    text="9",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(9)
)
button9.place(x=202, y=402, width=100, height=100)
original_positions[button9] = (202, 402)

# Button +/-
shadowpl = tk.Label(root, bg="black")
shadowpl.place(x=0, y=503, width=102, height=102)
original_positions[shadowpl] = (0, 503)

buttonpl = tk.Button(
    root,
    text="+/-",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=signer
)
buttonpl.place(x=0, y=503, width=100, height=100)
original_positions[buttonpl] = (0, 503)

# Button 0
shadow0 = tk.Label(root, bg="black")
shadow0.place(x=101, y=503, width=102, height=102)
original_positions[shadow0] = (101, 503)

button0 = tk.Button(
    root,
    text="0",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=lambda: set_value(0)
)
button0.place(x=101, y=503, width=100, height=100)
original_positions[button0] = (101, 503)

# Button add
shadowad = tk.Label(root, bg="black")
shadowad.place(x=303, y=200, width=102, height=102)
original_positions[shadowad] = (303, 200)

buttonad = tk.Button(
    root,
    text="+",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=addtog
)
buttonad.place(x=303, y=200, width=100, height=100)
original_positions[buttonad] = (303, 200)

# Button sub
shadowsu = tk.Label(root, bg="black")
shadowsu.place(x=303, y=301, width=102, height=102)
original_positions[shadowsu] = (303, 301)

buttonsu = tk.Button(
    root,
    text="-",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=subtog
)
buttonsu.place(x=303, y=301, width=100, height=100)
original_positions[buttonsu] = (303, 301)

# Button mul
shadowmul = tk.Label(root, bg="black")
shadowmul.place(x=303, y=402, width=102, height=102)
original_positions[shadowmul] = (303, 402)

buttonmul = tk.Button(
    root,
    text="x",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=multog
)
buttonmul.place(x=303, y=402, width=100, height=100)
original_positions[buttonmul] = (303, 402)

# Button equal
shadoweq = tk.Label(root, bg="black")
shadoweq.place(x=202, y=503, width=102, height=102)
original_positions[shadoweq] = (202, 503)

buttoneq = tk.Button(
    root,
    text="=",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=equalfunc
)
buttoneq.place(x=202, y=503, width=100, height=100)
original_positions[buttoneq] = (202, 503)

# Button divi
shadowd = tk.Label(root, bg="black")
shadowd.place(x=303, y=503, width=102, height=102)
original_positions[shadowd] = (303, 503)

buttond = tk.Button(
    root,
    text="÷",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    command=divtog
)
buttond.place(x=303, y=503, width=100, height=100)
original_positions[buttond] = (303, 503)

# Button pi
shadowpi = tk.Label(root, bg="black")
shadowpi.place(x=0, y=100, width=102, height=102)
original_positions[shadowpi] = (0, 100)

buttonpi = tk.Button(
    root,
    text="π",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    width=1,
    height=1,
    command=lambda: set_value(pi)
)
buttonpi.place(x=0, y=100, width=100, height=100)
original_positions[buttonpi] = (0, 100)

# Button clear
shadowc = tk.Label(root, bg="black")
shadowc.place(x=101, y=100, width=102, height=102)
original_positions[shadowc] = (101, 100)

buttonc = tk.Button(
    root,
    text="c",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    width=1,
    height=1,
    command=clearfunc
)
buttonc.place(x=101, y=100, width=100, height=100)
original_positions[buttonc] = (101, 100)

# Button delete
shadowdel = tk.Label(root, bg="black")
shadowdel.place(x=202, y=100, width=102, height=102)
original_positions[shadowdel] = (202, 100)

buttondel = tk.Button(
    root,
    text="⌫",
    font=("Arial", 26, "bold"),
    bg="lightblue",
    fg="white",
    width=1,
    height=1,
    command=lambda: delete_last_digit(x1,y1)
)
buttondel.place(x=202, y=100, width=100, height=100)
original_positions[buttondel] = (202, 100)



# Create a StringVar to hold the dynamic value
output_text = tk.StringVar()
output_text.set(str(x1))  # Set the initial value of x1
# Create the dynamic Label
output = tk.Label(root, bg="grey", textvariable=output_text, font=("Arial", 24),wraplength=400)
output.place(x=0, y=0, width=400, height=100)

made_by = tk.Label(root,bg = "black",text="Made By Sanat",font=("Arial", 15),fg = "white",wraplength=100)
made_by.place(x=303,y=100,width=100,height=100)

# Bind hover effects
button1.bind("<Enter>", lambda event: on_hover(event, button1, shadow1))
button1.bind("<Leave>", lambda event: on_leave(event, button1, shadow1))
button2.bind("<Enter>", lambda event: on_hover(event, button2, shadow2))
button2.bind("<Leave>", lambda event: on_leave(event, button2, shadow2))
button3.bind("<Enter>", lambda event: on_hover(event, button3, shadow3))
button3.bind("<Leave>", lambda event: on_leave(event, button3, shadow3))
button4.bind("<Enter>", lambda event: on_hover(event, button4, shadow4))
button4.bind("<Leave>", lambda event: on_leave(event, button4, shadow4))
button5.bind("<Enter>", lambda event: on_hover(event, button5, shadow5))
button5.bind("<Leave>", lambda event: on_leave(event, button5, shadow5))
button6.bind("<Enter>", lambda event: on_hover(event, button6, shadow6))
button6.bind("<Leave>", lambda event: on_leave(event, button6, shadow6))
button7.bind("<Enter>", lambda event: on_hover(event, button7, shadow7))
button7.bind("<Leave>", lambda event: on_leave(event, button7, shadow7))
button8.bind("<Enter>", lambda event: on_hover(event, button8, shadow8))
button8.bind("<Leave>", lambda event: on_leave(event, button8, shadow8))
button9.bind("<Enter>", lambda event: on_hover(event, button9, shadow9))
button9.bind("<Leave>", lambda event: on_leave(event, button9, shadow9))
buttonpl.bind("<Enter>", lambda event: on_hover(event, buttonpl, shadowpl))
buttonpl.bind("<Leave>", lambda event: on_leave(event, buttonpl, shadowpl))
button0.bind("<Enter>", lambda event: on_hover(event, button0, shadow0))
button0.bind("<Leave>", lambda event: on_leave(event, button0, shadow0))
buttonad.bind("<Enter>", lambda event: on_hover(event, buttonad, shadowad))
buttonad.bind("<Leave>", lambda event: on_leave(event, buttonad, shadowad))
buttonsu.bind("<Enter>", lambda event: on_hover(event, buttonsu, shadowsu))
buttonsu.bind("<Leave>", lambda event: on_leave(event, buttonsu, shadowsu))
buttonmul.bind("<Enter>", lambda event: on_hover(event, buttonmul, shadowmul))
buttonmul.bind("<Leave>", lambda event: on_leave(event, buttonmul, shadowmul))
buttond.bind("<Enter>", lambda event: on_hover(event, buttond, shadowd))
buttond.bind("<Leave>", lambda event: on_leave(event, buttond, shadowd))
buttoneq.bind("<Enter>", lambda event: on_hover(event, buttoneq, shadoweq))
buttoneq.bind("<Leave>", lambda event: on_leave(event, buttoneq, shadoweq))
buttonpi.bind("<Enter>", lambda event: on_hover(event, buttonpi, shadowpi))
buttonpi.bind("<Leave>", lambda event: on_leave(event, buttonpi, shadowpi))
buttonc.bind("<Enter>", lambda event: on_hover(event, buttonc, shadowc))
buttonc.bind("<Leave>", lambda event: on_leave(event, buttonc, shadowc))
buttondel.bind("<Enter>", lambda event: on_hover(event, buttondel, shadowdel))
buttondel.bind("<Leave>", lambda event: on_leave(event, buttondel, shadowdel))
root.mainloop()
