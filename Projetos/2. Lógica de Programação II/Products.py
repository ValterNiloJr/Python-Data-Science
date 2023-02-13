# os to use 'cls' command with OS System (Windows)
import os
# ast to use literal_eval to convert string to list
from ast import literal_eval
# db_manager is auxiliary functions code to manage database
import db_manager as db

# Function to clear output on console with 'cls' command (windows)
def clear_output(): os.system('cls')

# Text Options
OPTION_1 = 'Cadastrar Produto'
OPTION_2 = 'Consultar Produto'
OPTION_3 = 'Listar Produtos Cadastrados'
OPTION_4 = 'Atualizar Cadastro'
OPTION_5 = 'Excluir Cadastro'
OPTION_6 = 'Sair'

# formatted print on console based on the dictionary list
def formatted_print(list_dictionary, specs=True, quantity=True, description=True):
    # for each row in list dictionary -> data
    # get:
    # ID: id_value
    # Nome: name_value
    # > Especificações:
    # >> spec_name: spec_value
    for row in list_dictionary:
        print('-------------------------------')
        print(f"ID: {row['id']}")
        print(f"Nome: {row['Name']}")
        if specs:
            print("> Especificações:")
            list_specs = (literal_eval(row['Specs']))
            
            for i in range(len(list_specs[0])):
                print(f">> {list_specs[0][i]}: {list_specs[1][i]}")
        
        if quantity: 
            print(f"Quantidade no estoque: {row['Quantity']}")

        if description:
            print(f"Descrição: {row['Description']}")


# Register new product (id, name, specs, quantity, description)
def register_product(is_update=False, _id=0):
    if is_update == False:
        # Clear output with 'cls' command -> for windows
        clear_output()
        print(f'Opção selecionada: {OPTION_1}')
        # if is not update, get last id in database + 1
        _id = db.get_last_id() + 1

    # dict of Specs with [[name] and [feature]]
    specs = [[], []]
    description = ''
    # Get Product Name
    name = input('Informe o nome do produto: ')
    if name.strip().lower() == 'voltar':
        clear_output()
        menu()
    # ----------------------------------------------------------------
    # Ask about Specs
    # yes -> Get Spec Name and Get Spec Feature
    # no  -> break
    while True:
        add_spec = input('Adicionar Especificação? (Sim / Não): ')
        if add_spec.lower().strip() == 'não':
            break
        elif add_spec.lower().strip() == 'sim':
            specs[0].append(input('> Especificação: '))
            specs[1].append(
                input(f'>> {specs[0][-1]}: '))
        else:
            print('> ALERTA: Responda com \'Sim\' ou \'Não\'')

    # ----------------------------------------------------------------
    # Quantity
    # Accept negative quantity (for future sales)
    while True:
        # Try get a numeric value (float)
        try:
            quantity = float(
                input('Informe a quantidade do Produto no estoque: '))
        # Except if user input is not a numeric value 
        except ValueError:
            print('> ALERTA: A quantidade deve ser um valor numérico!')
        else:
            break

    # ----------------------------------------------------------------
    # Ask about Description
    # yes -> Get Description text
    # no  -> break
    while True:
        add_description = input('Adicionar Descrição? (Sim / Não): ')
        if add_description.lower().strip() == 'não':
            break
        elif add_description.lower().strip() == 'sim':
            description = input('Texto: ')
            break
        else:
            print('> ALERTA: Responda com \'Sim\' ou \'Não\'')

    # create a dictionary with register new product
    product = {'id': _id, 'Name': name, 'Specs': specs,
               'Quantity': quantity, 'Description': description}
    
    if is_update:
        # Update product row by 'product' id 
        db.update_row(product)
    else:
        # Create new row to insert 'product'
        db.append_row(product)
    menu()

# Consult product by id
def consult_product():
    clear_output()
    print(f'Opção selecionada: {OPTION_2}')
    # ----------------------------------------------------------------
    # Await valid ID -> is on the database
    while True:
        # Try get product id to delete in database
        try:
            _id = int(input('Informe o ID do produto: '))
            if db.id_exists(_id):
                break
            else:
                print('> ALERTA: ID não encontrado')
        # Except if id is not found
        except ValueError:
            print('> ALERTA: O ID deve ser um valor numérico')
    
    # Formatted print requires a list of dictionaries and the 
    # query is made with only one item, it is passed as a list
    formatted_print([db.get_product_by_id(_id)])
    menu()

# List all registered products
def list_registered_products():
    clear_output()
    print(f'Opção selecionada: {OPTION_3}')
    products = db.get_all_products()
    formatted_print(products)
    menu()

# Update one product in database by id
# Redirect to register_product with 'is_update = True'
def update_register():
    clear_output()
    print(f'Opção selecionada: {OPTION_4}')
    # ----------------------------------------------------------------
    # Await valid ID -> is on the database
    while True:
        # Try get product id to delete in database
        try:
            _id = int(input('Informe o ID do produto: '))
            if db.id_exists(_id):
                break
            else:
                print('> ALERTA: ID não encontrado')
        # Except if id is not found
        except ValueError:
            print('> ALERTA: O ID deve ser um valor numérico')

    # call register_product with 'is_update = True'
    register_product(is_update=True, _id=_id)
    menu()

# Delete one product in database by id
# ID is never used again
def delete_register():
    clear_output()
    print(f'Opção selecionada: {OPTION_5}')
    # ----------------------------------------------------------------
    # Await valid ID -> that is on the database
    while True:
        # Try get product id to delete in database
        try:
            _id = int(input('Informe o ID do produto: '))
            if db.id_exists(_id):
                break
            else:
                print('> ALERTA: ID não encontrado')
        # Except if id is not found
        except ValueError:
            print('> ALERTA: O ID deve ser um valor numérico')

    db.delete_row(_id)
    menu()

# MENU state for await input option to user
def menu():
    # Try get user option
    try:
        # user option (input)
        option = (input(f'''
    --- MENU ---

1 - {OPTION_1}
2 - {OPTION_2}
3 - {OPTION_3}
4 - {OPTION_4}
5 - {OPTION_5}
6 - {OPTION_6}

-> '''))

        # dict with user options for call funtions
        options = {
            '1': register_product,
            '2': consult_product,
            '3': list_registered_products,
            '4': update_register,
            '5': delete_register
        }

        # Exit option -> return
        if option == '6':
            return

        # Execute function on dict 'options' value by key 'option (input)'
        options[option]()

    # Except if key is not found on dictionary options
    except KeyError:
        clear_output()
        print(option)
        print('> ALERTA: Opção inválida ou não encontrada!')
        menu()

# Ensures that this code will run not to be executed by other code
if __name__ == '__main__':
    # Clear console output with 'cls' command -> for windows
    clear_output()
    # Welcome message
    print('Seja bem vindo ao sistema de produtos Let\'s Code')
    # Call menu state
    menu()
    # THE END
    print('    --- FIM ---')
