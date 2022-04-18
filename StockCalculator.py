#Delara Daryaei
#This program computes the transactions of stock

    
def load()->(str, int, float, float, float):
    '''Let user input a string an integer and 3 floats'''
    #User enters cost of purchasing and selling a stock
    stockName = input("\nEnter Stock name: ")
    numberOfShares = int(input("Enter Number of shares : "))
    purchasePrice = float(input("Enter Purchase price : "))
    sellingPrice = float(input("Enter selling price : "))
    commission = float(input("Enter Commission : "))
    
    return stockName, numberOfShares, purchasePrice, sellingPrice, commission


def calc(numberOfShares : int, purchasePrice : float, sellingPrice : float, commission : float) -> (int, float):
    '''Calculate the amount paid, selling amount, commision during purchase and sale, and profit/loss of inputed stock'''
    #Calculate transaction costs of stock
    amountPaid = numberOfShares * purchasePrice
    commissionPurchase = amountPaid * commission
    sellingAmount = numberOfShares * sellingPrice
    commissionSale = sellingAmount * commission
    profitLoss = (sellingAmount - commissionSale)-(amountPaid + commissionPurchase) 

    return amountPaid, commissionPurchase, sellingAmount, commissionSale, profitLoss


def output(stockName : str, amountPaid : float, commissionPurchase : float, sellingAmount : float, commissionSale : float, profitLoss : float) -> None:
    '''Prints data passed into the function'''
    #Display the transaction costs of stock calculated from user inputed data
    print ("\n\nStock Name : ", format(stockName))
    print ("Amount paid for the stock:            $", format(amountPaid, '13,.2f'))
    print ("Commission paid on the purchase:      $", format(commissionPurchase, '13,.2f'))
    print ("Amount the stock sold for:            $", format(sellingAmount, '13,.2f'))
    print ("Commission paid on the sale:          $", format(commissionSale, '13,.2f'))
    print ("Profit (or loss if negative):         $", format(profitLoss, '13,.2f'))


def main():
    while True:
        choice = input("\nEnter your stock information? Type 'y' for yes, or 'n' for no: ")
        if choice == 'n':
            return
        
        stockName, numberOfShares, purchasePrice, sellingPrice, commission = load()
        amountPaid, commissionPurchase, sellingAmount, commissionSale, profitLoss = calc(numberOfShares, purchasePrice, sellingPrice, commission)
        output(stockName, amountPaid, commissionPurchase, sellingAmount, commissionSale, profitLoss)
        

if __name__=="__main__":
    main()
    

##Test Run 1
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: Kaplack, Inc.
##Enter Number of shares : 10000
##Enter Purchase price : 33.92
##Enter selling price : 35.92
##Enter Commission : 0.04
##
##
##Stock Name :  Kaplack, Inc.
##Amount paid for the stock:            $    339,200.00
##Commission paid on the purchase:      $     13,568.00
##Amount the stock sold for:            $    359,200.00
##Commission paid on the sale:          $     14,368.00
##Profit (or loss if negative):         $     -7,936.00
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: IBM
##Enter Number of shares : 15000
##Enter Purchase price : 50.25
##Enter selling price : 100.2
##Enter Commission : 0.02
##
##
##Stock Name :  IBM
##Amount paid for the stock:            $    753,750.00
##Commission paid on the purchase:      $     15,075.00
##Amount the stock sold for:            $  1,503,000.00
##Commission paid on the sale:          $     30,060.00
##Profit (or loss if negative):         $    704,115.00
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
    
##Test Run 2
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
    
##Test Run 3
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: TGT
##Enter Number of shares : 500
##Enter Purchase price : 212.22
##Enter selling price : 250.75
##Enter Commission : 0.03
##
##
##Stock Name :  TGT
##Amount paid for the stock:            $    106,110.00
##Commission paid on the purchase:      $      3,183.30
##Amount the stock sold for:            $    125,375.00
##Commission paid on the sale:          $      3,761.25
##Profit (or loss if negative):         $     12,320.45
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: FB
##Enter Number of shares : 3000
##Enter Purchase price : 222.36
##Enter selling price : 200
##Enter Commission : 0.02
##
##
##Stock Name :  FB
##Amount paid for the stock:            $    667,080.00
##Commission paid on the purchase:      $     13,341.60
##Amount the stock sold for:            $    600,000.00
##Commission paid on the sale:          $     12,000.00
##Profit (or loss if negative):         $    -92,421.60
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: V
##Enter Number of shares : 1000
##Enter Purchase price : 221.77
##Enter selling price : 321.28
##Enter Commission : 0.05
##
##
##Stock Name :  V
##Amount paid for the stock:            $    221,770.00
##Commission paid on the purchase:      $     11,088.50
##Amount the stock sold for:            $    321,280.00
##Commission paid on the sale:          $     16,064.00
##Profit (or loss if negative):         $     72,357.50
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
    
##Test Run 4
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: AMZN
##Enter Number of shares : 5500
##Enter Purchase price : 3259.95
##Enter selling price : 3365.96
##Enter Commission : 0.03
##
##
##Stock Name :  AMZN
##Amount paid for the stock:            $ 17,929,725.00
##Commission paid on the purchase:      $    537,891.75
##Amount the stock sold for:            $ 18,512,780.00
##Commission paid on the sale:          $    555,383.40
##Profit (or loss if negative):         $   -510,220.15
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: Y
##
##Enter Stock name: MCD
##Enter Number of shares : 2500
##Enter Purchase price : 247.28
##Enter selling price : 198.96
##Enter Commission : 0.02
##
##
##Stock Name :  MCD
##Amount paid for the stock:            $    618,200.00
##Commission paid on the purchase:      $     12,364.00
##Amount the stock sold for:            $    497,400.00
##Commission paid on the sale:          $      9,948.00
##Profit (or loss if negative):         $   -143,112.00
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: NEnter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: AMZN
##Enter Number of shares : 5500
##Enter Purchase price : 3259.95
##Enter selling price : 3365.96
##Enter Commission : 0.03
##
##
##Stock Name :  AMZN
##Amount paid for the stock:            $ 17,929,725.00
##Commission paid on the purchase:      $    537,891.75
##Amount the stock sold for:            $ 18,512,780.00
##Commission paid on the sale:          $    555,383.40
##Profit (or loss if negative):         $   -510,220.15
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: MCD
##Enter Number of shares : 2500
##Enter Purchase price : 247.28
##Enter selling price : 198.96
##Enter Commission : 0.02
##
##
##Stock Name :  MCD
##Amount paid for the stock:            $    618,200.00
##Commission paid on the purchase:      $     12,364.00
##Amount the stock sold for:            $    497,400.00
##Commission paid on the sale:          $      9,948.00
##Profit (or loss if negative):         $   -143,112.00
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##
    
##Test Run 5
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: MA
##Enter Number of shares : 1000
##Enter Purchase price : 357.38
##Enter selling price : 399.65
##Enter Commission : 0.02
##
##
##Stock Name :  MA
##Amount paid for the stock:            $    357,380.00
##Commission paid on the purchase:      $      7,147.60
##Amount the stock sold for:            $    399,650.00
##Commission paid on the sale:          $      7,993.00
##Profit (or loss if negative):         $     27,129.40
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: y
##
##Enter Stock name: WMT
##Enter Number of shares : 25000
##Enter Purchase price : 148.92
##Enter selling price : 239.76
##Enter Commission : 0.05
##
##
##Stock Name :  WMT
##Amount paid for the stock:            $  3,723,000.00
##Commission paid on the purchase:      $    186,150.00
##Amount the stock sold for:            $  5,994,000.00
##Commission paid on the sale:          $    299,700.00
##Profit (or loss if negative):         $  1,785,150.00
##
##Enter your stock information? Type 'y' for yes, or 'n' for no: n
##


