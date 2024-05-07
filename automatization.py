# Projeito feito em Python com a biblioteca pandas. Automatização com função de leitura de uma tabela já fornecida, para o preenchimento de dados em um formulário.

import pyautogui
import time
import pandas as pd

#Pause para os comandos não se atropelarem
pyautogui.PAUSE = 0.5

#Abrir o navegador e inserir o link do site
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

#Tempo para o site carregar
time.sleep(1)


#Login
pyautogui.click(x=809, y=377)
pyautogui.write('login@gmail.com')

#Senha
pyautogui.press('tab')
pyautogui.write('21290187')


#Clicar no botão de login
pyautogui.click(x=958, y=547)


#Ler a base de dados com Pandas
tabela = pd.read_csv("produtos.csv")

print(tabela.head)


#Cadastrar as informações do produto:
for linha in tabela.index:

    #Clicar na primeira linha de preenchimento do formulário
    pyautogui.click(x=743, y=276)

    pyautogui.write(str(tabela.loc[linha,'codigo']))

    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'marca']))
    
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha,'tipo']))

   
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'categoria']))

    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'preco_unitario']))

    
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha,'custo']))

    pyautogui.press('tab')
    obs = str(tabela.loc[linha,'obs'])

    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')
    
    pyautogui.press('enter')
    
    pyautogui.scroll(5000)

   
