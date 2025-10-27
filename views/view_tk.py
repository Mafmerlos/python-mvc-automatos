import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analisador de Palavras do Autômato")
        self.geometry("600x450")

        self.controller = None
        self.filepaths = []

        frame_botoes = tk.Frame(self)
        frame_botoes.pack(pady=15)

        self.btn_selecionar = tk.Button(
            frame_botoes, 
            text="1. Selecionar Arquivos (.txt)", 
            command=self.solicitar_arquivos_palavras,
            font=('Arial', 10)
        )
        self.btn_selecionar.pack(side=tk.LEFT, padx=10)

        self.btn_processar = tk.Button(
            frame_botoes, 
            text="2. Processar Palavras", 
            command=self.iniciar_processamento,
            font=('Arial', 10, 'bold')
        )
        self.btn_processar.pack(side=tk.LEFT, padx=10)

        label_resultados = tk.Label(self, text="Resultados:", font=('Arial', 12))
        label_resultados.pack(pady=(5, 5))

        self.txt_resultados = scrolledtext.ScrolledText(
            self, 
            wrap=tk.WORD, 
            height=20, 
            width=70,
            font=('Courier New', 10)
        )
        self.txt_resultados.pack(pady=10, padx=10, fill="both", expand=True)

        self.txt_resultados.tag_config('cabecalho', foreground='#00008B', font=('Arial', 10, 'bold', 'underline'))
        self.txt_resultados.tag_config('aceita', foreground='green')
        self.txt_resultados.tag_config('rejeita', foreground='red')
        self.txt_resultados.tag_config('erro', foreground='#FF8C00', font=('Arial', 10, 'bold'))
        self.txt_resultados.tag_config('info', foreground='gray')

    def set_controller(self, controller):
        self.controller = controller

    def solicitar_arquivos_palavras(self):
        self.filepaths = filedialog.askopenfilenames(
            title="Selecione os arquivos de palavras",
            filetypes=[("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        
        if self.filepaths:
            self.limpar_resultados()
            self.txt_resultados.insert(tk.END, f"{len(self.filepaths)} arquivo(s) selecionado(s):\n", 'info')
            for path in self.filepaths:
                self.txt_resultados.insert(tk.END, f"  - {path}\n", 'info')
            self.txt_resultados.insert(tk.END, "\nClique em '2. Processar' para analisar.\n", 'info')
        else:
            messagebox.showinfo("Informação", "Nenhum arquivo selecionado.")

    def iniciar_processamento(self):
        if not self.controller:
            self.exibir_erro("O Controller não foi configurado.")
            return
        
        if not self.filepaths:
            self.exibir_erro("Nenhum arquivo selecionado. Clique em '1. Selecionar' primeiro.")
            return
        
        self.limpar_resultados()
        
        self.controller.processar_arquivos_gui(self.filepaths)

    def limpar_resultados(self):
        self.txt_resultados.delete('1.0', tk.END)

    def exibir_cabecalho_arquivo(self, nome_arquivo):
        self.txt_resultados.insert(tk.END, f"\n--- Testando: '{nome_arquivo}' ---\n", 'cabecalho')

    def exibir_resultado(self, palavra, resultado):
        res_str = "ACEITA"
        tag = 'aceita'
        if not resultado:
            res_str = "REJEITA"
            tag = 'rejeita'
            
        palavra_display = palavra if palavra else '""'
        
        self.txt_resultados.insert(tk.END, f"  Palavra: {palavra_display:<40} -> {res_str}\n", tag)
        self.update_idletasks() 

    def exibir_erro(self, mensagem):
        self.txt_resultados.insert(tk.END, f"[ERRO]: {mensagem}\n", 'erro')
        if "Arquivo não encontrado" in mensagem or "Nenhum arquivo" in mensagem:
             messagebox.showerror("Erro de Arquivo", mensagem)

    def main(self):
        self.mainloop()