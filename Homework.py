from pprint import pprint
import file_options


class CookRecipe:
    def __init__(self):
        with open('recipes.txt', encoding='utf-8') as f:
            self.cook_book = {}
            for line in f:
                dish = line.strip()
                num = int(f.readline())
                i = 0
                ingredients = []
                while i < num:
                    i += 1
                    ingredient_str = f.readline().strip()
                    row = {
                        'ingredient_name': ingredient_str[0: ingredient_str.find(' | ')],
                        'quantity': int(ingredient_str[ingredient_str.find(' | ') + 3: ingredient_str.rfind(' | ')]),
                        'measure': ingredient_str[ingredient_str.rfind(' | ') + 3:]
                    }
                    ingredients.append(row)
                self.cook_book[dish] = ingredients
                f.readline()

    def cook_book_view(self):
        pprint(self.cook_book)

    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {}
        for dish in dishes:
            if dish in self.cook_book:
                for row in self.cook_book[dish]:
                    if shop_list.get('ingredient_name') is None:
                        shop_list[row['ingredient_name']] = {'measure': row['measure'],
                                                             'quantity': row['quantity'] * person_count}
                    else:
                        shop_list['ingredient_name']['quantity'] += row['quantity'] * person_count
            else:
                print(f"Рецепт {dish} в вашей книге рецептов не обнаружен")
        return shop_list


if __name__ == '__main__':
    cook_session = CookRecipe()
    sl = cook_session.get_shop_list_by_dishes(['Утка по-пекински', 'Запеченый картофель', 'Фахитос', 'Омлет'], 4)
    pprint(sl)
    file_options.txt_file_steaching()


