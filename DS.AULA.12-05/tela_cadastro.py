# tela_cadastro.py
import tkinter as tk
from aluno import Aluno
from livro import Livro
from produto import Produto
from tkinter import messagebox

class TelaCadastro:
    def __init__(self, master, voltar_callback, tipo):
        self.tipo = tipo
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text=f"Cadastro de {self.tipo.capitalize()}")
        self.label.grid(row=0, column=1)

        # Campos de entrada de dados
        if self.tipo == 'aluno':
            self._criar_campos_aluno()
        elif self.tipo == 'livro':
            self._criar_campos_livro()
        elif self.tipo == 'produto':
            self._criar_campos_produto()

        self.botao_voltar = tk.Button(self.frame, text="Voltar", command=voltar_callback)
        self.botao_voltar.grid(row=4, column=1)

        self.lista_label = tk.Label(self.frame, text="")
        self.lista_label.grid(row=5, column=0, columnspan=2)

        self.lista = []  # Lista que vai armazenar os objetos cadastrados

    def _criar_campos_aluno(self):
        tk.Label(self.frame, text="Nome:").grid(row=1, column=0)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Idade:").grid(row=2, column=0)
        self.idade_entry = tk.Entry(self.frame)
        self.idade_entry.grid(row=2, column=1)

        self.botao_cadastrar = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar_aluno)
        self.botao_cadastrar.grid(row=3, column=1)

    def _criar_campos_livro(self):
        tk.Label(self.frame, text="Título:").grid(row=1, column=0)
        self.titulo_entry = tk.Entry(self.frame)
        self.titulo_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Autor:").grid(row=2, column=0)
        self.autor_entry = tk.Entry(self.frame)
        self.autor_entry.grid(row=2, column=1)

        self.botao_cadastrar = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar_livro)
        self.botao_cadastrar.grid(row=3, column=1)

    def _criar_campos_produto(self):
        tk.Label(self.frame, text="Nome do Produto:").grid(row=1, column=0)
        self.nome_produto_entry = tk.Entry(self.frame)
        self.nome_produto_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Preço:").grid(row=2, column=0)
        self.preco_entry = tk.Entry(self.frame)
        self.preco_entry.grid(row=2, column=1)

        self.botao_cadastrar = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar_produto)
        self.botao_cadastrar.grid(row=3, column=1)

    def cadastrar_aluno(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        if nome and idade.isdigit():
            aluno = Aluno(nome, int(idade))
            self.lista.append(aluno)
            self.nome_entry.delete(0, tk.END)
            self.idade_entry.delete(0, tk.END)
            self.exibir_lista()
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

    def cadastrar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        if titulo and autor:
            livro = Livro(titulo, autor)
            self.lista.append(livro)
            self.titulo_entry.delete(0, tk.END)
            self.autor_entry.delete(0, tk.END)
            self.exibir_lista()
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

    def cadastrar_produto(self):
        nome_produto = self.nome_produto_entry.get()
        preco = self.preco_entry.get()
        if nome_produto and preco.replace('.', '', 1).isdigit():
            produto = Produto(nome_produto, float(preco))
            self.lista.append(produto)
            self.nome_produto_entry.delete(0, tk.END)
            self.preco_entry.delete(0, tk.END)
            self.exibir_lista()
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

    def exibir_lista(self):
        texto = "\n".join(str(item) for item in self.lista)
        self.lista_label.config(text=texto)
