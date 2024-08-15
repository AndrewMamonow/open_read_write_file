# Задача №1 и №2
from pprint import pprint

# Функция создания рецепта блюда
def add_cook_book(ingredients):
    dishes = []
    for line in ingredients:
        line = line.strip()
        keys = ['ingredient_name', 'quantity', 'measure']
        ingredient_name, quantity, measure = line.split(" | ")
        # dishes.append(dict(zip(keys, line.split(' | '))))
        dishes.append({keys[0]: ingredient_name,
                    keys[1]: int(quantity),
                    keys[2]: measure})
    return dishes

# Функция создания словаря ингридиентов
def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredients in cook_book[dish]:
                ingredient_name = ingredients['ingredient_name']
                quantity = ingredients['quantity']
                measure = ingredients['measure']
                if ingredient_name not in ingredients_dict:
                    ingredients_dict[ingredient_name] = {'measure': measure,'quantity': int(quantity) * person_count}
                else:
                    ingredients_dict[ingredient_name]['quantity'] += int(quantity) * person_count
        else:
            return f'Ошибка: Блюда {dish} нет в кулинарной книге'
    return ingredients_dict

# Чтение файла с рецептами блюд
with open('recipes.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Запись рецептов в кулинарную книгу
len_lines = len(lines)
index_line = 0
cook_book = {}
while index_line < len_lines:
    line = lines[index_line].strip()
    if line.isdigit():
        name_dish = lines[index_line - 1].strip()
        count_ing = int(line)
        ingredients = lines[index_line + 1 : index_line + count_ing + 1]
        cook_book[name_dish] = add_cook_book(ingredients)
        index_line += count_ing
    else:    
        index_line += 1

# Вывод результата
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))      