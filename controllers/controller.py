from models.model import Model, carregar_palavras

class Controller:
    
    def __init__(self, model, view):
        self.model = model  
        self.view = view    

    def processar_arquivos_gui(self, filepaths):
        if not filepaths:
            self.view.exibir_erro("Nenhum arquivo foi fornecido.")
            return

        for path in filepaths:
            try:
                palavras = carregar_palavras(path)
                if not palavras:
                    self.view.exibir_erro(f"O arquivo '{path}' está vazio ou não contém palavras.")
                    continue
                
                self.view.exibir_cabecalho_arquivo(path)
                for palavra in palavras:
                    resultado = self.model.aceita_palavra(palavra)
                    self.view.exibir_resultado(palavra, resultado)

            except Exception as e:
                self.view.exibir_erro(str(e))