import os
table=["|"," ","-"]
matrix=[["1","2","3"],["4","5","6"],["7","8","9"]]
vitoria=[[1,2,3],[4,5,6],[7,8,9],[1,5,]
ganhou=False
posicaox=[]
posicaoo=[]
combinacoes=[[0,0],[0,1],[0,2]],[[0,0],[1,1],[2,2]],[[1,0],[1,1],[1,2]]
vencedor=""
def principal():
    print()
#_    os.system("clear")
    print("        Bem vindo ao jogo!\n")
    
    for item in matrix:
        t=2
        for c in item:
            if t>0:
                print("    {}    {}".format(c,table[0]),end="")
                t=t-1
            else: print("    {}    ".format(c),end="")
        print()

#        print(table[0],table[2],table[0],table[2],table[0],table[2],table[0])
#    posicao
def percorre(var,l):
    for c in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[c][i]==var:
                matrix[c][i]=l
                if l=="X":
                    posicaox.append([c,i])
                
                else:
                    posicaoo.append([c,i])
                verificador()

def verificador():
    for c in range(len(combinacoes)):
      #   for i in range(3):
             
        if combinacoes[c] in posicaox:
            ganhou=True
            vencedor="X"

        elif combinacoes[c] in posicaoo:
            ganhou=True
            vencedor="O"
        print("        {}x\n        {}o\n        {}".format(posicaox,posicaoo,combinacoes[c]))
        print("        {}em x\n        {}em o".format(combinacoes[c] ==  posicaox,combinacoes[c] in posicaoo))

def ttt():
    while not ganhou:
        x=input("Selecione uma posicao para o x: ")
        percorre(x,"X")
        if vencedor=="X":
            break
        else:
            principal()

        o=input("Selecione uma posicao para o o: ")
        percorre(o,"O")
        if vencedor=="O":
            break
        else:
            principal()    
    print("Parabens jogador {vencedor}!")

    #for i in range(3):
        #print("{}{}".format("|---------"*3,"|"))
        #for c in range(9):
            #print("{}{}".format("|         "*3,"|"))

    #print("{}{}".format("|---------"*3,"|"))



if __name__ == "__main__":
    principal()
    ttt()
