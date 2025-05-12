# tela_inicial.py
import tkinter as tk

class TelaInicial:
    def __init__(self, master, ir_para_cadastro):
        self.frame = tk.Frame(master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Bem-vindo ao sistema!")
        self.label.pack(pady=10)

        self.botao_aluno = tk.Button(self.frame, text="Cadastrar Aluno", command=lambda: ir_para_cadastro('aluno'))
        self.botao_aluno.pack()

        self.botao_livro = tk.Button(self.frame, text="Cadastrar Livro", command=lambda: ir_para_cadastro('livro'))
        self.botao_livro.pack()

        self.botao_produto = tk.Button(self.frame, text="Cadastrar Produto", command=lambda: ir_para_cadastro('produto'))
        self.botao_produto.pack()
