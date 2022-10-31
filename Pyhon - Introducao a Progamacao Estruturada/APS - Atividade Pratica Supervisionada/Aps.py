#==> Caracteres aceitos.
#AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz
#1234567890
#!@.#?,%&*( )-+;=_/:[]\'{}<>´`
#ÇçÃãÕõÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÂâÊêÎîÔôÛû


def nosep(*args):#==> Funcao responsavel por remover espacos do print quando passado dois ou mais argumentos
   print(*args, sep='')#==> *args e usado para receber uma lista de argumentos de comprimento variavel sem a palavra-chave, sep = '' remove os espacos entre eles

print("======================================================\n     Progama para Encriptar/Decriptar mensagens\n======================================================\n")
def aps():
  #==> Chave
  k = "0z1múa2ÀuÌcÕh3e}owóp4fÂlìgnày´r5bùtâvi<qãj6dêÚxks! 7AèBC;D?E'FÉÎGÍ8HéIJK{ûLM*Nò9ÊO`PõQR\SíTUÈîVÓ_WX>YZ.@,ô%:(Ò&-/çÔ)[Ã]ÙÇÁ#Û=+á" #==> Chave para a criacao dos dicionarios
  v = k[-1] + k[0:-1] #==> Valores que serao usados na criacao do dicionario

  #==> Criando dicionariso de criptacao e decriptacao
  c = dict(zip(k,v))#==> Criando dicionario para encriptar,  c recebe chave / valor
  d = dict(zip(v,k))#==> Criando dicionario para decriptar,  d recebe valor / chave

  #==> Validando se foi escolhido um opcao valida
  msg = input("Digite a sua mensagem: ")#==> Capturando a mensagem do usuario
  x = input("Digite [C] para criptografar, ou [D] para descriptografar: ")#==> Opcoes de escolha sendo [C] para criptar e [D] para decriptar
  while x.upper() != 'C' and x.upper() != 'D':#==> Validando se foi escolhido uma opcao valida
    print("Escolha uma opcao valida!")
    x = input("[C] ou [D]: ")
  #==> Tratando possiveis erros de caractere / criptando e decriptando a mensagem
  try:#==> Vai tentar executar o bloco abaixo caso contanha algum caractere invalido na mensagem / ocorrer algum error, vai retornar uma execpt
    if x.upper() != 'D' and x.upper() == 'C':#==> Validando a escolha do usuario se for escolhido criptar
      nmsg = ''.join([c[i] for i in msg])#==> Crio uma variavel nova para receber a mensagem criptada
      print("\nMensagem Criptografada, copie todos os caracteres entre as setas: ")#==> Intrucao de como a mensagem deve ser copiada
    else:#==> Validando a escolha do usuario se for escolhido decriptar
      x.upper() != 'C' and x.upper() == 'D'
      nmsg = ''.join([d[i] for i in msg])#==> Crio uma variavel nova para receber a mensagem criptada
  except Exception as err:#==> Caso seja inserido um caractere invalido, ou seja que nao contenha na minha chave, vai retornar uma execpt, pego essa execpt e armazeno na variavel err
    nmsg = ''
    print(f"\nInforme apenas caracteres validos! Caractere invalido ultilizado: {err} ")#==> Imprimo na tela que foi utilizado caractere invalido, e mostra na tela qual foi o caractere invalido utilizado
    vld = input("Deseja visualizar quais sao os caracteres validos? [Y]/[N]: ")#==> Opcao se deseja visualizar quais sao os caracteres validos
    while vld.upper() != 'Y' and vld.upper() != 'N':#==> Valido se foi escolhido uma opcao valida
      print("Escolha uma opcao valida!")
      vld = input("[Y] ou [N]: ")
    if vld.upper() != 'N' and vld.upper() == 'Y':#==> Se for esclhido Y, imprimo na tela quais os caracteres que podem ser utilizados na mensagem 
      print("\nLetras: \nAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz\n   \nNumeros:  \n1234567890\n  \nCaracteres Especiais:  \n!@.#?,%&*( )-+;=_/´`:[]\'{}<>\n  \nLetras Com Acento:  \nÇçÃãÕõÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÂâÊêÎîÔôÛû\n")
    else:
      print("\nProgama Finalizado!")
  if nmsg != '':#==> Valido se foi retornado uma mensagem criptada ou deu uma execpt
    return nosep("->",nmsg,"<-")#==> retorno a mensagem criptada formatada

aps()#==> Chamo a funcao APS