'''
Escreva um programa que leia um texto e imprima uma versão
codificada ou decodificada dele. A criptografia deve ser boa. O usuário deve escolher a ação que deseja realizar.

'''
# Importa a Biblioteca Para Gerar Numeros Aleatórios
import random

alfabeto=' abcdefghijklmnopqrstuvwxyz'
chave_texto=0
# Solicita o texto e armazena ela em uma variável.
texto=input('Digite um texto somente letras: ')

# Solicita se quer Criptografar texto ou converte de Criptografia para texto normal
criptografar=input('Digite "C" para Criptografar, ou "D" para Descriptografar: ')

# Checa se a Informação está correta
if criptografar=='C' or criptografar=='D':
    print('OK. Sigamos a Diante.')

    if criptografar=='C':
        contar=0
        texto_criptografado=''
        # Converte texto em Minúsculo
        texto=texto.lower()
        print(f'Texto em Minusculo: {texto}')

        # Gera A Chave de Criptografia
        chave_texto=random.randrange(1,5)
        print(f'A Chave Para Seu Texto é: {chave_texto}')

        # Precorrer o Texto
        posicao=0
        for i in texto:
            posicao =alfabeto.find(i)
            posicao = posicao + chave_texto
            texto_criptografado += alfabeto[posicao]

        #Recebe a Chave da Criptografia
        texto_criptografado = texto_criptografado + str(chave_texto)
        print(f'Anote Seu Texto Criptografado: {texto_criptografado}')
    else:
        texto_criptografado=texto.lower()  

#('Digite o Texto Criptografado: ')         texto_criptografado=texto_criptografado.lower()
        
        chave_texto=texto_criptografado[-1]
        print(texto_criptografado)
        texto_criptografado=texto_criptografado.replace(chave_texto,'')
        print(texto_criptografado)
        
        # Precorrer o Texto
        posicao=0
        texto=''
        for i in texto_criptografado:
            posicao = alfabeto.find(i)
            posicao = posicao - int(chave_texto)
            texto += alfabeto[posicao]

        #Recebe Texto Descriptografado
#        texto_criptografado = texto_criptografado + str(chave_texto)
        print(f'Seu Texto Criptografado é: {texto}')

else:
    print('Digite os Dados Corretamente!')



'''
        # Precorrer o Texto Criptografado
        for i in texto:
            teste =alfabeto.find(i)
            teste = teste + chave_texto
            #texto_criptografado += texto_criptografado.replace()
            
            alfabeto[teste]

'''



