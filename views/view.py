import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkFont


class View:

    BG_COLOR = "#ffffff"
    BTN_COLOR = "#007bff"
    BTN_HIST_COLOR = "#6c757d"
    BTN_DANGER_COLOR = "#dc3545"
    BTN_INFO_COLOR = "#17a2b8"
    BTN_FG_COLOR = "#ffffff"
    LABEL_COLOR = "#212121"
    TEXT_BG_COLOR = "#ffffff"
    BORDER_COLOR = "#d0d0d0"

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Analisador de Palavras do Autômato")
        self.window.geometry("960x520")
        self.window.configure(bg=self.BG_COLOR)
        self.window.resizable(False, False)

        self.FONT_BOLD = tkFont.Font(family="Segoe UI", size=12, weight="bold")
        self.FONT_BUTTON = tkFont.Font(
            family="Segoe UI", size=10, weight="bold")
        self.FONT_TEXT = tkFont.Font(family="Consolas", size=10)
        self.FONT_LABEL = tkFont.Font(family="Segoe UI", size=11)

        frame_selector = tk.Frame(self.window, bg=self.BG_COLOR)
        frame_selector.pack(pady=(25, 15))

        lbl_selector = tk.Label(
            frame_selector,
            text="Selecione o Autômato:",
            font=self.FONT_LABEL,
            bg=self.BG_COLOR,
            fg=self.LABEL_COLOR
        )
        lbl_selector.pack(side="left", padx=(0, 10))

        self.automaton_options = [
            "Inicia com 00",
            "Contém 00",
            "Termina com 00",
            "Inicia com 0 termina com 1",
            "Termina com 01",
            "Inicia com 11"
        ]

        style = ttk.Style()
        style.configure('TCombobox',
                        fieldbackground=self.TEXT_BG_COLOR,
                        foreground=self.LABEL_COLOR,
                        selectbackground=self.TEXT_BG_COLOR,
                        selectforeground=self.LABEL_COLOR,
                        borderwidth=0,
                        font=self.FONT_LABEL)
        style.map('TCombobox',
                  fieldbackground=[('readonly', self.TEXT_BG_COLOR)],
                  selectbackground=[('readonly', self.TEXT_BG_COLOR)],
                  selectforeground=[('readonly', self.LABEL_COLOR)])

        self.automaton_selector = ttk.Combobox(
            frame_selector,
            values=self.automaton_options,
            state="readonly",
            font=self.FONT_LABEL,
            width=25,
            style='TCombobox'
        )
        self.automaton_selector.current(0)
        self.automaton_selector.pack(side="left")

        frame_botoes = tk.Frame(self.window, bg=self.BG_COLOR)
        frame_botoes.pack(pady=15)

        self.btn_selecionar = tk.Button(
            frame_botoes,
            text="1. Importar Arquivos .txt",
            font=self.FONT_BUTTON,
            bg=self.BTN_COLOR,
            fg=self.BTN_FG_COLOR,
            relief="flat",
            padx=15,
            pady=8,
            activebackground="#0056b3",
            activeforeground="#ffffff",
            borderwidth=0
        )
        self.btn_selecionar.grid(row=0, column=0, padx=10)

        self.btn_processar = tk.Button(
            frame_botoes,
            text="2. Processar (do BD)",
            font=self.FONT_BUTTON,
            bg=self.BTN_COLOR,
            fg=self.BTN_FG_COLOR,
            relief="flat",
            padx=15,
            pady=8,
            activebackground="#0056b3",
            activeforeground="#ffffff",
            borderwidth=0
        )
        self.btn_processar.grid(row=0, column=1, padx=10)

        self.btn_historico = tk.Button(
            frame_botoes,
            text="3. Ver Histórico",
            font=self.FONT_BUTTON,
            bg=self.BTN_HIST_COLOR,
            fg=self.BTN_FG_COLOR,
            relief="flat",
            padx=15,
            pady=8,
            activebackground="#5a6268",
            activeforeground="#ffffff",
            borderwidth=0
        )
        self.btn_historico.grid(row=0, column=2, padx=10)

        self.btn_resetar = tk.Button(
            frame_botoes,
            text="4. Resetar BD",
            font=self.FONT_BUTTON,
            bg=self.BTN_DANGER_COLOR,
            fg=self.BTN_FG_COLOR,
            relief="flat",
            padx=15,
            pady=8,
            activebackground="#a71d2a",
            activeforeground="#ffffff",
            borderwidth=0
        )
        self.btn_resetar.grid(row=0, column=3, padx=10)

        self.btn_mostrar_codigo = tk.Button(
            frame_botoes,
            text="5. Ver Código",
            font=self.FONT_BUTTON,
            bg=self.BTN_INFO_COLOR,
            fg=self.BTN_FG_COLOR,
            relief="flat",
            padx=15,
            pady=8,
            activebackground="#117a8b",
            activeforeground="#ffffff",
            borderwidth=0
        )
        self.btn_mostrar_codigo.grid(row=0, column=4, padx=10)

        frame_resultados = tk.Frame(self.window, bg=self.BG_COLOR)
        frame_resultados.pack(padx=25, pady=(0, 25), fill="both", expand=True)

        lbl_resultados = tk.Label(
            frame_resultados,
            text="Resultados:",
            font=self.FONT_BOLD,
            bg=self.BG_COLOR,
            fg=self.LABEL_COLOR
        )
        lbl_resultados.pack(anchor="w", pady=(0, 10))

        text_frame = tk.Frame(
            frame_resultados,
            bg=self.BORDER_COLOR,
            borderwidth=1,
            relief="solid"
        )
        text_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(
            text_frame, relief="flat", troughcolor=self.BG_COLOR)
        scrollbar.pack(side="right", fill="y")

        self.txt_resultados = tk.Text(
            text_frame,
            height=15,
            font=self.FONT_TEXT,
            bg=self.TEXT_BG_COLOR,
            fg=self.LABEL_COLOR,
            relief="flat",
            borderwidth=0,
            yscrollcommand=scrollbar.set,
            state="disabled",
            padx=5,
            pady=5
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

    def exibir_bloco_de_texto(self, texto):
        self.txt_resultados.config(state="normal")
        self.txt_resultados.insert(tk.END, texto + "\n")
        self.txt_resultados.config(state="disabled")
        self.txt_resultados.see(tk.END)

    def exibir_resultado(self, palavra, resultado):
        res_str = "ACEITA" if resultado else "REJEITA"
        self._escrever_no_log(f'   Palavra: "{palavra}" -> {res_str}')

    def exibir_cabecalho_arquivo(self, nome_arquivo):
        self.txt_resultados.config(state="normal")
        self.txt_resultados.insert(tk.END, f"\n--- {nome_arquivo} ---" + "\n")
        self.txt_resultados.config(state="disabled")
        self.txt_resultados.see(tk.END)

    def exibir_erro(self, mensagem):
        self._escrever_no_log(f"[ERRO]: {mensagem}")

    def limpar_resultados(self):
        self.txt_resultados.config(state="normal")
        self.txt_resultados.delete("1.0", tk.END)
        self.txt_resultados.config(state="disabled")

    def exibir_linha_historico(self, data, automato, palavra, resultado):
        self.txt_resultados.config(state="normal")
        self.txt_resultados.insert(
            tk.END,
            f"[{data}] ({automato}) - Palavra: \"{palavra}\" -> {resultado}\n"
        )
        self.txt_resultados.config(state="disabled")
        self.txt_resultados.see(tk.END)

    def confirmar_reset(self) -> bool:
        return messagebox.askyesno(
            title="Confirmar Reset",
            message="ATENÇÃO!\n\nIsso apagará permanentemente TODO o histórico e TODOS os arquivos importados.\n\nEsta ação não pode ser desfeita.\n\nDeseja continuar?"
        )
