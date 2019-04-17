def divisor_list(input_integer):
    div_list = []
    for num in range(1,input_integer+1):
        if input_integer % num == 0:
            div_list.append(num);
    return div_list

def divisor_sum(input_integer):
    div_sum = 0
    for num in range(1,input_integer+1):
        if input_integer % num == 0:
            div_sum = div_sum + num
    return div_sum

def divisor_main(my_num):
    my_list = []
    my_list.append(divisor_list(my_num))
    my_list.append(divisor_sum(my_num))
    my_list.append(len(divisor_list(my_num)))
    print(my_list)

divisor_main(60)
   
