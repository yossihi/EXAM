from icecream import ic
from number.simp import adding, subtracting
from number.comp import sumofdigit, ispal
import sys


simp_call = False # flag to check if we called one of the simp module functions

def adding_test():
    test = True
    global simp_call # change the flag
    simp_call = True
    if adding(2, 3) != 5 or adding(-5, 7) != 2 or adding(0, 4) != 4: # check the adding function in 3 scenarios
        ic('adding function test failed')
        test = False # tests pailed
    return test # tests pass


def subtracting_test():
    test = True
    global simp_call
    simp_call = True
    if subtracting(2, 3) != -1 or subtracting(-5, 7) != -12 or subtracting(0, 4) != -4: # check the subtracting function in 3 scenarios
        ic('subtracting function test failed')
        test = False # tests pailed
    return test # tests pass

def sumof_test():
    if simp_call:
        test = True
        if sumofdigit(234) != 9 or sumofdigit(5) != 5: # check the sumofdigit function in two scenarios
            ic('sumofdigit function tests are failed')
            test = False # tests pailed
        return test # tests pass
    else: 
        raise Exception("Cannot call functions in comp module before calling at least one function in simp module") # no simp functions call

def ispal_test():
    if simp_call:
        test = True
        if not ispal(101) or not ispal(10201) or not ispal(1) or ispal(123): # check the ispal function
            ic('ispal function test failed')
            test = False # tests pailed
        return test # tests pass
    else: 
        raise Exception("Cannot call functions in comp module before calling at least one function in simp module") # no simp functions call




def main():
    # call all the four functions.
    if subtracting_test() and sumof_test() and ispal_test() and adding_test():
        ic('all tests passed')

if __name__ == '__main__':
    main()