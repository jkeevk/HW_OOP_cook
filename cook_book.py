from pprint import pprint

def read_file(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish = line.strip()
            count = int(f.readline())
            ingredients = []
            for _ in range(count):
                ingrs = {}
                ingr_line = f.readline().strip().split(' | ')
                ingrs['ingredient_name'] = ingr_line[0]
                ingrs['quantity'] = int(ingr_line[1])
                ingrs['measure'] = ingr_line[2]
                ingredients.append(ingrs)
            f.readline().strip()
            cook_book[dish] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_file('recipes.txt')
    for dish in dishes:
        for ingridient in cook_book[dish]:
            one_dish_list = dict(ingridient)
            one_dish_list['quantity'] *= person_count
            if one_dish_list['ingredient_name'] not in shop_list:
                shop_list[one_dish_list['ingredient_name']] = one_dish_list
                del one_dish_list['ingredient_name']
            else:
                shop_list[one_dish_list['ingredient_name']]['quantity'] += one_dish_list['quantity']
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 5))
