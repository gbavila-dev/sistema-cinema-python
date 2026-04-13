def menu():
    print("\n===================")
    print("SISTEMA - CINEMA")
    print("===================\n")
    print("1 - Mostrar cadeiras")
    print("2 - Reservar cadeira")
    print("3 - Cancelar reserva")
    print("4 - Mostrar livres")
    print("5 - Calcular resumo")
    print("0 - Sair\n")   

def mostrar_cadeiras(cadeiras):
    print("- Cadeiras:")
    for i in range(len(cadeiras)):
        if cadeiras[i] == 0:
            print(f"[{i+1}: L] ", end=" ")
        else:
            print(f"[{i+1}: O] ", end=" ")
    
    print()


def reservar_cadeira(cadeiras):
    try:
        cadeira = int(input(f"- Insira o número da cadeira (1 a {len(cadeiras)}): "))
        posicao = cadeira - 1

        if posicao >= 0 and posicao < len(cadeiras):
            if cadeiras[posicao] == 0:
                cadeiras[posicao] = 1
                print(f"Cadeira {cadeira} reservada com sucesso!")
            else:
                print("Essa cadeira já está reservada, selecione outra.")
        else:
            print("Número da cadeira inválido!")
    except ValueError:
        print("Insira apenas números!")

def cancelar_reserva(cadeiras):
    try:
        cadeira = int(input("- Insira o número da cadeira (1 a 8): "))
        posicao = cadeira - 1

        if posicao >= 0 and posicao < len(cadeiras):
            if cadeiras[posicao] == 1:
                cadeiras[posicao] = 0
                print(f"Reserva da cadeira {cadeira} cancelada com sucesso!")
            else:
                print("Essa cadeira não está ocupada.")
        else:
            print("Número da cadeira inválido!")
    except ValueError:
        print("Insira apenas números!")
    
def mostrar_livres(cadeiras):
    contador = 0
    
    for i in range(len(cadeiras)):
        if cadeiras[i] == 0:
            contador += 1

    print("- Cadeiras livres: ", end = " ")
    for i in range(len(cadeiras)):
        if cadeiras[i] == 0:
            print(f"{i+1} ", end = " ")        
    print()
    if contador == 0:
        print("Nenhuma cadeira está livre!")
    else:
        print(f"{contador} cadeiras estão livres!")

    

def calcular_resumo(cadeiras):
    contador_l = 0
    contador_r = 0

    for i in range(len(cadeiras)):
        if cadeiras[i] == 0:
            contador_l += 1
        else:
            contador_r += 1

    print("- Resumo:")
    print()
    print(f"Total de cadeiras: {len(cadeiras)}")
    print("-----------------------")
    print(f"Livres: {contador_l} | Ocupadas: {contador_r}")
    print()


cadeiras = [0, 0, 0, 0, 0, 0, 0, 0]
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
                mostrar_cadeiras(cadeiras)
            case 2:
                reservar_cadeira(cadeiras)
            case 3:
                cancelar_reserva(cadeiras)
            case 4: 
                mostrar_livres(cadeiras)
            case 5:
                calcular_resumo(cadeiras)
            case 0:
                print("Desligando o sistema...")
                break
            case _:
                print("Opção inválida!")
main()