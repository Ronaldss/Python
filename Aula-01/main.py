import pyautogui
import pyperclip
import time

# Rodando em ambiente fora do Jupyter
# será necessário importar demais bibliotecas
# pandas
# numpy
# openpyxl

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema (no caso, entrar no link)
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)
# Passo 2: Navegar até o local do relatório (Entrar na pasta Exportar)
pyautogui.click(x=334, y=288, clicks=2)

time.sleep(2)
# Passo 3: Fazer download do arquivo
pyautogui.click(x=428, y=408)
time.sleep(1)
pyautogui.click(x=1157, y=195)
time.sleep(1)
pyautogui.click(x=1084, y=597)
time.sleep(5)


# -----------------------------------------------

### Agora vamos lê o arquivo baixado e guardar os indicadores
## Faturamento
## Quantidade de produto

# Calcular os indicadores
import pandas as pd

tabela = pd.read_excel(r"C:\Users\Suporte\Downloads\Vendas - Dez.xlsx") # Consultar caminho do diretório
display(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# -----------------------------------------------

### Enviando e-mail via Gmail

# Passo 5: Entrar no email
pyautogui.hotkey("ctrl","t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(5)

# Passo 6: Enviar por e-mail o resultado
pyautogui.click(x=74, y=202)
time.sleep(1)

#pyautogui.write("e-mail@gmail.com")
pyautogui.write("ronaldcontact2019@gmail.com")
pyautogui.press("tab") # seleciona o e-mail
pyautogui.press("tab") # pula para campo assunto
pyperclip.copy("Relatório automatizado por Python #Ronald#")
pyautogui.hotkey("ctrl","v") # escreve o assunto
pyautogui.press("tab") # pula para campo conteudo

time.sleep(1)
texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produto foi de: R$ {quantidade:,}

Abs
Ronald SS"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")

# Apertar ctrl + enter para enviar e-mail
pyautogui.hotkey("ctrl","enter")


# -----------------------------------------------

### Use esse código para descobrir qual a posição de um item que queira clicar
##Lembre-se: a posição na sua tela é diferente da posição na minha tela

#time.sleep(4)
#pyautogui.position()





