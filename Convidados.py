# @Author: Kauan Rezende
# @Date:   2023-05-29 10:50:55

convidado = input("Escreva o nome do convidado: ")
#caso tenha mais participantes na lista de convidados, adiciona-los abaixo entre as aspas
if convidado in ["Miriam", "Raphael", "Marcos", "Kauan", "", "", "", "", "", "", "", "", "",]:
    print(convidado+ " " + "esta liberado para a festa!")

else:
    print(convidado+ " " + "não está na lista!")
