while True:
    Bp = float(input("Enter Buy Price: "))
    Mv = float(input("Enter Market Value: "))
    Sp = float(input("Enter Sale Price: "))

    Var0 = (Sp - Bp)
    Var1 = ((Mv / Var0)*100)
    Var2 = ((Bp / Var0)*100)
    Var3 = (Var1 - Var2)

    print(f'Buyers comission: {Var3}')
    if input('Continue? Y/N: ')in ('n', 'N'):
        break
