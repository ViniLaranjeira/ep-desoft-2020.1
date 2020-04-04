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
