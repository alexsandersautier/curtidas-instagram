from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoExperada
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

def typing_human(text,element):
    for word in text:
        element.send_keys(word)
        sleep(random.randint(1, 5)/30)

driver, wait = iniciar_driver()
# Entrar no site do instagram
driver.get('https://www.instagram.com/')
# Clicar e digitar meu usuário
field_login = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
typing_human('user', field_login)
sleep(1)
# Clicar e digitar minha senha 
field_password = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
typing_human('password', field_password)
sleep(1)
# Clicar no campo entrar
button_login = wait.until(CondicaoExperada.element_to_be_clickable((By.XPATH,"//div[text()='Entrar']")))
button_login.click()
sleep(15)
while True:
    # Navegar até a página alvo
    driver.get('https://www.instagram.com/futurecode_software/') 
    sleep(5)
    # Clicar na última  postagem
    post = wait.until(CondicaoExperada.visibility_of_any_elements_located((By.XPATH, "//div[@class='_aagu']")))
    sleep(5)
    post[0].click()
    sleep(2)
    # Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
    elements_post = wait.until(CondicaoExperada.visibility_of_any_elements_located((By.XPATH,"//div[@class='_abm0 _abl_']")))
    if len(elements_post) == 6:
        elements_post[1].click()
        sleep(86400)
    else:
        print('Post is liked')
        sleep(86400)    