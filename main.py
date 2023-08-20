#1°passo: escrever o passo a passo do código:

import pandas as pd
import pyautogui as pa
import time


# 1 - entrar no sistema da empresa

pa.PAUSE = 0.5 #da um deley de 0.5s entre os comandos
                #pode variar de acordo com a capacidade de cada máquina

#entrando no navegador (chrome)
pa.press("win") #Clicar na tecla windows 
pa.write("Chrome") #Escrever o nome do navegador
pa.press("enter") #apertar a tecla de enter
time.sleep(3)

#digitando texto de busca
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #escreve a url do site 
pa.press("enter")
time.sleep(3) #espera de 3s para a execução da próxima linha de código

#2 - fazendo login:
#pa.click(x=1314, y=43) #maximizando a tela
pa.click(x=504, y=371) #seleciona o campo de e-mail
pa.write("aaaaaaaa") #escrevendo o e-mail
pa.press("tab") #passa para o próximo campo
pa.click(x=475, y=466) #seleciona o campo de senha
pa.write("suasenha") #escreve a senha
pa.press("tab") 
pa.press("enter") #aperta enter, assim, seleciona o botão de login
time.sleep(3)

# 3 - importando a dase de dados de produtos

tabela = pd.read_csv("produtos.csv") #cria  a variável tabela com o pandas

print(tabela)

# 4 - cadacodigostrar

for linha in tabela.index: #laço para preencher toda a planilha
    pa.click(x=518, y=245) #seleciona o campo 'Código do produto'
    codigo = tabela.loc[linha, "codigo"] #pega o código do produto
    pa.write(str(codigo)) #escreve o código
                        #é usado str para garantir que o texto da tabela seja escrito
    pa.press("tab") #passa para o próximo campo
    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab") 
    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): #Se o valor de obs não for um Nan, eu escrevo qual que seja
        pa.write(str(tabela.loc[linha, "obs"]))
    pa.press("tab")
    pa.press("enter")

    pa.scroll(5000) #dar um scroll até o começo da página

# 5 - Repetir o processo ate o final
#para isso está sendo usado o for 





