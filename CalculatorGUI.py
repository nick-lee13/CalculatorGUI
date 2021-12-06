import tkinter as tk

calculation = ""

#Adds a symbol to calulation text field
def add_to_calcualtion(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

#Evaluates the expression in the text field, returns error if unable
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

#Clear current text field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

#Init GUI Pane
root = tk.Tk()
root.geometry("300x275")

#Calculator text box
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

#Calculator Buttons
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calcualtion(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calcualtion(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calcualtion(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calcualtion(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calcualtion(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calcualtion(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calcualtion(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calcualtion(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calcualtion(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calcualtion(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calcualtion("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calcualtion("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calcualtion("*"), width=5, font=("Arial", 14))
btn_multiply.grid(row=4, column=4)
btn_divide = tk.Button(root, text="/", command=lambda: add_to_calcualtion("/"), width=5, font=("Arial", 14))
btn_divide.grid(row=5, column=4)
btn_openParen = tk.Button(root, text="(", command=lambda: add_to_calcualtion("("), width=5, font=("Arial", 14))
btn_openParen.grid(row=5, column=1)
btn_closeParen = tk.Button(root, text=")", command=lambda: add_to_calcualtion(")"), width=5, font=("Arial", 14))
btn_closeParen.grid(row=5, column=3)
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=12, font=("Arial", 14))
btn_equals.grid(row=6, column=3,columnspan=2)
btn_clear = tk.Button(root, text="C", command=clear_field, width=12, font=("Arial", 14))
btn_clear.grid(row=6, column=1,columnspan=2)

root.mainloop()