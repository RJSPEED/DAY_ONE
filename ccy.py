"""Logic = Divide float by largest list element, if amount divides remains move to next
   element and iterate using remaining amount ... if amount not divisibe move
   to next number in list.""" 
def currency_converter(input_amount):

    ccy_list = [100,50,10,5,1,0.25,0.10,0.05,0.01]
    list_start_pos = 0
    remainder = 0 
    denom = 0
    denom_count = 0 
    amount = input_amount

    """Determine the highest denom."""
    for i in range(len(ccy_list)):
        """If amount is divisible by element."""
        if amount / ccy_list[i] > 0:
            list_start_pos = i
            denom = ccy_list[i]
            denom_count = amount // ccy_list[i]
            remainder = amount - ((amount // ccy_list[i])*ccy_list[i])
            if int(denom_count) > 0:
                print(int(denom_count)," ", denom)
            #print(remainder)
        amount = remainder
    
  
currency_converter(12.33)