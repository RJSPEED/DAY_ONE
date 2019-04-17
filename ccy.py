"""Logic = Loop through sorted list elements to determine if input_amount
   divides by element, if it does calc how many times and return, along
   with element value. Also deduct the related element amount from the
   input_amount and feed the remainder into the next iteration of the loop.""" 
def currency_converter(input_amount):

    ccy_list = [100,50,10,5,1,0.25,0.10,0.05,0.01]
    list_start_pos = 0
    remainder = 0 
    denom = 0
    denom_count = 0 
    amount = input_amount

    for i in range(len(ccy_list)):
        """First iteration does input_amount divide by first element value,
           subsequent iterations use potetially reducing total.""" 
        if amount / ccy_list[i] > 0:
            list_start_pos = i
            denom = ccy_list[i]
            denom_count = amount // ccy_list[i]
            remainder = amount - ((amount // ccy_list[i])*ccy_list[i])
            if int(denom_count) > 0:
                print(int(denom_count)," ", denom)
        amount = remainder
    
  
currency_converter(12.33)