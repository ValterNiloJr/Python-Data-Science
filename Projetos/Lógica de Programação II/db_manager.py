# import csv to manipulate files (database.csv)
import csv

# path to open database.csv
DB_PATH = 'Projetos/Lógica de Programação II/database.csv'

# -----------------------------------
# Funtions that used by db_manager.py
# -----------------------------------

# list all db rows
# params -> none
# return -> List -> rows in database.csv
def list_db_rows():
    list_rows = []
    # Try open database.db with 'read' mode
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';', lineterminator='\n')
            list_rows.extend(reader)

    # Except if database.csv is not found
    except FileNotFoundError:
        print('> ALERTA: Não foi possível abrir o arquivo')

    finally:
        return list_rows

# overwrite all rows in database.csv (basically a truncate function and save new data)
# params -> List -> rows with used as new data (overwrited)
# return -> none
def overwrite_rows(list_rows):
    # Try open database.csv with 'write' mode
    # if database.csv is not exists, 'w' mode creates the file
    try:
        with open(
            DB_PATH, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, 
                                    fieldnames=['id', 'Name', 'Specs', 'Quantity', 'Description'], 
                                    delimiter=';')
            writer.writeheader()
            writer.writerows(list_rows)
    # Except if not open database.csv
    except:
        print('> ALERTA: Não foi possível abrir o arquivo')


# ----------------------------------
# Functions that used by Products.py
# ----------------------------------


# Verify if the ID exists in the database.csv
# params -> int -> ID
# return -> bool -> id exists?
def id_exists(_id):
    # list all rows
    list_rows = list_db_rows()
    # get row index with row[id] equals [id]
    index = next((i for i, d in enumerate(list_rows) if int(d['id']) == _id), -1)
    if index == -1:
        return False
    else:
        return True

# Create a new row in the end of database.csv
# params -> Dict -> new row (dictionary)
# return -> none
def append_row(dicitonary):
    # Try open database.csv with 'append' mode
    try:
        with open(
            DB_PATH, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, 
                                    fieldnames=['id', 'Name', 'Specs', 'Quantity', 'Description'], 
                                    delimiter=';')

            writer.writerow(dicitonary)

    # Except if not open database.csv
    except:
        print('> ALERTA: Não foi possível abrir o arquivo')

    else:
        print('> Produto adicionado com sucesso!')


# Update specific row in database.csv by ID
# params -> Dict -> new row (update)
# return -> none 
def update_row(dictionary):
    # list all rows
    list_rows = list_db_rows()
    # get row index with row[id] equals dictionary[id]
    index = next((i for i, d in enumerate(list_rows) if int(d['id']) == dictionary['id']), -1)

    # change a specific row in list
    if index != -1:
        list_rows[index] = dictionary
    else:
        print('> ALERTA: ID não encontrado')
        return
    # Try open database.csv with 'write' mode
    try:
        with open(DB_PATH, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=['id', 'Name', 'Specs', 'Quantity', 'Description'], 
                                    delimiter=';')
            
            writer.writeheader()
            writer.writerows(list_rows)

    # Except if not open database.csv
    except:
        print('> ALERTA: Não foi possível abrir o arquivo')

# Delete specific row in database.csv by ID
# params -> id -> to delete row
# return -> none
def delete_row(_id):
    # list all rows
    list_rows = list_db_rows()
    # get row index with row[id] equals [id]
    index = next((i for i, d in enumerate(list_rows) if int(d['id']) == _id), -1)

    # if id exists, delete list rows and overwrite database.csv without row was deleted
    if index != -1:
        del list_rows[index]
        overwrite_rows(list_rows)
    else:
        print('> ALERTA: Houve um problema ao encontrar o id')


# Get all produts to show in console
# params -> none
# return -> List -> with all registered products
def get_all_products():
    # Try open database.db with 'read' mode
    try:
        with open(DB_PATH, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';', lineterminator='\n')
            products = []
            for row in reader:
                products.append(row)
        return products
    # Except if file is not found
    except FileNotFoundError:
        print('> ALERTA: Não foi possível abrir o arquivo')


# Get product by id in database.csv
# params -> id -> to return this row (product)
# return -> Dict -> selected row (product) if exists
def get_product_by_id(_id):
    if id_exists(_id):
        list_rows = list_db_rows()
        index = next((i for i, d in enumerate(list_rows) if int(d['id']) == _id), -1)
        return list_rows[index]

# Get last id in database.csv
# params -> none
# return -> int -> last ID
def get_last_id():
    list_rows = list_db_rows()
    return int(list_rows[-1]['id'])


    