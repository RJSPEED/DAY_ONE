#a = [[1, 2, 3], [4, 5, 6]]
#print(a[1][1])

#UNFINISHED
def print_list(my_list):
    #print(len(my_list))   
    """Loop through list elements."""
    for i in range(len(my_list)):
        """Can't use len() on an integer which is the first element,
           need to somehow check datatype of element ?"""
        for j in range(len(my_list[i])):
            print(my_list[i][j])

my_list = [1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]]

print_list(my_list)
