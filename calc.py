while True:
    Bp = float(input("Enter Buy Price: "))
    Mv = float(input("Enter Market Value: "))
    Sp = float(input("Enter Sale Price: "))
    
    Var1 = ((Mv / Sp)*100)
    Var2 = ((Bp / Sp)*100)
    Var3 = (Var1 - Var2)

    print(f'Buyers comission: {Var3}')
