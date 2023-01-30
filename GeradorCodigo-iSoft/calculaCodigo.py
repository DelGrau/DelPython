import datetime #importando a biblioteca Datetime

ct = datetime.datetime.now() #Pegando o horario atual

# Convertendo os valores de datetime para inteiro usando multiplicação
# Transformando os valores em multiplos de 10
# Ex: hora = 15
ano = ct.year*10000000000/10000000000
mes = ct.month*100000000/100000000
dia = ct.day*1000000/1000000
hora = ct.hour*10000/10000

# imprimindo o código
print ( '{:.0f}'.format((dia-mes+ano)*hora)+"1" )