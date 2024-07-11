from tkinter import *

window = Tk()
window.minsize(width=300, height=150)
window.title("Mile to Kilometer Converter")
window.config(padx=10, pady=10)


empty_label = Label(text=" ")
empty_label.grid(column=0, row=0)
empty_label.config(padx=40, pady=10)

input = Entry(width=10)
input.focus()
input.grid(column=1, row=0)

label_1 = Label(text="Miles", font=("Times New Roman", 16))
label_1.grid(column=2, row=0)
label_1.config(padx=10, pady=10)

label_2 = Label(text="is equal to", font=("Times New Roman", 16))
label_2.grid(column=0, row=1)
label_2.config(padx=10, pady=10)

result_label = Label(text="0", font=("Times New Roman", 16))
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)

label_3 = Label(text="Kilometers", font=("Times New Roman", 16))
label_3.grid(column=2, row=1)
label_3.config(padx=10, pady=10)

def calculate():
    result = round(float(input.get()) * 1.609, 2)
    result_label.config(text=f"{result}")

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()