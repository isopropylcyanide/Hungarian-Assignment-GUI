import Tkinter as Tk
import tkMessageBox
import assignmentProb as CLI


class Hungarian:

    def __init__(self, master):
        self.r, self.c, self.M = 0, 0, None
        self.root = master
        self.root.minsize(width=550, height=300)
        self.root.title('HUNGARIAN ASSIGNMENT')

        frame = Tk.Frame(self.root)
        frame.pack()

        self.enterRC = Tk.Label(
            frame, text="CONFIGURE ASSIGNMENT MODEl", fg="blue", bd=30,
            font=("Arial", 20))
        self.enterRC.pack(side=Tk.TOP)

        # middle frame
        midFrame = Tk.Frame(self.root)
        midFrame.pack()
        textRow = Tk.Label(midFrame, text="Enter rows:", relief=Tk.SUNKEN,
                           bd=8, pady=4, padx=4,  font=("Times New Roman", 16))
        textCol = Tk.Label(midFrame, text="Enter cols:", relief=Tk.SUNKEN,
                           bd=8, pady=4, padx=4,  font=("Times New Roman", 16))
        self.numRow = Tk.Entry(midFrame, justify=Tk.CENTER,
                               font=("Times New Roman", 16))
        self.numCol = Tk.Entry(midFrame, justify=Tk.CENTER,
                               font=("Times New Roman", 16))

        textRow.grid(row=0, pady=10)
        textCol.grid(row=1, pady=10)
        self.numRow.grid(row=0, column=1, padx=50)
        self.numCol.grid(row=1, column=1, padx=50)

        # Design the lower frame
        bottomFrame = Tk.Frame(self.root, pady=50)
        bottomFrame.pack(side=Tk.TOP)

        self.quitBut = Tk.Button(bottomFrame, text="QUIT",
                                 fg="red", command=frame.quit)

        self.quitBut.pack(side=Tk.LEFT, padx=50)

        self.nextBut = Tk.Button(
            bottomFrame, text="Continue", command=self.validateInput)
        self.nextBut.pack(side=Tk.RIGHT, padx=60)

    def validateInput(self):
        r, c = self.numRow.get(), self.numCol.get()
        if not (r.isdigit() and c.isdigit()):
            tkMessageBox.showinfo("Error", 'Enter valid rows and columns')
        else:
            self.r, self.c = int(r), int(c)
            self.storeModel()

    def storeModel(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.root.title('ENTER VALUES')
        self.root.minsize(width=550, height=400)

        frame = Tk.Frame(self.root)
        frame.pack()
        self.enterRC = Tk.Label(frame, text="Fill %d X %d matrix" % (
            self.r, self.c), fg="blue", bd=20, font=("Arial", 12))
        self.enterRC.pack(side=Tk.TOP)

        midFrame = Tk.Frame(self.root)
        midFrame.pack()

        self.M_entry = [[0 for i in xrange(self.c)] for j in xrange(self.r)]
        self.M = [[0 for i in xrange(self.c)] for j in xrange(self.r)]
        for i in xrange(self.r):
            for j in xrange(self.c):
                self.M_entry[i][j] = Tk.Entry(midFrame, justify=Tk.CENTER,
                                              font=("Times New Roman", 16))
                self.M_entry[i][j].insert(0, "0")

        for i in xrange(self.r):
            for j in xrange(self.c):
                self.M_entry[i][j].grid(row=i, column=j, padx=10, pady=10)

        # Design the lower frame
        bottomFrame = Tk.Frame(self.root, pady=50)
        bottomFrame.pack(side=Tk.TOP)

        self.rstBut = Tk.Button(bottomFrame, text="RESET",
                                fg="red", command=self.resetModel)

        self.rstBut.pack(side=Tk.LEFT, padx=50)

        self.solveBut = Tk.Button(
            bottomFrame, text="Solve", command=self.solveModel)
        self.solveBut.pack(side=Tk.RIGHT, padx=60)

    def resetModel(self):
        for i in xrange(self.r):
            for j in xrange(self.c):
                self.M_entry[i][j].delete(0, Tk.END)
                self.M_entry[i][j].insert(0, '0')

    def solveModel(self):
        allIntegers = True
        for i in xrange(self.r):
            for j in xrange(self.c):
                if not (self.M_entry[i][j].get()).isdigit():
                    allIntegers = False
                    break
            if not allIntegers:
                break
        if not allIntegers:
            tkMessageBox.showinfo("Error", 'Only integer values are allowed')
            self.resetModel()
        else:
            for i in xrange(self.r):
                for j in xrange(self.c):
                    self.M[i][j] = int(self.M_entry[i][j].get())

            CLI._GUI_M = self.M
            CLI._GUI_ROW = self.r
            CLI._GUI_COL = self.c
            CLI.main()

if __name__ == '__main__':
    root = Tk.Tk()
    hGui = Hungarian(root)
    root.mainloop()
    pass
