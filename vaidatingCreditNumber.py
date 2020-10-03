n = int(input())

_temp = []

num = '0123456789'

for i in range(n):
    a = 0
    b = 0
    cardNumber = list(input())
    # print('first print: ', cardNumber)
    # print('len of card number: ', len(cardNumber))
    if len(cardNumber) == 16 :
        # print('first if working')
        # print(cardNumber[0])
        if cardNumber[0] == '4' or cardNumber[0] == '5' or cardNumber[0] == '6':
            # print('2nd if working')
            for j in cardNumber:
                if j not in num:
                    b += 1
                    # print(b)
                    # print(j)
                
            for k in range(0,13):
                if cardNumber[k] == cardNumber[k+1] == cardNumber[k+2] == cardNumber[k+3]:
                    a += 1
                else:
                    a == a
            if a>0 or b>0:
                print('Invalid')
            else:
                print('Valid')
                
        else:
            print('Invalid')

    elif cardNumber[4] == cardNumber[9] == cardNumber[14] == '-':
        cardNumber.remove(cardNumber[4])
        cardNumber.remove(cardNumber[8])
        cardNumber.remove(cardNumber[12])
        # print(cardNumber,'printing card number')
        if len(cardNumber) == 16 :
        # print('first if working')
        # print(cardNumber[0])
            if cardNumber[0] == '4' or cardNumber[0] == '5' or cardNumber[0] == '6':
                # print('2nd if working')
                for l in cardNumber:
                    if l not in num:
                        b += 1
                        # print(b)
                        # print(l)
                    
                for m in range(0,13):
                    if cardNumber[m] == cardNumber[m+1] == cardNumber[m+2] == cardNumber[m+3]:
                        a += 1
                    else:
                        a == a
                if a>0 or b>0:
                    print('Invalid')
                else:
                    print('Valid')
                    
            else:
                print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')