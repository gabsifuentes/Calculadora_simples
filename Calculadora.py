def Soma(num1, num2):
        return num1 + num2

def Subtracao(num1, num2):
        return num1 - num2

def Multiplicacao(num1, num2):
        return num1 * num2
        
def Divisao(num1, num2):
        return num1 / num2


def Main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    match operacao:
           case "+":
                  print(f"O resoltado da soma é: {Soma(num1, num2)}")
           case "-":
                  print(f"O resultado da subtração é: {Subtracao(num1, num2)}")
           case "*":
                  print(f"O resultado da multiplicação é: {Multiplicacao(num1, num2)}")
           case "/":
                  print(f"O resultado da divisão é: {Divisao(num1, num2)}")

Main()
