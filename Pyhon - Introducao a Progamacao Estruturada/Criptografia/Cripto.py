import time
import getpass, sys
import pyAesCrypt
import os.path
from rich.progress import track
from rich import print
from os import stat, remove

#==> Buffer size - 64K
bufferSize = 64 * 1024
arq = 'file.txt'
carq = 'file.txt.aes'
#==> Menu de alternativas.
choice = input('Selecione uma das opcoes abaixo: \n1-> Encriptar\n2-> Decriptar	\n3-> Exit\nR: ')
#==> Trantando caso nao seja selecionado uma opcao valida
while choice != '1' and choice != '2' and choice != '3':
  print ('\n[red]Opcao invalida![/] \n[blue]Por favor selecione uma opcao valida![/]')
  choice = input("Tente Novamente: ")
  time.sleep(0.3)
#==> Alternativa 3 responsavel por sair do progama
if choice == '3':
  print("\n[red]Finalizando o Progama![/]")
  time.sleep(1)
  sys.exit()
#==> Pegando a senha digitada pelo usuario
password = getpass.getpass('\nDigite a Senha:')
#==> Alternativa 1 responsavel por encriptar o arquivo 
if choice == '1':
  #==> Veririfcando se o arquivo decriptado ja existe
  if os.path.isfile(arq):
    print("[purple]Criptografando um aqruivo ja esxistente![/]")
    #==> Veririfcando se o arquivo encriptado ja existe
    if os.path.isfile(carq):
      print("[red]Antencao!! Ja existe um arquivo criptografado nesta pasta, voce ira sobreescrever o mesmo![/]") 
      #==> Tratando as opcoes de escolha
      vld = input("\nDeseja contiuar? Aperte [y] para sim, ou [n] para nao:")
      while vld != 'y' or vld != 'n' or vld == 'y' or vld == 'n':
        if vld == 'y' and vld != 'n':
          print("[purple]\nArquivo sobrescrevido![/]")
          arq = open("file.txt", "w")
          arq.write(input("\nInforme a mensagem a ser Criptografada: "))
          arq.close()
          break
        elif vld != 'y' and vld == 'n':
          print("[green]\nArquivo mantido![/]\n\n[purple]Mova o aquivo e faca o processo novamente[/]! \n\n[red]Finalizando o progama![/]")
          time.sleep(2.5)
          sys.exit()
        else:
          print("\n[red]Escolha uma opcao valida![/]")
          vld = input("[y] ou [n]: ")
  else:
   arq = open("file.txt", "w")
   arq.write(input("Informe a mensagem a ser Criptografada: "))
   arq.close()
   if os.path.isfile(carq):
    print("[red]Antencao!! Ja existe um arquivo criptografado nesta pasta, voce ira sobreescrever o mesmo![/]") 
    #==> Tratando as opcoes de escolha
    vld = input("\nDeseja contiuar? Aperte [y] para sim, ou [n] para nao:")
    while vld != 'y' or vld != 'n' or vld == 'y' or vld == 'n':
      if vld == 'y' and vld != 'n':
        print("[purple]\nArquivo sobrescrevido![/]")
        break
      elif vld != 'y' and vld == 'n':
        print("[green]\nArquivo mantido![/]\n\n[purple]Mova o aquivo e faca o processo novamente![/] \n\n[red]Finalizando o progama![/]")
        time.sleep(2.5)
        sys.exit()
      else:
        print("\n[red]Escolha uma opcao valida![/]")
        vld = input("[y] ou [n]: ")
  # encriptando  arquivo
  with open("file.txt", "rb") as fIn:
   with open("file.txt.aes", "wb") as fOut:
    pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
  #==> Tratando as opcoes de escolha
  x = input ('\nDeseja deletar o arquivo descriptografado?\nAperte [y] para sim, ou [n] para nao: ')
  while x != 'y' or x != 'n' or x == 'y' or x == 'n':
   if x != 'y' and x == 'n':
    print ('\n[green]Arquivo descriptografado foi mantido![/]\n\n[red]Finalizando o progama![/]')
    time.sleep(1)
    sys.exit()
   elif x == 'y' and x != 'n':  
    remove("file.txt")
    print ('\n[purple]Arquivo descriptografado deletado![/]\n\n[red]Finalizando o progama![/]')
    time.sleep(2)
    sys.exit()
   else:
     print("\n[red]Escolha uma opcao valida![/]")
     x = input("[y] ou [n]: ")
#==> Alternativa 2 resonsavel por decriptar o arquivo
if choice == '2':
 if os.path.isfile(carq):
  #==> Pegando o arquivo encriptado
  encFileSize = stat("file.txt.aes").st_size
  #==> Descriptando o arquivo
  with open("file.txt.aes", "rb") as fIn:
   try:
    with open("file.txt", "wb") as fOut:
     pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
     print("[green]\nArquivo descriptografado com sucesso![/]")
   except ValueError:
    print ('[red]Senha incorreta![/]\n\n[red]Finalizando o progama![/]')
    #==> removendo a saida em caso de erro
    remove("file.txt")
    time.sleep(2)
    sys.exit()
   #==> Tratando as opcoes de escolha
   x = input("\nDeseja visualizar o conteudo do arquivo?\nAperte [y] para sim, ou [n] para nao:  ")
   while x != 'y' or x != 'n' or x == 'y' or x == 'n':
    if x != 'y' and x == 'n':
      print("\n[red]Finalizando o progama![/]")
      sys.exit(2)
    elif x == 'y' and x != 'n':
     with open("file.txt", "r", encoding="utf-8") as coded:
      print("\n",coded.read(),"\n")
      print("\n[purple]Atencao!!!  A visualizacao esta disponivel por 10s![/]")
      for i in track(range(10),'Tempo restante!'):
        time.sleep(1)
      sys.exit()   
    else:
     print("\n[red]Escolha uma opcao valida![/]")
     x = input("[y] ou [n]: ")
 else:
  print("[purple]Nenhum arquivo a ser descriptografado![/]\n\n[red]Finalizando o progama![/]")
time.sleep(2)
sys.exit()

