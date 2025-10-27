from tkinter import filedialog
from models.model import Model, carregar_palavras
from views.view import View
import os

class Controller:
    
    def __init__(self, model, view):
        self.model = model  
        self.view = view
        self.filepaths = []
        
        self.view.btn_selecionar['command'] = self.selecionar_arquivos
        self.view.btn_processar['command'] = self.processar_palavras

    def selecionar_arquivos(self):
        self.filepaths = filedialog.askopenfilenames(
            title="Selecione os arquivos .txt",
            filetypes=(("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*"))
        )
        
        if self.filepaths:
            self.view.limpar_resultados()
            self.view.exibir_cabecalho_arquivo(f"{len(self.filepaths)} arquivo(s) selecionado(s).")
        else:
            self.view.exibir_erro("Nenhum arquivo selecionado.")

    def processar_palavras(self):
        if not self.filepaths:
            self.view.exibir_erro("Nenhum arquivo foi selecionado. Clique em '1. Selecionar Arquivos' primeiro.")
            return

        self.view.limpar_resultados()
        
        for path in self.filepaths:
            try:
                palavras = carregar_palavras(path)
                if not palavras:
                    self.view.exibir_erro(f"O arquivo '{os.path.basename(path)}' está vazio.")
                    continue
                
                self.view.exibir_cabecalho_arquivo(os.path.basename(path))
                for palavra in palavras:
                    resultado = self.model.aceita_palavra(palavra)
                    self.view.exibir_resultado(palavra, resultado)

            except Exception as e:
                self.view.exibir_erro(str(e))