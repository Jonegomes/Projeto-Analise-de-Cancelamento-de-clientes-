link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

import pandas as pd 
import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")    
pyautogui.sleep(2)

pyautogui.write(link)
pyautogui.press("enter")
pyautogui.sleep(5)   
pyautogui.click(x=524, y=405)   
pyautogui.write("pythonimpressionardor@gmail.com")
pyautogui.press("tab")
pyautogui.write("Hashtag@1234")
pyautogui.press("enter")        
pyautogui.sleep(4)

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=531, y=297)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if obs != "nan":  # Checa se obs é NaN
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)
    


