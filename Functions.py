# Function to Find all duplicate elements in list
# @ Params { list, element }
# @ Return { list }
def find_all_in_list(input_list:list, element) -> list:
    indexes = [i for i, x in enumerate(input_list) if x == element]
    return indexes

# Funtion to format printed text 

# Ex:
# name = 'Valter'
# print(f'|{name:^20})
# output -> '       Valter       '

# print(f'|{name:>20})
# output -> '              Valter'

# print(f'|{name:<20})
# output -> 'Valter              '

# @ Params { str }
# @ Return { }
def print_text_format(name:str):
    print(f'|{name:20}|')
    print(f'|{name:>20}|')
    print(f'|{name:<20}|')
    print(f'|{name:^20}|')

