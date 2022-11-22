#partie 2
#exercice 2
joueur1="X"
joueur2="0"
ordre = 0
print("tic tac toe")


if(ordre==0):
    #position horizontal
    print("horizontal")
    posH=input()
    #position vertical
    print("vertical")
    posV=input()
    for a in range (1,4):
        if(a==posH):
            for b in range (1,4):
                if(b==posV):
                    print("X",end='')
                else:
                    print("_",end='')
        else:
            for b in range (0,3):
                print("_",end='')
        print()
