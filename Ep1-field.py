import random
b=random.randint(1,6)
c=random.randint(1,6)
fase='come out'
t=int(input('Bem vindo a rodada de come out, quantas fichas você tem disponivel: '))
f=int(input('Quantas fichas você quer apostar nessa rodada: '))
f2=f*2
f3=f*3
d=b+c
print('O valor do primeiro dado for {0} e o valor do segundo dado foi {1}. Portanto a soma dos dados é {2}'.format(b,c,d))
while fase == 'come out':
    if 5<=d<=8:
        print('Você perdeu tudo')
        break
    elif d==3 or d==4 or d==9 or d==10 or d==11:
        print('Você recebeu sua aposta de {0} fichas de volta'.format(f))
        fase='point'
    elif d==2:
        print('Você recebeu {0} fichas'.format(f2))
        fase='point'
    else:
        print('Você recebeu {0} fichas'.format(f3))
        fase='point'
