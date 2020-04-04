from random import randint

def principal ():
  continua = True
  validar = True
  fichas = 75000
  while continua:
    while validar:
      aposta = input("Voce tem {} fichas. Quantas fichas voce quer aposta?: ". format(fichas))
      try:
        aposta = int(aposta)
        if (aposta >= 1) and (aposta <= fichas):
          validar = False
      except:
        print("Aposta nao valida.")
    print("que tipo de aposta vc quer fazer?")
    Apostas = input("(aperte 't' para Twelve, 'a' para Any Craps): " )
    if (Apostas == 't' or Apostas == 'T'):
      fichas = Twelve (fichas, aposta)
      print ("voce tem",(fichas), "fichas.")
    if (Apostas == 'A' or Apostas == 'a'):
      fichas = AnyCraps (fichas, aposta)
      print ("voce tem",(fichas), "fichas.")
    if fichas == 0:
      print("vc perdeu todas suas fichas. mais sorte na proxima vez!")
      continua = False
    if continua == True:
      print("vc quer continuar jogando?")
      sairdojogo = input("(Escreva 'sair' para sair do jogo ou qualquer tecla para continuar): ")
      if (sairdojogo == 'q' or sairdojogo == 'Q'):
        print("voce saiu com", (fichas), "fichas.")
        continua = False
    validar = True

def jogando_os_dados(numero_aleatorio):
  if numero_aleatorio == 6:
    print (" 6 ")
  elif numero_aleatorio == 5:
    print (" 5 ")
  elif numero_aleatorio == 4:
    print (" 4 ")
  elif numero_aleatorio == 3:
    print (" 3 ")
  elif numero_aleatorio == 2:
    print (" 2 ")
  elif numero_aleatorio == 1:
    print (" 1 ")
    
def rolagem_aleatoria():
  numero_aleatorio = randint(1, 6)
  jogando_os_dados (numero_aleatorio)
  return numero_aleatorio

def AnyCraps (fichas, aposta):
    validar = True
    checar = True 
    Dado1 = rolagem_aleatoria()
    Dado2 = rolagem_aleatoria()
    Sdados= Dado2 + Dado1
    AnyCraps = (7*aposta)
    fichas = fichas - aposta
    fichas = fichas + aposta
    if Sdados== 2 or Sdados== 3 or Sdados== 12:
        fichas = fichas + aposta    
        print('Você ganhou {}, 7 vezes o valor apostado!!'. format(Any_Craps))
    else:
        fichas = fichas - aposta
        print('vc perdeu {} fichas'. format(aposta))
    return fichas

def Twelve (fichas, aposta):
    validar = True
    checar = True 
    Dado1 = rolagem_aleatoria()
    Dado2 = rolagem_aleatoria()
    Sdados= Dado2 + Dado1
    Twelve = (30*aposta)
    if Sdados== 12:
        fichas = fichas + aposta
        print('Você ganhou {}, 30 vezes o valor apostado!!!!'. format(Twelve))
    else:
        fichas = fichas - aposta
        print('vc perdeu {} fichas'. format(aposta))
    return fichas 

principal ()   
