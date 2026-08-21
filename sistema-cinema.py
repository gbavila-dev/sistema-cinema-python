cinema = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append("L")
    cinema.append(linha)

def menu():
    print("\n===================")
    print("SISTEMA - CINEMA")
    print("===================\n")
    print("1 - Mostrar cadeiras")
    print("2 - Reservar cadeira")
    print("3 - Cancelar reserva")
    print("4 - Mostrar resumo")
    print("0 - Sair\n")   

def mostrar_cadeiras(cinema):
    for i in range(len(cinema)):
        for j in range(len(cinema[i])):
            print(f"[{i+1},{j+1}]: {cinema[i][j]}", end=" ")
        print()

def reservar_cadeira(cinema):
    linha = int(input("Fileira: ")) - 1
    coluna = int(input("Coluna: ")) - 1

    if cinema[linha][coluna] == "L":
        cinema[linha][coluna] = "O"
        print("Reservado!")
    else:
        print("Já está ocupado!")

def cancelar_reserva(cinema):
    linha = int(input("Fileira: ")) - 1
    coluna = int(input("Coluna: ")) - 1

    if cinema[linha][coluna] == "O":
        cinema[linha][coluna] = "L"
        print("Cancelado!")
    else:
        print("Essa cadeira já está livre!")
    
def mostrar_resumo(cinema):
    livres = 0
    ocupadas = 0

    for i in range(len(cinema)):
        for j in range(len(cinema[i])):
            if cinema[i][j] == "L":
                livres += 1
            else:
                ocupadas += 1

    print("- Resumo:")
    print()
    print(f"Total de cadeiras: {len(cinema) * len(cinema[0])}")
    print("-----------------------")
    print(f"Livres: {livres} | Ocupadas: {ocupadas}")
    print()

def main():
    while True:
        menu()
        try:
            opcao = int(input("- Escolha uma opção: "))
            print()
        except ValueError:
            print("Insira apenas números!")
            continue

        match opcao:
            case 1:
                mostrar_cadeiras(cinema)
            case 2:
                reservar_cadeira(cinema)
            case 3:
                cancelar_reserva(cinema)
            case 4: 
                mostrar_resumo(cinema)
            case 0:
                print("Desligando o sistema...")
                break
            case _:
                print("Opção inválida!")
main()