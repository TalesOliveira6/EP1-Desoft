import random
b=random.randint(1,6)
c=random.randint(1,6)
game=True
f=0
f2=0
f3=0
ff2=0
ff3=0
fichas=10000-f
s7=0
s30=0
print('Você possuí {0} fichas'.format(fichas))
while game:
    fase='come_out'
    d=b+c
    a=0
    s=0
    ap=int(input('Quantas fichas você quer apostar nessa rodada: '))
    ta=str(input('Onde você gostaria de apostar? Suas opções são Pass Line Bet, Any Craps, Field, Twelve: '))
    s1=fichas-ap
    s2=fichas+ap
    print('O valor do primeiro dado for {0} e o valor do segundo dado foi {1}. Portanto a soma dos dados é {2}'.format(b,c,d))
    tf=fichas-f
    while fase=='come_out':
        a+=f
        s=fichas-a
        if ta=='Pass Line Bet':
            if d==7 or d==11:
                print('Você recuperou sua aposta {0} e agora tem {1}.'.format(ap,s2))
                f=int(input('Quantas fichas você quer apostar nessa rodada: '))
                b=random.randint(1,6)
                c=random.randint(1,6)
                d=b+c
                print('O valor do primeiro dado for {0} e o valor do segundo dado foi {1}. Portanto a soma dos dados é {2}'.format(b,c,d))
                if d==2 or d==3 or d==12:
                    print('CRAPS! Você perdeu!')
                    break
                while d==7 or d==11:
                    print('Você recuperou sua aposta {0}.'.format(f))
                    f=int(input('Quantas fichas você quer apostar nessa rodada: '))
                    b=random.randint(1,6)
                    c=random.randint(1,6)
                    d=b+c
                    print('O valor do primeiro dado for {0} e o valor do segundo dado foi {1}. Portanto a soma dos dados é {2}'.format(b,c,d))
                    if d==2 or d==3 or d==12:
                        print('CRAPS! Você perdeu!')
                        break
                else:
                    while fase =='point' and d!=7:
                        b=random.randint(1,6)
                        c=random.randint(1,6)
                        d=b+c
                        print('O valor do primeiro dado for {0} e o valor do segundo dado foi {1}. Portanto a soma dos dados é {2}'.format(b,c,d))
                        if d==7:
                            print('Você perdeu!')
                            break        
                        else:
                            print('Os dados serão rolados novamente')
            elif d==2 or d==3 or d==12:
                print('CRAPS! Você perdeu!')
                break 
        elif ta=='Any Craps':
            s7=f*7
            if d==2 or d==3 or d==12:
                print('Você ganhou {0} fichas'.format(s7))
            else:
                print('Você perdeu')
                break 
        elif ta=='Field':
            f2=f*2
            f3=f*3
            if 5<=d<=8:
                print('Você perdeu')
                break
            if d==3 or d==11:
                print('Você recebeu sua aposta de {0} fichas de volta'.format(f))
                break
            if d==4 or d==9 or d==10:
                print('Você recebeu sua aposta de {0} fichas de volta'.format(f))
            elif d==2:
                print('Você recebeu {0} fichas'.format(f2))
                break
            else:
                print('Você recebeu {0} fichas'.format(f3))
                break
        else:
            if ta=='Twelve':
                s30=f*30
                if d==12:
                    print('Você ganhou {0} fichas'.format(s30))
                    break
                else:
                    print('Você perdeu.')
                    break  
        if d==4 or d==5 or d==6 or d==8 or d==9 or d==10:
            h=str(input('Você quer continuar o jogo: '))
            if h=='sim':
                print('Agora você está na fase de point, ainda possuí {0} fichas e sua aposta de {1} está mantida. Tudo que você ganhou nas outras etapas pode ser somada ao seu valor total'.format(s1,ap))
            if h=='não':
                game=False
                break
            fase='point' 
            break
    b1=random.randint(1,6)
    c1=random.randint(1,6)
    d1=b1+c1
    while fase=='point':
        ta=str(input('Onde você gostaria de apostar? Suas opções são Any Craps, Field, Twelve: '))
        print('O valor do primeiro dado for {0} e o valor do segundo dado foi {1}. Portanto a soma dos dados é {2}'.format(b1,c1,d1))
        if ta=='Any Craps':
            s7=f*7
            if d==2 or d==3 or d==12:
                print('Você ganhou {0} fichas'.format(s7))
                break
            else:
                print('Você perdeu')
                break 
        elif ta=='Field':
            ff2=f*2
            ff3=f*3
            if 5<=d<=8:
                print('Você perdeu tudo')
                break
            elif d==3 or d==4 or d==9 or d==10 or d==11:
                print('Você recebeu sua aposta de {0} fichas de volta'.format(f))
                break
            elif d==2:
                print('Você recebeu {0} fichas'.format(ff2))
                break
            else:
                print('Você recebeu {0} fichas'.format(ff3))
                break
        elif ta=='Twelve':
            s30=f*30
            if d==12:
                print('Você ganhou {0} fichas'.format(s30))
                break
            else:
                print('Você perdeu.')
                break       
    h=str(input('Você quer continuar o jogo?: '))
    if h=='sim':
        fase='come_out'
    else:
        if h=='não':
            game=False

