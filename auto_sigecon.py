# Importação dos pacotes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from si_janeiro_mat import obter_matriculas_por_tipo
from si_janeiro_mat import obter_hora_por_tipo

var1 = obter_matriculas_por_tipo("si_jan.xlsx")
var2 = obter_hora_por_tipo("si_jan.xlsx")


# Navevagção para a pagina
url = 'http://sn-iis-02/SIGECON20/'

nav = webdriver.Firefox()

nav.get(url)

# Elemento Usuario
e_usuario = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="UserName"]')))
usuario = "matheus.reck"
e_usuario.send_keys(usuario)

# Elemento Senha
e_senha = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Password"]')))
senha = "P**75**"
e_senha.send_keys(senha)

# Elemento Ano
e_ano = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Ano"]')))
e_ano.click()
e_ano_2024 = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/fieldset/div[3]/select/option[1]')))
e_ano_2024.click()

# Elemento Entidade
e_entidade = WebDriverWait(nav, 5).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Cod_Empresa"]')))
e_entidade.click()
e_entidade_senai = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/fieldset/div[4]/select/option[3]')))
e_entidade_senai.click()

# Elemento Entrar
e_entrar = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/form/fieldset/div[6]/input')))
e_entrar.click()

# Elemento unidade

e_uni_tag1 = WebDriverWait(nav, 10).until(EC.visibility_of_element_located(
    (By.PARTIAL_LINK_TEXT, 'Senai Taguatinga')))
e_uni_tag1.click()

#Elemento CR INICIAÇÃO PROFISSIONAL PRESENCIAL
e_cr_inici_prese = WebDriverWait(nav, 5).until(EC.visibility_of_element_located(
    (By.PARTIAL_LINK_TEXT, 'INICIACAO PROFISSIONAL PRESENCIAL')))
e_cr_inici_prese.click()

#Elemento FICHA DE PRODUÇÃO # Click com JS

e_ficha_prod = WebDriverWait(nav, 15).until(EC.visibility_of_element_located(
    (By.LINK_TEXT, 'Produção')))

nav.execute_script("arguments[0].scrollIntoView(true);", e_ficha_prod)

nav.execute_script("arguments[0].click();", e_ficha_prod)

#Elemento Grupo de meta

e_grupo_meta = WebDriverWait(nav, 30).until(EC.visibility_of_element_located(
    (By.XPATH, "//a[@href='/SIGECON20/Metas/MetasTipo/309/2024/0902030201/229?cd_centro_resp=30303010101&nm_unidade=SENAI%20TAGUATINGA&nm_centro_resp=INICIACAO%20PROFISSIONAL%20PRESENCIAL&id_grupo=1&ds_grupo=Inicia%C3%A7%C3%A3o%20Profissional&fase=Realiza%C3%A7%C3%A3o']"
)))

nav.execute_script("arguments[0].scrollIntoView(true);", e_grupo_meta)

e_grupo_meta.click()

# Elemento Matricula Bolsa - JANEIRO

em_bolsa_click = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-tipo="1"]')))

em_bolsa_click.click()

em_bolsa_s = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

em_bolsa_s.send_keys(var1['ip_mat_bolsa'])

em_bolsa_s.send_keys(Keys.ENTER)

# Elemento Matricula Não Gratuita - JANEIRO

em_n_gratuita_click = WebDriverWait(nav, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//tr[@id='5114']/td[4]/a")))

em_n_gratuita_click.click()

em_n_gratuita_s = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]")))

em_n_gratuita_s.send_keys(var1['ip_mat_n_gratuita'])

em_n_gratuita_s.send_keys(Keys.ENTER)

# Elemento Hora Aluno Bolsa - JANEIRO

nav.refresh()

eha_bolsa_click2 = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5111'].indicador")))

eha_bolsa_click2.click()

eha_bolsa_id = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID, "5111"
)))

eha_bolsa_popover = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "popover-content"
)))

eha_bolsa_s = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eha_bolsa_s.send_keys(var2['ip_ha_bolsa'])

eha_bolsa_s.send_keys(Keys.ENTER)

#Elemento Hora Aluno Não Gratuita - JANEIRO

eha_n_gratuita_click = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "td:nth-child(4) > [id='5112'].indicador")))

eha_n_gratuita_click.click()

eha_n_gratuita_s = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.ID,5112)))

eha_n_gratuita_s = WebDriverWait(nav, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,"popover-content")))

eha_n_gratuita_s = WebDriverWait(nav, 10).until(EC.visibility_of_element_located((By.XPATH, "(//input[@type='text'])[8]"
)))

eha_n_gratuita_s.send_keys(var2['ip_ha_n_gratuita'])

eha_n_gratuita_s.send_keys(Keys.ENTER)


