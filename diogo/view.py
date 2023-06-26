from tkinter import *
from tkinter import ttk
import sys
from controller import Controller
from model import Model

class View:
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.controller = Controller(self.model, self)
        self.root.geometry("800x600")
        self.root.configure(bg="#bcc2c1")
        self.root.title("Sistema de cadastro de Fornecedor")
        self.root.resizable(False, False)
        self.frames()
        self.nametele()
        self.type_fav()
        self.button()
        self.arvore()
        self.lista_vil()
        self.root.bind("<Escape>", self.close)
        self.root.mainloop()

    def frames(self):
        self.supeior = Frame(self.root, bd=4, bg="#1cfde2")
        self.supeior.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.inferior = Frame(self.root, bd=4, bg="#1cfde2")
        self.inferior.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def nametele(self):
        name = Label(self.supeior, text="Nome:", bg="#1cfde2", fg="black", font=("Calibri", 11, "bold"))
        name.place(relx=0, rely=0.07)
        self.nameEntra = Entry(self.supeior, bd=2)
        self.nameEntra.place(relx=0.1, rely=0.07, relwidth=0.5, relheight=0.11)

        phone = Label(self.supeior, text="Telefone:", bg="#1cfde2", fg="black", font=("Calibri", 11, "bold"))
        phone.place(relx=0, rely=0.3)
        self.phoneEntra = Entry(self.supeior, bd=2)
        self.phoneEntra.place(relx=0.1, rely=0.3, relwidth=0.5, relheight=0.11)

        cnpj_label = Label(self.supeior, text="CNPJ:", bg="#1cfde2", fg="black", font=("Calibri", 11, "bold"))
        cnpj_label.place(relx=0, rely=0.5)
        self.cnpj_entry = Entry(self.supeior, bd=2)
        self.cnpj_entry.place(relx=0.1, rely=0.5, relwidth=0.5, relheight=0.11)

        id_label = Label(self.supeior, text="ID:", bg="#1cfde2", fg="black", font=("Calibri", 11, "bold"))
        id_label.place(relx=0.3, rely=0.5, relheight=0.5)
        self.idEntra = Entry(self.supeior, bd=2)
        self.idEntra.place(relx=0.33, rely=0.7, relwidth=0.1)

    def type_fav(self):
        Type = Label(self.supeior, text="Tipo", bg="#1cfde2", fg="black", font=("Calibri", 11, "bold"))
        Type.place(rely=0.9)
        self.radio = StringVar()
        self.op1 = Radiobutton(self.supeior, text="Monopolista", variable=self.radio, value="Monopolista", bg="#1cfde2",
                               fg="black", font=("Calibri", 10, "bold"))
        self.op1.place(relx=0.1, rely=0.9)
        self.op2 = Radiobutton(self.supeior, text="Habitual", variable=self.radio, value="Habitual", bg="#1cfde2",
                               fg="black", font=("Calibri", 10, "bold"))
        self.op2.place(relx=0.3, rely=0.9)
        self.op3 = Radiobutton(self.supeior, text="Especial", variable=self.radio, value="Especial", bg="#1cfde2",
                               fg="black", font=("Calibri", 10, "bold"))
        self.op3.place(relx=0.5, rely=0.9)

        fav = Label(self.supeior, text="fav", bg="#1cfde2", fg="black", font=("Calibri", 11, "bold"))
        fav.place(rely=0.7)
        self.checkbutt = BooleanVar()
        self.favocheck = Checkbutton(self.supeior, variable=self.checkbutt, bg="#1cfde2", fg="black")
        self.favocheck.place(relx=0.1, rely=0.7)

    def button(self):
        new = Button(self.supeior, text="Novo", bg="#3d8592", fg="black",
                     bd=3, font=("Calibri", 11, "bold"), command=self.add_pessoa)
        new.place(relx=0.65, rely=0.07, relwidth=0.15, relheight=0.12)

        search = Button(self.supeior, text="Buscar", bg="#3d8592", fg="black",
                        bd=3, font=("Calibri", 11, "bold"), command=self.search)
        search.place(relx=0.83, rely=0.07, relwidth=0.15, relheight=0.12)

        alt = Button(self.supeior, text="Alterar", bg="#3d8592", fg="black",
                     bd=3, font=("Calibri", 11, "bold"), command=self.alt)
        alt.place(relx=0.65, rely=0.3, relwidth=0.15, relheight=0.12)

        delete = Button(self.supeior, text="Excluir", bg="#EF3636", fg="black",
                        bd=3, font=("Calibri", 11, "bold"), command=self.delete)
        delete.place(relx=0.83, rely=0.3, relwidth=0.15, relheight=0.12)

        clean = Button(self.supeior, text="Limpar", bg="#EF3636", fg="black",
                       bd=3, font=("Calibri", 11, "bold"), command=self.clear)
        clean.place(relx=0.74, rely=0.6, relwidth=0.15, relheight=0.12)

    def arvore(self):
        self.treeview = ttk.Treeview(self.inferior, height=3,
                                     columns=("colu1", "colu2", "colu3", "colu4", "colu5", "colu6", "colu7"))
        self.treeview.heading("#0", text="")
        self.treeview.heading("#1", text="ID")
        self.treeview.heading("#2", text="Nome")
        self.treeview.heading("#3", text="Telefone")
        self.treeview.heading("#4", text="CNPJ")
        self.treeview.heading("#5", text="Tipo")
        self.treeview.heading("#6", text="fav")

        self.treeview.column("#0", width=5)
        self.treeview.column("#1", width=20)
        self.treeview.column("#2", width=200)
        self.treeview.column("#3", width=125)
        self.treeview.column("#4", width=125)
        self.treeview.column("#5", width=125)
        self.treeview.column("#6", width=125)
        self.treeview.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.rolagem = Scrollbar(self.inferior, orient="vertical")
        self.treeview.configure(yscroll=self.rolagem.set)
        self.rolagem.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.treeview.bind("<Double-1>", self.clique)

    def exibir_itens(self, items):
        for item in items:
            if len(item) >= 7:
                self.treeview.insert("", "end", text="",
                                     values=(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
            else:
                print("Tupla com tamanho insuficiente:", item)

    def clique(self, event):
        selected_item = self.treeview.selection()
        if selected_item:
            item_id = self.treeview.item(selected_item)['values'][0]
            self.controller.get_item_by_id(item_id)

    def lista_vil(self):
        self.controller.lista_vil()

    def close(self, event=None):
        sys.exit()

    def clear(self):
        self.nameEntra.delete(0, END)
        self.phoneEntra.delete(0, END)
        self.cnpj_entry.delete(0, END)
        self.radio.set("")
        self.checkbutt.set(False)

    def add_pessoa(self):
        self.controller.add_pessoa(self.nameEntra.get(), self.phoneEntra.get(), self.cnpj_entry.get(),
                                   self.radio.get(), self.checkbutt.get())

    def delete(self):
        self.controller.delete_pessoa()

    def alt(self):
        self.controller.alt_pessoa()

    def search(self):
        self.controller.search_pessoa()