# currency converter

def curr_conv(from_curr,to_curr,amt):
    price={
        'USD':1.0,
        'INR':89.99,
        'EURO':.85,
        'YEN':110.53,
        'GBP':0.75,
        
        
    }
    if from_curr not in price or to_curr not in price:
        print("Currency not supported")
        return None
    
    in_usd=amt/price[from_curr]
    converted_amt=in_usd*price[to_curr]
    return converted_amt

print("Currency Converter")
print("Currencies Supported:USD,INR","EURO","YEN","GBP")


amt=float(input("Enter amount:"))
from_curr=input("From Currency:").upper()
to_curr=input("To Currency:").upper()

outcome=curr_conv(from_curr,to_curr,amt)

if outcome is not None:
    print(f"{amt:.2f} {from_curr} = {outcome:.2f} {to_curr}")