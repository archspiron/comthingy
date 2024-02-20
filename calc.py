while True:
    BuyPrice = float(input("Enter Buy Price: "))
    MarketValue = float(input("Enter Market Value: "))
    SalePrice = float(input("Enter Sale Price: "))

    TotalComission = (SalePrice - BuyPrice)
    MarketPercentage = ((MarketValue / TotalComission)*100)
    BuyPercentage = ((BuyPrice / TotalComission)*100)
    BuyerComission = (MarketPercentage - BuyPercentage)

    print(f'Buyers comission: {BuyerComission}')
    if input('Continue? Y/N: ')in ('n', 'N'):
        break
