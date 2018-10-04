from tkinter import *
from tkinter import ttk
import random as rand
root = Tk()

class App:

    def __init__(self, master):
        mframe = Frame(master, width=500, height=500)
        mframe.pack()

        master.title("Pricing")

        self.price = StringVar(value="Price: $0.00")
        self.progress = IntVar()
        self.shipping = ["UPS", "Express", "Ground"]
        self.itemlist = ["Chicken", "Spaghetti", "Marinara", "Water", "Book", "CD", "Car", "Andrew", "Soda", "Computer", "Math", "Dry Erase Marker", "Glue", "Pencil", "Peach"]
        self.pricelist = dict()
        for item in self.itemlist:
            self.pricelist[item] = rand.randint(1, 50)

        self.choicebox = ttk.Combobox(mframe, width=12, state='readonly', value=self.shipping)
        self.choicebox.grid(column=1, row=1, sticky='w')
        self.choicebox.bind('<<ComboboxSelected>>')

        self.itembox = Listbox(mframe, height=10, listvariable=self.itemlist)
        for item in self.itemlist:
            self.itembox.insert('end', '%s' % item)
        self.itembox.grid(column=1, row=2, sticky='w')

        notebox = Text(mframe, width=10, height=5, wrap='word')
        notebox.grid(column=2, row=2)

        l = Label(mframe, text=self.price.get())
        l.grid(column=456, row=238)

        s = ttk.Scrollbar(mframe, orient=VERTICAL, command=self.itembox.yview)
        s.grid(column=0, row=2, sticky='nse')
        self.itembox.configure(yscrollcommand=s.set)

        p = ttk.Progressbar(mframe, orient=VERTICAL, length=100, mode='determinate', value=self.progress.get())
        p.grid(column=3, row=2)

        calculate = Button(mframe, text="SUBMIT", command=self.calc)
        calculate.grid(column=3, row=3)

        clearb = Button(mframe, text="CLEAR", command=self.clear)
        clearb.grid(column=4, row=3)

    def calc(self):
        pass

    def clear(self):
        pass






app = App(root)
root.mainloop()