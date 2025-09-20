import os

restaurants = [
    {
        'name': 'Praça',
        'category': 'Japonesa',
        'active': False
    },
    {
        'name': 'Pizza Suprema',
        'category': 'Pizza',
        'active': True
    },
    {
        'name': 'Cantina',
        'category': 'Italiana',
        'active': True
    }
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
    text_length = '*'  * (len(text))
    print(text_length)
    print(text)
    print(text_length)

def show_options():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alterar restaurante")
    print("4. Sair\n")

def close_app():
    show_title("Exit")

def invalid_options():
    print('invalid options! \n')
    back_home()

def create_a_new_restaurant():
    show_title("Restaurant registered")
    restaurant_name = input("Digite o nome do restaurante: ")
    category = input("Digite o nome da categoria do restaurante: ")

    restaurantModel = {
        'name': restaurant_name,
        'category': category,
        'active': False
    }

    restaurants.append(restaurantModel)
    print(f"O restaurante {restaurant_name} foi cadastrado")
    back_home()

def get_all_restaurants():
    show_title("list restaurant")
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria do restaurante'.ljust(22)} | {'Status'.ljust(22)}")
    for r in restaurants:
        active = "ativado" if r["active"] else "desativado" 
        print(f"- {r["name"].ljust(20)} | {r["category"].ljust(20)} | {active}")

    input("\n Digite uma tecla para voltar para a tela principal")
    main()

def update_restaurant_status():
    show_title("Alterando o estado do restaurante")
    restaurant_name = input("Digite o nome do restaurante")
    restaurant_find = False

    for r in restaurants:
        if restaurant_name == r['name']:
            restaurant_find = True
            r['active'] = not r['active']
            message = f'O restaurante {restaurant_name} foi encontrado com sucesso' if r['active'] else f"O restaurante foi desativado"
            print(message)

        if not restaurant_find:
            print("Restaurante n encontrado")

def selectOptions():
    try:
        option = int(input("Escolha uma opção:"))

        print(f"Você escolheu a opção {option}")
        print(type(option))

        if option == 1:
            create_a_new_restaurant()
        elif option == 2:
            get_all_restaurants()
        if option == 3:
            update_restaurant_status()
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
