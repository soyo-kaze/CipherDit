import crypto as c
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class CipherDit:
    def __init__(self):
        self.op = False
        pass

    def crypt(self, call):
        word = self.tex.get("1.0", "end-1c")
        key = self.password.get()

        # --------- Path specifier --------------

        F_name = self.file_name.get()

        if self.file_name.get() == " FileName" or self.file_name.get() == "":
            F_name = "Un_dit.txt"
        if self.dir.get() == " Path" or self.dir.get() == "":
            self.path = F_name
        else:
            self.path = self.dir.get() + "/" + F_name

        # ---------------------------------------

        if self.password.get() == " Password" or self.password.get() == "":
            messagebox.showwarning("PASSWORD ERROR", "ERROR 404: PASSWORD NOT FOUND!!")
        elif len(self.password.get()) <= 3:
            messagebox.showwarning("PASSWORD ERROR", "PASSWORD IS TOO SHORT. SHOULD BE ATLEAST 4 LETTERS LONG!!")
        else:
            self.box.destroy()
            if call == "enc":
                enc = c.encrypto(word, key)
                messagebox.showinfo("COMPLETED", "DONE ENCRYPTION!!")
                self.tex.delete(1.0,"end")
            elif call == "dec":
                enc = c.decrypto(word, key)
                messagebox.showinfo("COMPLETED", "DONE DECRYPTION!!")
                self.tex.delete(1.0,"end")

            # ---------- save encryption/decryption to path -------------
            file = open(self.path, "w")
            file.write(enc)
            file.close()
            # --------------------------------------------------

        print(self.path)

    def direct(self):
        self.file_direct = filedialog.askdirectory(initialdir="/", title="Select Path")
        self.dir.delete(0, "end")
        self.dir.insert(0, self.file_direct)
        self.dir.config(fg="black", bg="grey")

    def crypt_box(self,call):
        self.box = Tk()
        self.box.iconbitmap(r'.\cipherdit_logo.ico')
        if len(self.tex.get(1.0, "end-1c")) == 0:
            self.box.destroy()
            if call == "enc":
                messagebox.showwarning("ENCRYPTION ERROR", "NOTHING TO ENCRYPT")
            elif call =="dec":
                messagebox.showwarning("DECRYPTION ERROR", "NOTHING TO DECRYPT")
        else:
            frame = Frame(self.box)
            frame.pack()
            frame1 = Frame(frame)
            frame1.pack(side=LEFT)
            frame2 = Frame(frame)
            frame2.pack(side=RIGHT)
            frame3 = Frame(self.box)
            frame3.pack(side=LEFT)
            frame4 = Frame(self.box)
            frame4.pack(side=BOTTOM)

            self.password = Entry(frame3, width=40)  # key
            self.password.insert(0, " Password")
            self.password.config(fg="grey")

            self.password.pack(side=LEFT, padx=10, pady=10)

            self.password.bind('<FocusIn>', self.password_onclick)
            self.password.bind('<FocusOut>', self.password_watermark)

            self.dir = Entry(frame1, width=40)   # filepath
            self.dir.insert(0, " Path")
            self.dir.config(fg="grey")

            self.dir.bind('<FocusIn>', self.dir_onclick)
            self.dir.bind('<FocusOut>', self.dir_watermark)

            self.dir.pack(pady=10, padx=10)

            self.file_name = Entry(frame1, width=40)  # filename
            self.file_name.insert(0, " FileName")
            self.file_name.config(fg="grey")

            self.file_name.bind('<FocusIn>', self.filename_onclick)
            self.file_name.bind('<FocusOut>', self.filename_watermark)

            self.file_name.pack(pady=10, padx=10)

            self.directory = Button(frame2, text="Browse", width=10, font="ethnocentricrg-regular 10", command=lambda: self.direct())
            self.directory.pack(padx=10, pady=10)

            if call == "enc":
                self.box.title("ENCRYPT")
                yes = Button(frame4, text="OK", width=10, font="ethnocentricrg-regular 10", command=lambda: self.crypt(call))
                yes.pack(side=BOTTOM, pady=10, padx=10)
            elif call == "dec":
                self.box.title("DECRYPT")
                yes = Button(frame4, text="OK", width=10, font="ethnocentricrg-regular 10", command=lambda: self.crypt(call))
                yes.pack(side=BOTTOM, pady=10, padx=10)

            self.box.mainloop()

    def password_onclick(self, x):
        if self.password.get() == " Password":
            self.password.delete(0, 'end')
            self.password.insert(0, "")
            self.password.config(bg="grey", fg="black", show="*")

    def password_watermark(self, y):
        if self.password.get() == "" or self.password.get() == " ":
            self.password.delete(0, "end")
            self.password.insert(0, " Password")
            self.password.config(bg="white", fg="grey", show="")

    def dir_watermark(self, y):
        if self.dir.get() == "" or self.dir.get() == " ":
            self.dir.delete(0, "end")
            self.dir.insert(0, " Path")
            self.dir.config(bg="white", fg="grey")

    def dir_onclick(self, y):
        if self.dir.get() == " Path":
            self.dir.delete(0, "end")
            self.dir.insert(0, "")
            self.dir.config(bg="grey", fg="black")

    def filename_watermark(self, y):
        if self.file_name.get() == "" or self.file_name.get() == " ":
            self.file_name.delete(0, "end")
            self.file_name.insert(0, " FileName")
            self.file_name.config(bg="white", fg="grey")

    def filename_onclick(self, y):
        if self.file_name.get() == " FileName":
            self.file_name.delete(0, "end")
            self.file_name.insert(0, "")
            self.file_name.config(bg="grey", fg="black")

    def win_open(self):
        self.op = True
        filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))  # file browser

        file = open(filename, "r")
        self.filedata = file.read()
        file.close()

        self.window.destroy()
        self.win()

    def win_new(self):
        self.window.destroy()
        self.win()

    def win(self):
        self.window = Tk()
        self.window.iconbitmap(r'.\cipherdit_logo.ico')
        self.window.title("CipherDit")

        scroll = Scrollbar(self.window)
        scroll.pack(side=RIGHT, fill=Y)

        var_men = Menu(self.window)
        self.window.config(menu=var_men)

        var_name = Menu(var_men, tearoff=False)
        var_name1 = Menu(var_men, tearoff=False)

        var_men.add_cascade(label="File", menu=var_name)
        var_men.add_cascade(label="Help", menu=var_name1)

        var_name.add_command(label="New", command=lambda: self.win_new())
        var_name.add_command(label="Open             ", command=lambda: self.win_open())
        var_name.add_command(label="Close", command=self.window.destroy)

        if self.op:
            self.tex = Text(self.window)
            self.tex.insert(1.0, self.filedata)
            self.tex.pack(expand=True, fill='both')
            self.op = False
        else:
            self.tex = Text(self.window)
            self.tex.pack(expand=True, fill='both')
            self.tex.config(bg="lightgrey")

        scroll.config(command=self.tex.yview)
        self.tex.config(yscrollcommand=scroll.set)

        frame_c = Frame(self.window, height=5).pack()
        frame_b = Frame(self.window, height=7).pack(side=BOTTOM)

        button = Button(frame_b, text="Encrypt", font="ethnocentricrg-regular 10", command=lambda: self.crypt_box("enc"))
        button.pack(side=LEFT, padx=10)
        button1 = Button(frame_b, text="Decrypt", font="ethnocentricrg-regular 10", command=lambda: self.crypt_box("dec"))
        button1.pack(side=LEFT, padx=10)

        self.window.mainloop()


ciper = CipherDit()
ciper.win()

