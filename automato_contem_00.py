def validar(palavra: str) -> bool:
    if not palavra:
        return False

    estado_atual = "Q0"

    for simbolo in palavra:
        if simbolo not in ('0', '1'):
            return False

        if estado_atual == "Q0":
            if simbolo == '0':
                estado_atual = "Q1"

        elif estado_atual == "Q1":
            if simbolo == '0':
                estado_atual = "Q2"
            else:
                estado_atual = "Q0"

        elif estado_atual == "Q2":
            pass

    return estado_atual == "Q2"


def carregar_palavras(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            palavras = [linha.strip() for linha in f if linha.strip()]
            return palavras
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    except Exception as e:
        raise IOError(f"Erro ao ler o arquivo '{filepath}': {e}")