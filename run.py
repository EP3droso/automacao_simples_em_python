import pyautogui
import time
import pandas as pd

#pyautogui.write = escreve
#pyautogui.click = clica com o mouse
#pyautogui.press = clica uma tecla
#pyautogui.hotkey = clica um atalho do teclado
#pyautogui.PAUSE = x   [comando que define uma pausa entre cada comando do py autogui por x segundos]

#pyautogui.position() = mostra a posição do mouse
#pyautogui.drag = clica e arrasta

#.index = seleciona as linhas da tabela (elas tem o nome de indice/ index em ingles)

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=696, y=362)
# escrever o seu email
pyautogui.write("emailfalso@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar

tabela = pd.read_csv("produtos.csv")


# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=753, y=240)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
