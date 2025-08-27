frase = input("Digite uma frase: ")

frase_alterada = frase.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u", "5")
print(f"A frase alterada é: {frase_alterada}") #Aqui eu fiz a parte codificada, com o código atual. o replace usei para substituir um pelo outro

frase_decotificada = frase_alterada.replace("1" , "a").replace("2" , "e").replace("3" , "i").replace("4" , "o").replace("5" , "u")
print(f"A frase decodificada é: {frase_decotificada}")
'''aqui eu criei uma outra variável para decotificar, ai eu tive que fazer o inverso da frase alterada'''