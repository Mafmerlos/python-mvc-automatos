from tkinter import filedialog
from views.view import View
from database import DatabaseManager
import os

from automato_inicia_00 import validar as validar_inicia_00
from automato_contem_00 import validar as validar_contem_00
from automato_termina_00 import validar as validar_termina_00

class Controller:
    
    def __init__(self, view):
        self.view = view
        self.db_manager = DatabaseManager("automato_mestre.db")
        
        self.validation_map = {
            "Inicia com 00": validar_inicia_00,
            "Contém 00": validar_contem_00,
            "Termina com 00": validar_termina_00
        }
        
        self.view.btn_selecionar['command'] = self.importar_arquivos_para_bd
        self.view.btn_processar['command'] = self.processar_palavras_do_bd
        self.view.btn_historico['command'] = self.visualizar_historico
        self.view.btn_resetar['command'] = self.solicitar_reset_banco

    def importar_arquivos_para_bd(self):
        filepaths = filedialog.askopenfilenames(
            title="Selecione os arquivos .txt para importar",
            filetypes=(("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*"))
        )
        
        if not filepaths:
            self.view.exibir_erro("Nenhuma importação realizada.")
            return

        try:
            self.view.limpar_resultados()
            self.view.exibir_cabecalho_arquivo("Importando arquivos para o banco de dados...")
            
            total_arquivos, total_palavras = self.db_manager.importar_arquivos_txt(filepaths)
            
            if total_palavras > 0:
                self.view.exibir_cabecalho_arquivo(
                    f"Sucesso: {total_palavras} palavras de {total_arquivos} arquivo(s) importadas para o BD."
                )
            else:
                self.view.exibir_erro("Os arquivos selecionados estavam vazios ou não puderam ser lidos.")
                
        except Exception as e:
            self.view.exibir_erro(f"Erro ao importar arquivos para o BD: {e}")

    def processar_palavras_do_bd(self):
        selected_automaton_name = self.view.automaton_selector.get()
        if not selected_automaton_name:
            self.view.exibir_erro("Por favor, selecione um autômato no menu.")
            return
            
        validar_funcao = self.validation_map[selected_automaton_name]

        self.view.limpar_resultados()
        self.view.exibir_cabecalho_arquivo(f"Processando com o Autômato: '{selected_automaton_name}'")
        
        resultados_para_salvar_no_bd = []

        try:
            dados_do_banco = self.db_manager.consultar_palavras_para_teste()
            
            if not dados_do_banco:
                self.view.exibir_erro("Nenhuma palavra encontrada no banco. Importe os arquivos primeiro.")
                return

            for nome_arquivo, palavras in dados_do_banco.items():
                self.view.exibir_cabecalho_arquivo(f"Resultados de '{nome_arquivo}' (lido do BD)")
                
                for palavra in palavras:
                    resultado_bool = validar_funcao(palavra)
                    self.view.exibir_resultado(palavra, resultado_bool)
                    
                    resultado_str = "ACEITA" if resultado_bool else "REJEITA"
                    dados_para_salvar = (palavra, nome_arquivo, selected_automaton_name, resultado_str)
                    resultados_para_salvar_no_bd.append(dados_para_salvar)

            if resultados_para_salvar_no_bd:
                self.db_manager.salvar_validacao_em_lote(resultados_para_salvar_no_bd)
                self.view.exibir_cabecalho_arquivo(
                    f"Histórico de {len(resultados_para_salvar_no_bd)} validações salvo no BD."
                )

        except Exception as e:
            self.view.exibir_erro(f"Erro ao processar ou salvar no BD: {e}")

    def visualizar_historico(self):
        try:
            self.view.limpar_resultados()
            self.view.exibir_cabecalho_arquivo("Consultando Histórico Completo do BD...")
            
            historico = self.db_manager.consultar_historico_completo()
            
            if not historico:
                self.view.exibir_erro("Nenhum histórico encontrado no banco de dados.")
                return

            self.view.exibir_cabecalho_arquivo(f"Encontrados {len(historico)} registros.")
            
            for registro in historico:
                (id, palavra, nome_arq, automato, res, data) = registro
                data_formatada = str(data).split(" ")[0]
                self.view.exibir_linha_historico(data_formatada, automato, palavra, res)
        
        except Exception as e:
            self.view.exibir_erro(f"Erro ao consultar histórico: {e}")

    def solicitar_reset_banco(self):
        if self.view.confirmar_reset():
            try:
                self.db_manager.resetar_banco_de_dados()
                self.view.limpar_resultados()
                self.view.exibir_cabecalho_arquivo("BANCO DE DADOS RESETADO.")
                self.view.exibir_erro("Todo o histórico e palavras importadas foram apagados.")
            except Exception as e:
                self.view.exibir_erro(f"Erro ao resetar o banco: {e}")
        else:
            self.view.limpar_resultados()
            self.view.exibir_cabecalho_arquivo("Operação de reset cancelada.")