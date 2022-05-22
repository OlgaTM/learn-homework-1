"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

phone_sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
 
def count_sales_sum(product_sales):
  one_product_sales_sum = 0
  for sales in product_sales:
    one_product_sales_sum += sales
  return one_product_sales_sum

def count_sales_avg(product_sales):
  one_product_sales_sum = 0
  for sales in product_sales:
    one_product_sales_sum += sales
  return one_product_sales_sum / len(product_sales)

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

all_products_sales_sum = 0
for one_phone_sales in phone_sales:
  sales_sum = count_sales_sum(one_phone_sales['items_sold'])
  print(f'Общая сумма продаж {one_phone_sales["product"]} - {sales_sum}')
  all_products_sales_sum += sales_sum

sum_all_products_sales_avg = 0
for one_phone_sales in phone_sales:
  sales_avg = int(count_sales_avg(one_phone_sales['items_sold']))
  print(f'Среднее количество продаж {one_phone_sales["product"]} - {sales_avg}')
  sum_all_products_sales_avg += sales_avg

all_products_sales_avg = int(sum_all_products_sales_avg / len(phone_sales))

print(f'Общаяя сумма продаж {all_products_sales_sum}')
print(f'Общаее среднее количество продаж {all_products_sales_avg}')

if __name__ == "__main__":
    main()
