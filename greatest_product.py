#Bianca
"""
Write a function that, given four numbers, returns the greatest product of two of them. For example, if you receive the numbers 1, 5, -2, -4, you should return 8, which is the largest product that can be obtained between them.
"""
def main():
    print("\n -Program that returns the greatest product of two of for numbers given- \n")
    n1 = float(input("please enter 1st number: "))
    n2 = float(input("please enter 2nd number: "))
    n3 = float(input("please enter 3rd number: "))
    n4 = float(input("please enter 4th number: "))
    answer = greates_product(n1, n2, n3, n4)
    print("The greatest product is: ", answer)

def greates_product(num1, num2, num3,num4):
    max = 0
    p =[num1 * num2, num1 * num3, num1 * num4, num2 * num3, num2 * num4, num3 * num4]
    for product in p:
        if product > max:
            max = product

    return max

main()
