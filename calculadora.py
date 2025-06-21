class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero!")
        return a / b

def exibir_menu():
    print("Menu:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")
    print("")
    escolha = input("Escolha uma opção: ")
    print("")
    if escolha not in ['1', '2', '3', '4', '5']:
        print("Opção inválida! Tente novamente.")
        return exibir_menu()
    return escolha

def main():
    calculator = Calculadora()
    while True:
        escolha = exibir_menu()
        if escolha == '1':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {calculator.somar(a, b)}")
            print("")
        elif escolha == '2':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {calculator.subtrair(a, b)}")
            print("")
        elif escolha == '3':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            print(f"Resultado: {calculator.multiplicar(a, b)}")
            print("")
        elif escolha == '4':
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
            try:
                print(f"Resultado: {calculator.dividir(a, b)}")
                print("")
            except ValueError as e:
                print(e)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()