
class Model:
    def aceita_palavra(self, palavra):
        if len(palavra) < 2:
            return False
        
        if palavra[0] == '0':
            if palavra[1] == '0':
                return True
            else:
                return False
        else:
            return False

def carregar_palavras(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            palavras = [linha.strip() for linha in f if linha.strip()]
            return palavras
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    except Exception as e:
        raise IOError(f"Erro ao ler o arquivo '{filepath}': {e}")

