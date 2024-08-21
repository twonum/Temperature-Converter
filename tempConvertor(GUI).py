import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("900x510")
root.resizable(False, False)

# Define colors
primaryColor = "#212121"
secondaryColor = "#1DA756"
primShade = "#303030"
secondaryShade = "#136C38"

# Define fonts
def getFont(size=9, bold=False):
    return ("TkDefaultFont", size, "bold" if bold else "normal")

# Input validation function
def validate(P):
    if P == "":
        return True
    try:
        float(P)
        return True
    except ValueError:
        return False

# Conversion dictionary
calcDic = {
    "cf": lambda x: x * 9/5 + 32,
    "ck": lambda x: x + 273.15,
    "fc": lambda x: (x - 32) * 5/9,
    "fk": lambda x: (x - 32) * 5/9 + 273.15,
    "kc": lambda x: x - 273.15,
    "kf": lambda x: (x - 273.15) * 9/5 + 32
}

def calculate():
    try:
        temp = float(entry.get())
        if temp < -273.15:
            raise ValueError("Temperature below absolute zero is not allowed.")
        
        key = f"{unitVar.get()[0].lower()}{convertVar.get()[0].lower()}"
        if key in calcDic:
            result = calcDic[key](temp)
            resultVar.set(f"Result: {result:.2f} {convertVar.get()[0]}")
            resultLabel.config(fg=primaryColor, font=getFont(40, True))
        else:
            resultVar.set("Invalid Conversion")
            resultLabel.config(fg="red", font=getFont(20, True))  # Smaller font size for error
    except ValueError as ve:
        resultVar.set(str(ve))
        resultLabel.config(fg="red", font=getFont(20, True))  # Smaller font size for error


# Register validation function
reg = root.register(validate)

# Left Frame for input and options
leftFrame = tk.Frame(root, bg=primaryColor, width=450, height=510)
leftFrame.pack(side=tk.LEFT, padx=5, pady=5)

# Input Label
enterLabel = tk.Label(leftFrame, text="Enter Temperature", bg=primaryColor, fg=secondaryColor, font=getFont(16, True))
enterLabel.place(x=30, y=50)

# Degree Label
degLabel = tk.Label(leftFrame, text="Degree", bg=primaryColor, fg=secondaryColor, font=getFont(9))
degLabel.place(x=30, y=120)

# Entry field for temperature input
entry = tk.Entry(leftFrame, bg=primShade, fg="#ffffff", insertbackground="#ffffff", font=getFont(12), borderwidth=5, relief="flat", validate="key", validatecommand=(reg, "%P"))
entry.place(x=30, y=160, width=265, height=42)

# Unit selection menu
unitVar = tk.StringVar(value="C")
unitMenu = ttk.OptionMenu(leftFrame, unitVar, "C", "C", "F", "K")
unitMenu.place(x=320, y=160, width=50, height=42)

# Convert To Label
convertToLabel = tk.Label(leftFrame, text="Convert To", bg=primaryColor, fg=secondaryColor, font=getFont(9))
convertToLabel.place(x=30, y=280)

# Convert To menu
convertVar = tk.StringVar(value="Farenheit")
convertToMenu = ttk.OptionMenu(leftFrame, convertVar, "Farenheit", "Farenheit", "Celsius", "Kelvin")
convertToMenu.place(x=30, y=320, width=320, height=42)

# Convert Button
convertButton = tk.Button(leftFrame, text="Convert", bg=secondaryColor, fg=primaryColor, font=getFont(12, True), relief="flat", activebackground=secondaryColor, bd=0, command=calculate)
convertButton.place(x=150, y=400, width=140, height=40)

# Right Frame for result display
rightFrame = tk.Frame(root, bg=secondaryColor, width=450, height=510)
rightFrame.pack(side=tk.RIGHT, padx=5, pady=5)

# Result Label
resultVar = tk.StringVar(value="Result:  F")
resultLabel = tk.Label(rightFrame, textvariable=resultVar, bg=secondaryColor, fg=primaryColor, font=getFont(40, True))
resultLabel.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the main loop
root.mainloop()
