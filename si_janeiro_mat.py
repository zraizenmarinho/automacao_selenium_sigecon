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



#Fevereiro

    fev_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['2'], ['2023'], '1 Gratuidade Regimental')
    fev_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['2'], ['2023'], '2 Gratuidade Não Regimental')
    fev_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['2'], ['2023'], '3 Convênio')
    fev_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['2'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')

#Março

    mar_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['3'], ['2023'], '1 Gratuidade Regimental')
    mar_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['3'], ['2023'], '2 Gratuidade Não Regimental')
    mar_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['3'], ['2023'], '3 Convênio')
    mar_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['3'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')

#Abril

    abr_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['4'], ['2023'], '1 Gratuidade Regimental')
    abr_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['4'], ['2023'], '2 Gratuidade Não Regimental')
    abr_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['4'], ['2023'], '3 Convênio')
    abr_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['4'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')

#Maio

    mai_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['5'], ['2023'], '1 Gratuidade Regimental')
    mai_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['5'], ['2023'], '2 Gratuidade Não Regimental')
    mai_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['5'], ['2023'], '3 Convênio')
    mai_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['5'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')


#Junho

    jun_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['6'], ['2023'], '1 Gratuidade Regimental')
    jun_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['6'], ['2023'], '2 Gratuidade Não Regimental')
    jun_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['6'], ['2023'], '3 Convênio')
    jun_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['6'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')

#Julho

    jul_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['7'], ['2023'], '1 Gratuidade Regimental')
    jul_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['7'], ['2023'], '2 Gratuidade Não Regimental')
    jul_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['7'], ['2023'], '3 Convênio')
    jul_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['7'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')

#Agosto

    ago_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['8'], ['2023'], '1 Gratuidade Regimental')
    ago_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['8'], ['2023'], '2 Gratuidade Não Regimental')
    ago_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['8'], ['2023'], '3 Convênio')
    ago_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['8'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')


#Setembro

    set_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['9'], ['2023'], '1 Gratuidade Regimental')
    set_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['9'], ['2023'], '2 Gratuidade Não Regimental')
    set_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['9'], ['2023'], '3 Convênio')
    set_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['9'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')


#Outubro

    out_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['10'], ['2023'], '1 Gratuidade Regimental')
    out_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['10'], ['2023'], '2 Gratuidade Não Regimental')
    out_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['10'], ['2023'], '3 Convênio')
    out_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['10'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')

#Novembro

    nov_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['11'], ['2023'], '1 Gratuidade Regimental')
    nov_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['11'], ['2023'], '2 Gratuidade Não Regimental')
    nov_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['11'], ['2023'], '3 Convênio')
    nov_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['11'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')


#Dezembro

    dez_ip_mat_regi = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12'], ['2023'], '1 Gratuidade Regimental')
    dez_ip_mat_bolsa = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12'], ['2023'], '2 Gratuidade Não Regimental')
    dez_ip_mat_convenio = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12'], ['2023'], '3 Convênio')
    dez_ip_mat_n_gratuita = matriculas_por_tipo.contar_matriculas('1117376 SENAI Taguatinga', '5 Iniciação Profissional', '1 Presencial', ['12'], ['2023'], '9 Pago por Pessoa Fisica ou Empresa')


    return {
    
        "fev_ip_mat_regi": fev_ip_mat_regi,
        "fev_ip_mat_bolsa":fev_ip_mat_bolsa,
        "fev_ip_mat_convenio":fev_ip_mat_convenio,
        "fev_ip_mat_n_gratuita":fev_ip_mat_n_gratuita,

        "abr_ip_mat_regi": abr_ip_mat_regi,
        "abr_ip_mat_bolsa":abr_ip_mat_bolsa,
        "abr_ip_mat_convenio":abr_ip_mat_convenio,
        "abr_ip_mat_n_gratuita":abr_ip_mat_n_gratuita,

        "mai_ip_mat_regi": mai_ip_mat_regi,
        "mai_ip_mat_bolsa":mai_ip_mat_bolsa,
        "mai_ip_mat_convenio":mai_ip_mat_convenio,
        "mai_ip_mat_n_gratuita":mai_ip_mat_n_gratuita,

        "jun_ip_mat_regi": jun_ip_mat_regi,
        "jun_ip_mat_bolsa":jun_ip_mat_bolsa,
        "jun_ip_mat_convenio":jun_ip_mat_convenio,
        "jun_ip_mat_n_gratuita":jun_ip_mat_n_gratuita,

        "jul_ip_mat_regi": jul_ip_mat_regi,
        "jul_ip_mat_bolsa":jul_ip_mat_bolsa,
        "jul_ip_mat_convenio":jul_ip_mat_convenio,
        "jul_ip_mat_n_gratuita":jul_ip_mat_n_gratuita,

        "ago_ip_mat_regi": ago_ip_mat_regi,
        "ago_ip_mat_bolsa":ago_ip_mat_bolsa,
        "ago_ip_mat_convenio":ago_ip_mat_convenio,
        "ago_ip_mat_n_gratuita":ago_ip_mat_n_gratuita,

        "set_ip_mat_regi": set_ip_mat_regi,
        "set_ip_mat_bolsa":set_ip_mat_bolsa,
        "set_ip_mat_convenio":set_ip_mat_convenio,
        "set_ip_mat_n_gratuita":set_ip_mat_n_gratuita,

        "out_ip_mat_regi": out_ip_mat_regi,
        "out_ip_mat_bolsa":out_ip_mat_bolsa,
        "out_ip_mat_convenio":out_ip_mat_convenio,
        "out_ip_mat_n_gratuita":out_ip_mat_n_gratuita,

        "nov_ip_mat_regi": nov_ip_mat_regi,
        "nov_ip_mat_bolsa":nov_ip_mat_bolsa,
        "nov_ip_mat_convenio":nov_ip_mat_convenio,
        "nov_ip_mat_n_gratuita":nov_ip_mat_n_gratuita,

        "dez_ip_mat_regi": dez_ip_mat_regi,
        "dez_ip_mat_bolsa":dez_ip_mat_bolsa,
        "dez_ip_mat_convenio":dez_ip_mat_convenio,
        "dez_ip_mat_n_gratuita":dez_ip_mat_n_gratuita, 
    }


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
    resultados = {}

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

    return resultados

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
