
class Model:
    def aceita_palavra(self, palavra):
        return palavra.startswith("00")


def carregar_palavras(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            palavras = [linha.strip() for linha in f if linha.strip()]
            return palavras
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    except Exception as e:
        raise IOError(f"Erro ao ler o arquivo '{filepath}': {e}")
