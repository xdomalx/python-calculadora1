# Função para adicionar
def add(x, y):
    return x + y

# Função para subtrair
def subtract(x, y):
    return x - y

# Função para multiplicar
def multiply(x, y):
    return x * y

# Função para dividir
def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        choice = input("Digite o número da operação desejada (1/2/3/4): ")

        # Verificar se a escolha é válida
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        else:
            print("Opção inválida! Por favor, escolha uma operação válida (1/2/3/4).")

        # Perguntar se o usuário deseja continuar
        next_calculation = input("Deseja realizar outra operação? (sim/não): ").lower()
        if next_calculation != 'sim':
            break

if __name__ == "__main__":
    calculator()
