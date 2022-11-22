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
    for a in range (0,3):
        if(a==posV):
            for b in range (0,3):
                if(b==posH):
                    print("X")
                else:
                    print("_",end='')
        else:
            for b in range (0,3):
                print("_",end='')
        print()
