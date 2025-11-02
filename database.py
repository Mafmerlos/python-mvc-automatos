import sqlite3
import os
import datetime

class DatabaseManager:

    def __init__(self, db_name="automato_mestre.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self._criar_tabelas()

    def _criar_tabelas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS arquivos_fonte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_arquivo TEXT NOT NULL UNIQUE,
                data_importacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS palavras_fonte (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                arquivo_id INTEGER NOT NULL,
                palavra TEXT NOT NULL,
                FOREIGN KEY (arquivo_id) REFERENCES arquivos_fonte(id)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS validacao_historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                palavra TEXT NOT NULL,
                nome_arquivo_fonte TEXT NOT NULL,
                automato_usado TEXT NOT NULL,
                resultado TEXT NOT NULL,
                data_validacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def importar_arquivos_txt(self, filepaths: list):
        total_palavras_inseridas = 0
        try:
            for path in filepaths:
                nome_arquivo = os.path.basename(path)
                
                # Limpa dados antigos deste arquivo para evitar duplicatas
                self.cursor.execute("DELETE FROM palavras_fonte WHERE arquivo_id IN (SELECT id FROM arquivos_fonte WHERE nome_arquivo = ?)", (nome_arquivo,))
                self.cursor.execute("DELETE FROM arquivos_fonte WHERE nome_arquivo = ?", (nome_arquivo,))

                # Insere o novo arquivo
                self.cursor.execute("INSERT INTO arquivos_fonte (nome_arquivo) VALUES (?)", (nome_arquivo,))
                arquivo_id = self.cursor.lastrowid
                
                # Lê as palavras do arquivo
                with open(path, 'r', encoding='utf-8') as f:
                    palavras_para_inserir = [
                        (arquivo_id, linha.strip()) 
                        for linha in f if linha.strip()
                    ]
                
                if not palavras_para_inserir:
                    continue

                # Insere as palavras
                self.cursor.executemany(
                    "INSERT INTO palavras_fonte (arquivo_id, palavra) VALUES (?, ?)",
                    palavras_para_inserir
                )
                total_palavras_inseridas += len(palavras_para_inserir)
            
            self.conn.commit()
            return len(filepaths), total_palavras_inseridas
        
        except Exception as e:
            self.conn.rollback()
            raise e

    def consultar_palavras_para_teste(self):
        self.cursor.execute("""
            SELECT a.nome_arquivo, p.palavra 
            FROM palavras_fonte p
            JOIN arquivos_fonte a ON p.arquivo_id = a.id
            ORDER BY a.nome_arquivo, p.id
        """)
        
        resultados_agrupados = {}
        for nome_arquivo, palavra in self.cursor.fetchall():
            if nome_arquivo not in resultados_agrupados:
                resultados_agrupados[nome_arquivo] = []
            resultados_agrupados[nome_arquivo].append(palavra)
            
        return resultados_agrupados

    def salvar_validacao_em_lote(self, resultados: list):
        try:
            sql = """
                INSERT INTO validacao_historico 
                (palavra, nome_arquivo_fonte, automato_usado, resultado) 
                VALUES (?, ?, ?, ?)
            """
            self.cursor.executemany(sql, resultados)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
    
    def consultar_historico_completo(self):
        self.cursor.execute("SELECT * FROM validacao_historico ORDER BY data_validacao DESC")
        return self.cursor.fetchall()

    def fechar_conexao(self):
        if self.conn:
            self.conn.close()

    def resetar_banco_de_dados(self):

  
        try:
            self.cursor.execute("DROP TABLE IF EXISTS validacao_historico")
            self.cursor.execute("DROP TABLE IF EXISTS palavras_fonte")
            self.cursor.execute("DROP TABLE IF EXISTS arquivos_fonte")
            self.conn.commit()
            
            self._criar_tabelas() 
        except Exception as e:
            self.conn.rollback()
            raise e