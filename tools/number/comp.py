
def sumofdigit(num):
    """
    function that return the sum of digits
    """
    sumof = 0
    while num > 0:
        sumof += num % 10 #add the last number to the sumof variable
        num = num // 10 # cut the last digit
    return sumof


def ispal(num):
    "function that chack if a given number is a plindrome"
    str_num = str(num) # convert the number to string so it will be iterable
    pal = True
    for ind in range(len(str_num)//2):
        if str_num[ind] != str_num[-(ind+1)]: # chack the two sides of the string if they equal
            pal = False
    return pal