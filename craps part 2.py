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