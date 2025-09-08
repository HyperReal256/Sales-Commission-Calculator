'''
making use of the return function
'''

def main():
    first_age = int(input('Enter your age: '))
    second_age = int(input('Enter your friend age: '))
    total = sum(first_age, second_age)
    print("Together you are ", total, "years old")

def sum(first_age, second_age):
    result = first_age + second_age
    return result

main()


