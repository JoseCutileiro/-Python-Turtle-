"""
ALUNO:
PROJETO: BUILT IT YOURSELF
"""

import turtle
from math import sqrt
from random import *    # O random é uma funcao utilizada para fazer o telhado e dar uma sensação 3d

print("BEM-VINDO ao 'BUILD IT YOURSELF")
tamanho_casa_var = int(input("Digite o tamanho para a casa: "))
largura_casa_var = int(input("Digite a largura para a casa: "))
cor_fundo = input("Digite aqui a cor do fundo: ")
cor_central = input("Digite uma cor para o quadrado central da casa: ")
cor_lateral = input("Digite uma cor para a lateral da casa:")
cor_porta = input("Digite uma cor para a porta da casa: ")
print("O telhado é composto por 5 cores")
primeira = input("Primeira cor: ")
segunda = input("Segunda cor: ")
terceira = input("Terceira cor: ")
quarta = input("Quarta cor: ")
quinta = input("Quinta cor: ")

# CANETAS UTILIZADAS
caneta_texto =  turtle.Turtle()
quadrado_central = turtle.Turtle()
lateral_casa = turtle.Turtle()
porta = turtle.Turtle()
primeiro_telhado = turtle.Turtle()

primeiro_telhado.speed(10000)


# Variaveis
Tamanho_casa = tamanho_casa_var
Tamanho_lateral_casa = largura_casa_var


# ECRA
cor_do_fundo = cor_fundo
screen = turtle.Screen()
screen.bgcolor(cor_do_fundo)


#TEXTO
caneta_texto.color(cor_do_fundo)
caneta_texto.left(90)
caneta_texto.forward(300)
caneta_texto.color("black")
fonte = ("arial",18,"bold")
caneta_texto.write("Ola",False,"center",fonte)


#Quadrado Central
quadrado_central.color(cor_central)
quadrado_central.begin_fill()
for i in range(4):
    quadrado_central.forward(Tamanho_casa)
    quadrado_central.left(90)
quadrado_central.end_fill()
quadrado_central.color(cor_do_fundo)
quadrado_central.forward(2000)   # Expulsar os pointers do ecra

#Lateral Casa
lateral_casa.color(cor_do_fundo)  # (tornar invisivel)
lateral_casa.forward(Tamanho_casa)
lateral_casa.color(cor_lateral) # (tornar visivel)

lateral_casa.begin_fill()
for i in range(4):
    if i < 2 or i == 3:
        lateral_casa.left(45)
    else:
        lateral_casa.left(90+45)
    if i%2 == 0:
        lateral_casa.forward(Tamanho_lateral_casa)
    else:
        lateral_casa.forward(Tamanho_casa)
lateral_casa.end_fill()
lateral_casa.color(cor_do_fundo)
lateral_casa.forward(2000)  # Expulsar os pointers do ecra


#Porta
porta.color("white")
porta.forward(Tamanho_casa/3)
porta.color(cor_porta)
porta.begin_fill()
for i in range(4):
    if i%2 == 0:
        porta.forward(Tamanho_casa/4)

    else:
        porta.forward((Tamanho_casa/2))
    porta.left(90)
porta.end_fill()
porta.color(cor_fundo)
porta.forward(2000)

#Telhado  // TECNICA UTILIZADA -> SPRITE STACKING
primeiro_telhado.color(cor_do_fundo)
primeiro_telhado.left(90)
primeiro_telhado.forward(Tamanho_casa)
primeiro_telhado.left(-45)
primeiro_telhado.forward(Tamanho_lateral_casa)
primeiro_telhado.left(-45)
primeiro_telhado.forward(Tamanho_casa)
primeiro_telhado.color("chartreuse4")
cores_telhado = [primeira,segunda,terceira,quarta,quinta]

i2 = 0
while i2 <= Tamanho_lateral_casa:
    r = randint(0,4)
    cor_random = cores_telhado[r]
    primeiro_telhado.color(cor_random)
    primeiro_telhado.begin_fill()
    for i in range(3):
        primeiro_telhado.left(120)
        primeiro_telhado.forward(Tamanho_casa)
    primeiro_telhado.end_fill()
    primeiro_telhado.left(45)
    primeiro_telhado.forward(-1)
    primeiro_telhado.left(-45)
    i2 += 1


primeiro_telhado.left(180)
primeiro_telhado.color(cor_fundo)
primeiro_telhado.forward(2000)




turtle.mainloop()