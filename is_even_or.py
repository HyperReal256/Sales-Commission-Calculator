
'''
rewriting the sames program
'''
num = int(input("Enter a number:"))
def is_even(num):
    if num % 2 == 0:
        status = True
    else:
        status = False
    return status

if is_even(num):
    print(f"The number {num} is even")

else:
    print(f"{num} is an odd number")
