listaNum=[]

num=float(input("Digite o primeiro numero. "))

while num != 0:
    listaNum.append(num)
    num=float(input("Digite outro numero. "))

tam=len(listaNum)-1

while tam >= 0:
    print(listaNum[tam])
    tam=tam -1