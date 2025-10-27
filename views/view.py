import tkinter as tk
from tkinter import font as tkFont

class View:
    
    BG_COLOR = "#f0f0f0"
    BTN_COLOR = "#007bff"
    BTN_FG_COLOR = "#ffffff"
    LABEL_COLOR = "#333333"
    TEXT_BG_COLOR = "#ffffff"
    BORDER_COLOR = "#cccccc"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Analisador de Palavras do Autômato")
        self.window.geometry("500x450")
        self.window.configure(bg=self.BG_COLOR)
        self.window.resizable(False, False)

        FONT_BOLD = tkFont.Font(family="Arial", size=12, weight="bold")
        FONT_BUTTON = tkFont.Font(family="Arial", size=10, weight="bold")
        FONT_TEXT = tkFont.Font(family="Courier New", size=10)

        frame_botoes = tk.Frame(self.window, bg=self.BG_COLOR)
        frame_botoes.pack(pady=20)

        self.btn_selecionar = tk.Button(
            frame_botoes,
            text="1. Selecionar Arquivos (txt)",
            font=FONT_BUTTON,
            bg=self.BTN_COLOR,
            fg=self.BTN_FG_COLOR,
            relief="flat",
            padx=15,
            pady=8,
            activebackground="#0056b3",
            activeforeground="#ffffff"
        )
        self.btn_selecionar.grid(row=0, column=0, padx=10)

        self.btn_processar = tk.Button(
            frame_botoes,
            text="2. Processar Palavras",
            font=FONT_BUTTON,
            bg=self.BTN_COLOR,
            fg=self.BTN_FG_COLOR,
            relief="flat",
            padx=15,
            pady=8,
            activebackground="#0056b3",
            activeforeground="#ffffff"
        )
        self.btn_processar.grid(row=0, column=1, padx=10)

        frame_resultados = tk.Frame(self.window, bg=self.BG_COLOR)
        frame_resultados.pack(padx=20, pady=(0, 20), fill="both", expand=True)

        lbl_resultados = tk.Label(
            frame_resultados,
            text="Resultados:",
            font=FONT_BOLD,
            bg=self.BG_COLOR,
            fg=self.LABEL_COLOR
        )
        lbl_resultados.pack(anchor="w", pady=(0, 5))

        text_frame = tk.Frame(
            frame_resultados,
            bg=self.BORDER_COLOR,
            borderwidth=1,
            relief="solid"
        )
        text_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")

        self.txt_resultados = tk.Text(
            text_frame,
            height=15,
            font=FONT_TEXT,
            bg=self.TEXT_BG_COLOR,
            fg=self.LABEL_COLOR,
            relief="flat",
            borderwidth=0,
            yscrollcommand=scrollbar.set,
            state="disabled"
        )
        self.txt_resultados.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.txt_resultados.yview)

    def iniciar_loop(self):
        self.window.mainloop()

    def _escrever_no_log(self, mensagem):
        self.txt_resultados.config(state="normal")
        self.txt_resultados.insert(tk.END, mensagem + "\n")
        self.txt_resultados.config(state="disabled")
        self.txt_resultados.see(tk.END)

    def exibir_resultado(self, palavra, resultado):
        res_str = "ACEITA" if resultado else "REJEITA"
        self._escrever_no_log(f'   Palavra: "{palavra}" -> {res_str}')

    def exibir_cabecalho_arquivo(self, nome_arquivo):
        self._escrever_no_log(f"\n--- Testando palavras do arquivo: '{nome_arquivo}' ---")

    def exibir_erro(self, mensagem):
        self._escrever_no_log(f"[ERRO]: {mensagem}")

    def limpar_resultados(self):
        self.txt_resultados.config(state="normal")
        self.txt_resultados.delete("1.0", tk.END)
        self.txt_resultados.config(state="disabled")