from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from keys import username,password
from os import system
import time

system('clear') 
dtinicial = input('Digite a data inicial no formato DDMMAAAA \n')
dtfinal = input('Digite a data final no formato DDMMAAAA \n')

dtInicialAno =  dtinicial[4:8]
dtInicialMes = dtinicial[2:4]
dtInicialDia = dtinicial[0:2]
formatedDtInicial = (dtInicialAno + "-" + dtInicialMes + "-" + dtInicialDia)
dtfinalAno = dtfinal[4:8]
dtfinalMes = dtfinal[2:4]
dtfinalDia = dtfinal[0:2]
formatedDtFinal = (dtfinalAno + "-" + dtfinalMes + "-" + dtfinalDia)
formatedDtFinal += "T23%3A59%3A59-03%3A00"
formatedDtInicial += "T00%3A00%3A00-03%3A00"

link = ("https://app.intercom.com/a/apps/iirbswk2/reports/customer-support?rangeEnd=" + formatedDtFinal + "&rangeStart=" + formatedDtInicial)
print("\nLink: " + link + "\n")

DRIVER_PATH = '../../Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(link)
time.sleep(10)
googleClick = driver.find_element_by_class_name("m__sign-in-with-google__logo").click()
time.sleep(5.0)
googleLogin = driver.find_element_by_xpath("//input").send_keys(username)
googleLoginClick = driver.find_element_by_xpath("//button[@jsname='LgbsSe']").click()
time.sleep(5.0)
googleSenha = driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
googleSenhaClick = driver.find_element_by_xpath("//button[@jscontroller='soHxf']").click()
time.sleep(30)

i=0
while i < 21:
    try:
        delay = 2
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'ember1995')))
        driver.find_element_by_id("ember1995").click()
        time.sleep(2)
        i += 1
    except TimeoutException:
        print ("Não existe mais botão 'Load More'")
        i=21

if i==21:
    print("Todos atendentes foram carregados")