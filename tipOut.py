# tipOut function to streamline end of night

def tipOut(totalTips, numBartenders, numBarbacks, numBouncers):
    
    if numBarbacks < 0 or numBartenders < 0 or numBouncers < 0:
        raise ValueError("Invalid Values")

    # Holder variables for how much each position makes
    bartenderPay = 1
    barbackPay = bartenderPay/3
    bouncerPay = bartenderPay/4

    totalPay = (numBartenders * bartenderPay) + (numBarbacks * barbackPay) + (numBouncers * bouncerPay)

    if totalPay == 0:
        raise ValueError("Invalid Values")

    tipPerPerson = totalTips/totalPay

    print("Bartenders: $" + "{:.2f}".format(tipPerPerson * bartenderPay))
    print("")
    print("Barbacks: $" + "{:.2f}".format(tipPerPerson * barbackPay))
    print("")
    print("Bouncers: $" + "{:.2f}".format(tipPerPerson * bouncerPay))