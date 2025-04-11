def main(): 
    while True:
     idade = 0
     print("\n Qual a sua Idade? \n")
     idade = int(input("Digite a sua idade: "))

     if  idade <13:
       print("Você é uma criança! saia já daqui!")

     elif 13 <= idade <= 17:
      print("você é um adolescente! VAI ESTUDAR")

     elif 18 <= idade <= 59:
      print("Você é um adulto! E a vida amorosa?")

     else:
      print("você é um idoso! A aposentadoria atrasou de novo seu Jorge?!")
        
if __name__ == "__main__": 

    main()
        