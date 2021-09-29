nome=input('Qual é o seu nome? ')
idade=input('Qual a sua idade? ')
print('Vamos calcular sua média!')
nota1=int(input('Digite sua nota 1: '))
nota2=int(input('Digite sua nota 2: '))
nota3=int(input('Digite sua nota 3: '))
somanota=nota1 + nota2 + nota3
medianota= int(somanota /3)
if medianota >=6:
    print('Você foi aprovado! Sua média foi de:', medianota)
else:
    print('Você foi reprovado! Sua média foi de:', medianota)   


