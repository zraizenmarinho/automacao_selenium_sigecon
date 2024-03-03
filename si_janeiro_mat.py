import pandas as pd
import openpyxl
import numpy as np
import si_janeiro
import pandas as pd


# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL PRESENCIAl

def obter_matriculas_por_tipo_jan(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas_jan(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin(mes_rela)
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin(mes_referencia)
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan]

            return len(base_filtrada)
    
    matriculas_por_tipo = MatriculasPorTipoFinanciamento(file_path)

    #Janeiro

    jan_ip_mat_regi = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '1 Gratuidade Regimental')
    jan_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '2 Gratuidade Não Regimental')
    jan_ip_mat_convenio = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '3 Convênio')
    jan_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas_jan('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '9 Pago por Pessoa Fisica ou Empresa')

def obter_matriculas_por_tipo(file_path):
    class MatriculasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_matriculas(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin(mes_referencia)
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo  & filtro_mes & filtro_ano & filtro_finan]

            return len(base_filtrada)
    
    matriculas_por_tipo = MatriculasPorTipoFinanciamento(file_path)


    meses = {
 
        'fev': ['22024'],
        'mar': ['32024'],
        'abr': ['42024'],
        'mai': ['52024'],
        'jun': ['62024'],
        'jul': ['72024'],
        'ago': ['82024'],
        'set': ['92024'],
        'out': ['102024'],
        'nov': ['112024'],
        'dez': ['122024']
    }
    
    resultados_mat = {}
    
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ip_mat_{tipo_financiamento}"
            resultados[chave_resultado] = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', mes_referencia, tipo_financiamento)
    
    return resultados_mat
    
def obter_hora_por_tipo(file_path):
    class HorasPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)

        def somar_hora(self, unidade, modalidade, tipo_acao, mes_referencia, tipo_financiamento):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_ref = self.data['MES_REFERENCIA'].astype(str).isin(mes_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_ref & filtro_finan]

            soma_hora_aluno = base_filtrada['HORA_ALUNO'].sum()
            soma_hora_aluno_ead = base_filtrada['HORA_ALUNO_EAD'].sum()

            return soma_hora_aluno + soma_hora_aluno_ead

    hora_aluno_por_tipo = HorasPorTipoFinanciamento(file_path)

    # Criando um dicionário para os meses
    meses = {
        'jan': ['12024'],
        'fev': ['22024'],
        'mar': ['32024'],
        'abr': ['42024'],
        'mai': ['52024'],
        'jun': ['62024'],
        'jul': ['72024'],
        'ago': ['82024'],
        'set': ['92024'],
        'out': ['102024'],
        'nov': ['112024'],
        'dez': ['122024']
    }

    # Inicializando um dicionário para armazenar os resultados
    resultados_ha = {}

    # Iterando sobre os meses
    for mes_atual, mes_referencia in meses.items():
        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado = f"{mes_atual}_ip_ha_{tipo_financiamento}"
            resultados[chave_resultado] = hora_aluno_por_tipo.somar_hora('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', mes_referencia, tipo_financiamento)

    # Calculando a diferença entre os meses subsequentes
    for idx, (mes_atual, mes_referencia) in enumerate(meses.items()):
        if idx == 0:
            continue

        mes_anterior_str = str(int(mes_referencia[0]) - 1).zfill(2)
        mes_anterior = [mes_anterior_str]

        for tipo_financiamento in ['1 Gratuidade Regimental', '2 Gratuidade Não Regimental', '3 Convênio', '9 Pago por Pessoa Fisica ou Empresa']:
            chave_resultado_atual = f"{mes_atual}_ip_ha_{tipo_financiamento}"
            chave_resultado_anterior = f"{list(meses.keys())[idx-1]}_ip_ha_{tipo_financiamento}"
            
            resultado_atual = resultados[chave_resultado_atual]
            soma_meses_anteriores = sum(resultados[f"{list(meses.keys())[i]}_ip_ha_{tipo_financiamento}"] for i in range(idx))
            resultados[chave_resultado_atual] -= soma_meses_anteriores

    return resultados_ha

def obter_concluintes_por_tipo(file_path):
    class ConcluintesPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_concluintes(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento, tipo_situa):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin(mes_rela)
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin(mes_referencia)
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            filtro_situa = self.data['SITUACAO_MATRICULA'] == tipo_situa

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan & filtro_situa]
    

            return len(base_filtrada)
    
    concluintes_por_tipo = ConcluintesPorTipoFinanciamento(file_path)
    
    jan_ip_conc_regi = concluintes_por_tipo.contar_concluintes('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '1 Gratuidade Regimental','2 Concluída')
    jan_ip_conc_bolsa = concluintes_por_tipo.contar_concluintes('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '2 Gratuidade Não Regimental','2 Concluída')
    jan_ip_conc_convenio = concluintes_por_tipo.contar_concluintes('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '3 Convênio','2 Concluída')
    jan_ip_conc_n_gratuita = concluintes_por_tipo.contar_concluintes('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '9 Pago por Pessoa Fisica ou Empresa','2 Concluída')

    return {
        "jan_ip_conc_regi": jan_ip_conc_regi,
        "jan_ip_conc_bolsa": jan_ip_conc_bolsa,
        "jan_ip_conc_convenio": jan_ip_conc_convenio,
        "jan_ip_conc_n_gratuita": jan_ip_conc_n_gratuita
    }

def obter_evasao_por_tipo(file_path):
    class EvasaoPorTipoFinanciamento:
        def __init__(self, file_path):
            self.data = pd.read_excel(file_path)
        
        def contar_evadidos(self, unidade, modalidade, tipo_acao, mes_rela, mes_referencia, anos_referencia, tipo_financiamento, tipo_situa):
            filtro_uni = self.data['UNIDADE_ATENDIMENTO'] == unidade
            filtro_mod = self.data['MODALIDADE'] == modalidade
            filtro_tipo = self.data['TIPO_ACAO'] == tipo_acao
            filtro_mes_rel = self.data['MES_REFERENCIA'].astype(str).isin(mes_rela)
            filtro_mes = self.data['DT_ENTRADA_MÊS'].astype(str).isin(mes_referencia)
            filtro_ano = self.data['DT_ENTRADA_ANO'].astype(str).isin(anos_referencia)
            filtro_finan = self.data['TIPO_FINANCIAMENTO'] == tipo_financiamento
            filtro_situa = self.data['SITUACAO_MATRICULA'] == tipo_situa

            base_filtrada = self.data[filtro_uni & filtro_mod & filtro_tipo & filtro_mes_rel & filtro_mes & filtro_ano & filtro_finan & filtro_situa]

            return len(base_filtrada)
    
    evadidos_por_tipo = EvasaoPorTipoFinanciamento(file_path)
    
    jan_ip_eva_regi = evadidos_por_tipo.contar_evadidos('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '1 Gratuidade Regimental','4 Evadida')
    jan_ip_eva_bolsa = evadidos_por_tipo.contar_evadidos('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '2 Gratuidade Não Regimental','4 Evadida')
    jan_ip_eva_convenio = evadidos_por_tipo.contar_evadidos('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '3 Convênio','4 Evadida')
    jan_ip_eva_n_gratuita = evadidos_por_tipo.contar_evadidos('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial',['12024'], ['1','2','3','4','5','6','7','8','9','10','11','12'], ['2016','2017','2018','2019','2020','2021','2022','2023','2024'], '9 Pago por Pessoa Fisica ou Empresa','4 Evadida')

    return {
        "jan_ip_eva_regi": jan_ip_eva_regi,
        "jan_ip_eva_bolsa": jan_ip_eva_bolsa,
        "jan_ip_eva_convenio": jan_ip_eva_convenio,
        "jan_ip_eva_n_gratuita": jan_ip_eva_n_gratuita
    }


# SENAI TAGUATINGA INICIAÇÃO PROFISSIONAL DISTANCIA
