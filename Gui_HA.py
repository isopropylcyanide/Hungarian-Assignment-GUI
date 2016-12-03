import Tkinter as Tk
import tkMessageBox
import tkFileDialog
import assignmentProb as CLI
from cStringIO import StringIO
import sys


class Capturing(list):
    """Class to capture output from a function"""

    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


class Hungarian:
    """The main class dealing with the GUI input / output"""

    def __init__(self, master):
        self.r, self.c, self.Matrix = 0, 0, None
        self.root = master
        self.root.minsize(width=550, height=300)
        self.root.title('HUNGARIAN ASSIGNMENT')

        # topframe has a Label
        self.topFrame = Tk.Frame(self.root)
        self.topFrame.pack()

        self.enterRC = Tk.Label(
            self.topFrame, text="CONFIGURE ASSIGNMENT MODEl", fg="blue", bd=30,
            font=("Arial", 20))
        self.enterRC.pack(side=Tk.TOP)

        # middle frame has two label and entry boxes
        self.midFrame = Tk.Frame(self.root)
        self.midFrame.pack()
        textRow = Tk.Label(self.midFrame, text="Enter rows:", relief=Tk.SUNKEN,
                           bd=8, pady=4, padx=4,  font=("Times New Roman", 16))
        textCol = Tk.Label(self.midFrame, text="Enter cols:", relief=Tk.SUNKEN,
                           bd=8, pady=4, padx=4,  font=("Times New Roman", 16))
        self.rowEntry = Tk.Entry(self.midFrame, justify=Tk.CENTER, width=12,
                                 font=("Times New Roman", 16))
        self.colEntry = Tk.Entry(self.midFrame, justify=Tk.CENTER, width=12,
                                 font=("Times New Roman", 16))

        textRow.grid(row=0, pady=10)
        textCol.grid(row=1, pady=10)
        self.rowEntry.grid(row=0, column=1, padx=50)
        self.colEntry.grid(row=1, column=1, padx=50)

        # bottomFrame has necessary Buttons
        self.bottomFrame = Tk.Frame(self.root, pady=50)
        self.bottomFrame.pack(side=Tk.TOP)

        self.quitBut = Tk.Button(self.bottomFrame, text="QUIT",
                                 font=("Times New Roman", 16), fg="dark green",
                                 command=self.topFrame.quit)

        self.quitBut.pack(side=Tk.LEFT, padx=50)

        self.nextBut = Tk.Button(self.bottomFrame, text="CONTINUE",
                                 font=("Times New Roman", 16), fg="dark green",
                                 command=self.validateInput)
        self.nextBut.pack(side=Tk.RIGHT, padx=60)

    def validateInput(self):
        """Verify whether the entered row/col are correct"""
        r, c = self.rowEntry.get(), self.colEntry.get()
        if not (r.isdigit() and c.isdigit()):
            tkMessageBox.showinfo("Error", 'Enter valid rows and columns')
        else:
            self.r, self.c = int(r), int(c)
            self.getAssignments()

    def getAssignments(self):
        """Get the assignments from the user"""
        for child in self.root.winfo_children():
            child.pack_forget()

        self.root.title('ENTER VALUES')
        self.root.minsize(width=550, height=400)

        # topframe has the fill label
        topFrame = Tk.Frame(self.root)
        topFrame.pack()
        self.fillRC = Tk.Label(topFrame, text="Fill %d X %d matrix" % (
            self.r, self.c), fg="blue", bd=20, font=("Times New Roman", 20))
        self.fillRC.pack(side=Tk.TOP)

        # midframe allows the user to enter assignments
        midFrame = Tk.Frame(self.root)
        midFrame.pack()

        self.Mat_entry = [[0 for i in xrange(self.c)] for j in xrange(self.r)]
        self.Matrix = [[0 for i in xrange(self.c)] for j in xrange(self.r)]

        for i in xrange(self.r):
            for j in xrange(self.c):
                self.Mat_entry[i][j] = Tk.Entry(midFrame, justify=Tk.CENTER,
                                                fg="orange", bg="black",
                                                width=6, font=("", 16))
                self.Mat_entry[i][j].insert(0, "0")

        for i in xrange(self.r):
            for j in xrange(self.c):
                self.Mat_entry[i][j].grid(row=i, column=j, padx=10, pady=10)

        # bottomFrame has the necessary Buttons
        bottomFrame = Tk.Frame(self.root, pady=50)
        bottomFrame.pack(side=Tk.TOP)

        self.resetBut = Tk.Button(bottomFrame, text="RESET", bg="#1f0b3b",
                                  fg="cyan", font=("Times New Roman", 16),
                                  command=self.resetAssignments)
        self.backBut = Tk.Button(bottomFrame, text="BACK", bg="#1f0b3b",
                                 fg="cyan", font=("Times New Roman", 16),
                                 command=self.restoreWindow)
        self.solveBut = Tk.Button(bottomFrame, text="SOLVE", bg="#1f0b3b",
                                  command=self.solveModel, fg="cyan",
                                  font=("Times New Roman", 16))

        self.resetBut.pack(side=Tk.LEFT, padx=50, pady=50)
        self.backBut.pack(side=Tk.LEFT, padx=50)
        self.solveBut.pack(side=Tk.RIGHT, padx=60)

    def restoreWindow(self):
        """restores the user assignment window when back is pressed"""
        if hasattr(self, "resultWindow"):
            self.resultWindow.destroy()
            for child in self.root.winfo_children():
                child.destroy()
            self.__init__(self.root)
        else:
            for child in self.root.winfo_children():
                child.pack_forget()
            self.root.minsize(width=550, height=300)
            self.root.title('HUNGARIAN ASSIGNMENT')
            self.topFrame.pack()
            self.midFrame.pack()
            self.bottomFrame.pack()

    def resetAssignments(self):
        """reset user assignments to zero"""
        for i in xrange(self.r):
            for j in xrange(self.c):
                self.Mat_entry[i][j].delete(0, Tk.END)
                self.Mat_entry[i][j].insert(0, '0')

    def solveModel(self):
        """Main stub that solves the MODEL
            Uses CLI module which has the necessary functions
            Store the results as well as the final result
        """
        allIntegersEntered = True
        for i in xrange(self.r):
            for j in xrange(self.c):
                if not (self.Mat_entry[i][j].get()).isdigit():
                    allIntegersEntered = False
                    break
                else:
                    self.Matrix[i][j] = int(self.Mat_entry[i][j].get())
            if not allIntegersEntered:
                break

        if not allIntegersEntered:
            tkMessageBox.showinfo("Error", 'Only integer values are allowed')
            self.resetAssignments()
        else:
            CLI._GUI_ROW = self.r
            CLI._GUI_COL = self.c
            CLI._GUI_M = self.Matrix
            # Capture output from the module
            with Capturing() as self.stepResults:
                CLI.main()
            self.resultOptionWindow()
            self.finalResult = CLI.finalResult
            self.stepResults = '\n'.join(self.stepResults)

    def resultOptionWindow(self, created=False):
        """User can either view final result or the entire steps"""

        if not created:
            self.resultWindow = Tk.Toplevel(self.root)
            self.resultWindow.resizable(False, False)

        self.resultWindow.minsize(width=550, height=400)
        self.resultWindow.title('RESULTS VIEWER')
        optMode = Tk.Label(
            self.resultWindow, text="Specify choice for the result",
            fg="dark red", bd=30, font=("Times New Roman", 20))
        optMode.pack()

        modeABut = Tk.Button(self.resultWindow, text="View Final Result",
                             fg="white", command=self.viewFinalResult,
                             bg="#6e054a", font=("Times New Roman", 16))
        modeBBut = Tk.Button(self.resultWindow, text="View steps", fg="white",
                             bg="#6e054a", command=self.viewIterationResult,
                             font=("Times New Roman", 16))
        backBut = Tk.Button(self.resultWindow, text="Modify / Back",
                            bg="#6e054a", command=self.resultWindow.destroy,
                            fg="white", font=("Times New Roman", 16))
        saveBut = Tk.Button(self.resultWindow, text="Save final", fg="white",
                            bg="#6e054a", command=self.saveResult,
                            font=("Times New Roman", 16))

        modeABut.pack(padx=10, pady=20)
        modeBBut.pack(padx=10, pady=30)
        saveBut.pack(padx=10, pady=30)
        backBut.pack(padx=10, pady=30)

    def saveResult(self):
        """Saves the result on a file specified by the user"""
        f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            # asksaveasfile return `None` if dialog closed with "cancel".
            return
        # starts from `1.0`, not `0.0`
        text2save = '\n'.join(self.stepResults.split(CLI.delimiter))
        f.write(text2save)
        f.close()

    def goBack(self, param):
        """ if param is false, simply clear current window
            else go back to some other window after clearing"""
        for child in self.resultWindow.winfo_children():
            child.destroy()
        if param:
            self.resultOptionWindow(True)

    def viewFinalResult(self):
        """View the final result of the assignment problem in a window"""

        self.goBack(False)
        self.resultWindow.minsize(width=450, height=400)
        self.resultWindow.title('Final Results')

        resVar = Tk.Label(
            self.resultWindow, text=self.finalResult, fg="blue", bg='white',
            font=("Times New Roman", 16))

        backBut = Tk.Button(self.resultWindow, text="BACK", bg='black',
                            fg="orange", font=("Times New Roman", 16),
                            command=lambda: self.goBack(True))
        resVar.pack(pady=30)
        backBut.pack(padx=10, pady=20)

    def viewIterationResult(self):
        """View the final result of the assignment problem in a Window"""

        def showNextStep(resVar, generator):
            try:
                curText = generator.next()
                resVar.config(text=curText)
            except StopIteration:
                resVar.config(text="\n Finished displaying result", fg='red',
                              bg='white', font=("Times New Roman", 16))
                self.goBack(True)

        self.goBack(False)
        self.resultWindow.minsize(width=450, height=400)
        self.resultWindow.title('Stepped Results')

        gen = iter(self.stepResults.split(CLI.delimiter))

        resVar = Tk.Label(
            self.resultWindow, text="\n Press Next to view steps\n\n",
            fg="blue", bg='white', font=("Times New Roman", 16))
        resVar.pack(pady=30)

        nextBut = Tk.Button(self.resultWindow, text="NEXT STEP", bg='black',
                            fg="orange", font=("Times New Roman", 16),
                            command=lambda: showNextStep(resVar, gen))
        backBut = Tk.Button(self.resultWindow, text="BACK", bg='black',
                            fg="orange", font=("Times New Roman", 16),
                            command=lambda: self.goBack(True))
        nextBut.pack(side=Tk.LEFT, padx=60, pady=20)
        backBut.pack(side=Tk.LEFT, padx=60, pady=20)


if __name__ == '__main__':
    root = Tk.Tk()
    hGui = Hungarian(root)
    root.mainloop()
    pass
