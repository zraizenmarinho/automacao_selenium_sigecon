import pandas as pd
import openpyxl
import numpy as np
import si_janeiro_mat
import pandas as pd

# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL PRESENCIAL - Matricula

def obter_matriculas_por_tipo(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas(self, unidade, modalidade, tipo_acao, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_ano & filtro_finan]

            return len(base_filtrada)
    
    matriculas_por_tipo = MatriculasPorTipoFinanciamento(file_path)
    
    ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '1 Gratuidade Regimental')
    ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '2 Gratuidade Não Regimental')
    ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '3 Convênio')
    ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '9 Pago por Pessoa Fisica ou Empresa')

    return {
        "ip_mat_regi": ip_mat_regi,
        "ip_mat_bolsa": ip_mat_bolsa,
        "ip_mat_convenio": ip_mat_convenio,
        "ip_mat_n_gratuita": ip_mat_n_gratuita
    }

# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL PRESENCIAL - Hora Aluno

def obter_hora_por_tipo(file_path):
    class HorasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)

        def somar_hora(self, unidade, modalidade, tipo_acao, mes_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes = self.data['MES_REFERENCIA'].astype(str).isin(mes_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes & filtro_finan]

            soma_hora = base_filtrada.loc[:, 'HORA_ALUNO'].sum() + base_filtrada.loc[:, 'HORA_ALUNO_EAD'].sum()

            return str(soma_hora)
        
    hora_aluno_por_tipo = HorasPorTipoFinanciamento(file_path)

    ip_ha_regi = hora_aluno_por_tipo.somar_hora('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12024'], '1 Gratuidade Regimental')
    ip_ha_bolsa = hora_aluno_por_tipo.somar_hora('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12024'], '2 Gratuidade Não Regimental')
    ip_ha_convenio = hora_aluno_por_tipo.somar_hora('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12024'], '3 Convênio')
    ip_ha_n_gratuita = hora_aluno_por_tipo.somar_hora('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12024'], '9 Pago por Pessoa Fisica ou Empresa')

    return {
        "ip_ha_regi": ip_ha_regi,
        "ip_ha_bolsa": ip_ha_bolsa,
        "ip_ha_convenio": ip_ha_convenio,
        "ip_ha_n_gratuita": ip_ha_n_gratuita
        
    }


# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL DISTANCIA

