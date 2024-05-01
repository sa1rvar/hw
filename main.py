#task1
def check(lst, num):
    return num in lst

print(check([1,2,3,4,5], 3))
print(check([1,1,2,1,1,],3))
print(check([5,5,5,6], 5))
check([],5)

def list_less_than_100(lst):
    the_sum_number = 0
    for number in lst:
        the_sum_number += number
    return the_sum_number < 100

print(list_less_than_100([5, 57]))
print(list_less_than_100([77,30]))
print(list_less_than_100([0]))

def max_total(lst):
    lst.sort(reverse=True)
    number = 0
    for x in range(5):
        number += lst[x]
        return number

print([1,1,0,1,3,10,10,10,10,1])
print([0,0,0,0,0,0,0,0,0,10])
print([1,2,3,4,5,6,7,8,9,10])






