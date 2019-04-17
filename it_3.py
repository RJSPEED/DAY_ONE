
def list_stats(my_list):
    mean_tot = 0
    mean_count = 0
    mode = None
    mode_count = 0
    for i in my_list:
        """Loop through list elements counting how many times each element
           occurs in list. If the count > than prev saved count then
           overwrite the count and assign that element as the mode."""
        if my_list.count(i) > mode_count:
            mode_count = my_list.count(i)
            mode = i
        """Loop through all list elements creating a cum total and 
           element count.""" 
        mean_tot = mean_tot + i
        mean_count = mean_count + 1

    """Median related"""
    sorted_list = sorted(my_list)
    odd_element_placer = ((len(my_list)-1)//2)
    even1_element_placer = ((len(my_list)-1)//2)
    even2_element_placer = ((len(my_list)-1)//2)+1
    """If list has even number of elements."""
    if len(my_list) % 2 == 0:
        print(int((sorted_list[even1_element_placer]+sorted_list[even2_element_placer])/2.0))            
    """Odd number."""
    else:
        print(sorted_list[odd_element_placer])

    print(int(mean_tot/mean_count))
    print(mode)

my_list = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]
#my_list = [1,2,3,4]

list_stats(my_list)
