#Gerenciador de senhas com Python - Kauan
# @Author: Kauan Rezende
# @Date:   2023-05-23 10:52:13

import random 

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%^&*()!"

for_pass = lower_case + upper_case + numbers + symbols

tamanho_da_senha = 12

password = "".join(random.sample(for_pass, tamanho_da_senha))

print("Minha senha é: " + password)
