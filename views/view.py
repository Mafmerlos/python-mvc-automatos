class View:
    def solicitar_arquivos_palavras(self):
        print("Digite os caminhos dos arquivos .txt (com palavras), separados por vírgula:")
        entrada = input("Arquivos: ")
        return [caminho.strip() for caminho in entrada.split(',') if caminho.strip()]

    def exibir_cabecalho_arquivo(self, nome_arquivo):
        print(f"\n--- Testando palavras do arquivo: '{nome_arquivo}' ---")

    def exibir_resultado(self, palavra, resultado):
        res_str = "ACEITA" if resultado else "REJEITA"
        print(f"  Palavra: \"{palavra}\" -> {res_str}")

    def exibir_erro(self, mensagem):
        print(f"[ERRO]: {mensagem}")