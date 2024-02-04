from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.config(width=500, height=500, padx=50, pady=50)
tk.title("Weight Converter")


# convert def
def convert_kg():
    # Check if the value of kg is int

    try:
        # Get the kg value
        kg_value = weight_entry.get()
        print(kg_value)

        # Value calc
        gram = int(kg_value) * 1000
        pounds = int(kg_value) * 2.205
        ounce = int(kg_value) * 35.274
        centigram = int(kg_value) * 100000
        decigram = int(kg_value) * 10000
        milligram = int(kg_value) * 1000000

        # Text replacing
        gram_text.delete("1.0", END)
        gram_text.insert(END, f"{gram}")

        pound_text.delete("1.0", END)
        pound_text.insert(END, f"{pounds}")

        ounce_text.delete("1.0", END)
        ounce_text.insert(END, f"{ounce}")

        centigram_text.delete("1.0", END)
        centigram_text.insert(END, f"{centigram}")

        decigram_text.delete("1.0", END)
        decigram_text.insert(END, f"{decigram}")

        milligram_text.delete("1.0", END)
        milligram_text.insert(END, f"{milligram}")

    except ValueError:
        messagebox.showerror("Value Error", "Error: Please Enter a Number Not a String")


weightLabel = Label(tk, text="Input The Weight In Kilograms: ", font="Arial", fg='#191919', pady=20)
weightLabel.grid(column=0, row=0)
weight_entry_value = StringVar()
weight_entry = Entry(tk, textvariable=weight_entry_value, borderwidth=2, relief=GROOVE, bg='#527853', fg="white",
                     selectbackground='#191919', insertbackground='white', font="Arial")
weight_entry.grid(column=1, row=0)

gram_entry = Label(text='Gram', font="Arial", fg='#191919')
pound_entry = Label(text='Pound', font="Arial", fg='#191919')
ounce_entry = Label(text='Ounce', font="Arial", fg='#191919')
centigram_entry = Label(text='Centigram', font="Arial", fg='#191919', pady=10)
decigram_entry = Label(text='Decigram', font="Arial", fg='#191919')
milligram_entry = Label(text='Milligram', font="Arial", fg='#191919')
gram_entry.grid(column=0, row=1)
pound_entry.grid(column=1, row=1)
ounce_entry.grid(column=2, row=1)
centigram_entry.grid(column=0, row=3)
decigram_entry.grid(column=1, row=3)
milligram_entry.grid(column=2, row=3)

# Weight values

gram_text = Text(tk, height=5, width=30, font="Arial", bg='#527853', fg='white', borderwidth=.5,
                 selectbackground='#191919', insertbackground='white')
pound_text = Text(tk, height=5, width=30, font="Arial", bg='#527853', fg='white', borderwidth=.5,
                  selectbackground='#191919', insertbackground='white')
ounce_text = Text(tk, height=5, width=30, font="Arial", bg='#527853', fg='white', borderwidth=.5,
                  selectbackground='#191919', insertbackground='white', )
centigram_text = Text(tk, height=5, width=30, font="Arial", bg='#527853', fg='white', borderwidth=.5,
                      selectbackground='#191919', insertbackground='white', )
decigram_text = Text(tk, height=5, width=30, font="Arial", bg='#527853', fg='white', borderwidth=.5,
                     selectbackground='#191919', insertbackground='white', )
milligram_text = Text(tk, height=5, width=30, font="Arial", bg='#527853', fg='white', borderwidth=.5,
                      selectbackground='#191919', insertbackground='white', )

gram_text.grid(column=0, row=2)
pound_text.grid(column=1, row=2)
ounce_text.grid(column=2, row=2)
centigram_text.grid(column=0, row=4)
decigram_text.grid(column=1, row=4)
milligram_text.grid(column=2, row=4)

convert_button = Button(text="Convert", command=convert_kg, width=15, borderwidth=0, relief=GROOVE, bg='#527853',
                        fg="white", activebackground='white', activeforeground='#527853')
convert_button.grid(column=2, row=0)

tk.mainloop()
