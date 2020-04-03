import random
b=random.randint(1,6)
c=random.randint(1,6)
fase='come out'
t=int(input('Bem vindo a rodada de come out, quantas fichas você tem disponivel: '))
f=int(input('Quantas fichas você quer apostar nessa rodada: '))
s=f*7
d=b+c
print('O valor do primeiro dado for {0} e o valor do segundo dado foi {1}. Portanto a soma dos dados é {2}'.format(b,c,d))
while fase == 'come out':
    if d==2 or d==3 or d==12:
        print('Você ganhou {0} fichas'.format(s))
        fase='point'
    else:
        print('Você perdeu')
        break