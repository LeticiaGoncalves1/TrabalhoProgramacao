# a - print de boas vindas personalizado
print ('   --- Bem-vindo(a) a Loja da Letícia Gonçalves ---   ')
print (' ')

# b - valor unitário e preço do produto
produto = (input('Qual o nome do produto que deseja? '))
preco = float(input('Qual o valor do produto desejado? R$'))
unid = int(input('Quantas unidades você deseja? '))
print (' ')

# c - desconto conforme enunciado
desconto = 0

# d 1 - valor sem desconto
valor_sem_desc = preco * unid

# e - if, elif, else (descontos progressivos)
if valor_sem_desc < 2500:
    desconto = 0

elif valor_sem_desc >= 2500 and valor_sem_desc < 6000:
    desconto = 4

elif valor_sem_desc >= 6000 and valor_sem_desc < 10000:
    desconto = 7

else:
    desconto = 11

# d 1.2 - valor total com desconto
valor_final_com_desc = valor_sem_desc - (valor_sem_desc * desconto / 100)

# g - saída com nome da loja personalizado 
# h - informação da % de desconto aplicado 
if valor_sem_desc >= 2500:
    print (f'A sua compra de {unid} {produto}(s) na Loja da Letícia Gonçalves ficou no valor de R${valor_sem_desc:.2f}, com o desconto de {desconto}% aplicado, o valor final da compra é R${valor_final_com_desc:.2f}.')
else:
    print (f'A sua compra de {unid} {produto}(s) na Loja da Letícia Gonçalves ficou no valor total de R${valor_sem_desc:.2f}, a sua compra não houve desconto aplicado.')

print (' ')
print ('Obrigada pela compra, volte sempre!')

