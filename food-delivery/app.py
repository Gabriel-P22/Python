import os

restaurants = [
    'Pizza',
    'Hamburguer'
]

def show_project_name():
    print("""      
        
    ███████╗░█████╗░░█████╗░██████╗░  ██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░██╗░░░██╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗╚██╗░██╔╝
    █████╗░░██║░░██║██║░░██║██║░░██║  ██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝░╚████╔╝░
    ██╔══╝░░██║░░██║██║░░██║██║░░██║  ██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗░░╚██╔╝░░
    ██║░░░░░╚█████╔╝╚█████╔╝██████╔╝  ██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░
    ╚═╝░░░░░░╚════╝░░╚════╝░╚═════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
        
    """)

def back_home():
    input("\n Digite uma tecla para voltar para a tela principal")
    main()

def show_title(text):
    os.system('clear')
    print(text)

def show_options():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def close_app():
    show_title("Exit")

def invalid_options():
    print('invalid options! \n')
    back_home()

def create_new_restaurant():
    show_title("Restaurant registered")
    restaurant_name = input("Digite o nome do restaurante: ")
    restaurants.append(restaurant_name)
    print(f"O restaurante {restaurant_name} foi cadastrado")
    back_home()

def show_restaurants():
    show_title("list restaurant")
    for r in restaurants:
        print(f".{r}")

    input("\n Digite uma tecla para voltar para a tela principal")
    main()

def selectOptions():
    try:
        option = int(input("Escolha uma opção:"))

        print(f"Você escolheu a opção {option}")
        print(type(option))

        if option == 1:
            create_new_restaurant()
        elif option == 2:
            show_restaurants()
        if option == 3:
            print("Valid Option")
        if option == 4:
            close_app()
        else: 
            invalid_options()
    except:
        invalid_options()

def main():
    os.system('clear')
    show_project_name()
    show_options()
    selectOptions()

if __name__ == '__main__':
    main()
