import requests

def add(num1, num2):
    response = requests.get(f'http://backend:5000/api/add?num1={num1}&num2={num2}')
    return response.text


def subtract(num1, num2):
    response = requests.get(f'http://backend:5000/api/subtract?num1={num1}&num2={num2}')
    return response.text


def multiply(num1, num2):
    response = requests.get(f'http://backend:5000/api/multiply?num1={num1}&num2={num2}')
    return response.text


def divide(num1, num2):
    response = requests.get(f'http://backend:5000/api/divide?num1={num1}&num2={num2}')
    return response.text

def invalid():
    return "Invalid Input"


def calc(choice):
    if choice not in ('1', '2', '3', '4'):

        return "Invalid Input"

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        return str(num1) + " + " + str(num2) + " = " + str(add(num1, num2))

    if choice == '2':
        return str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2))

    if choice == '3':
        return str(num1) + " * " + str(num2) + " = " + str(multiply(num1, num2))

    if choice == '4':
        return str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2))

    return None

def main():
    while True:
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")

        # take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        print(calc(choice))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break


if __name__ == "__main__":
    main()
