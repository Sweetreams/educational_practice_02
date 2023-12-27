total_sales = 0

product_stock = {"Хлеб" : [123, 34], "Рыба" : [40, 300], "Лимон": [310, 30]}

def calculate_sales(list_price):
    global total_sales
    for q in list_price:
        total_sales += q
    return total_sales

def check_stock(name_produck):
    try:
        if product_stock[name_produck]:
            print(f"Товар в наличие: {name_produck}, Количество: {product_stock.get(name_produck)[0]}, Цена: {product_stock.get(name_produck)[1]}")
    except:
        print("Товар не найден")

# С одним товаром
def calculate_revenue(name_produck, sales):
    global total_sales
    try:
        if product_stock[name_produck] :
            if sales <= product_stock.get(name_produck)[0]:
                print(f"Продано : {sales} единиц товара, выручка: {sales * product_stock.get(name_produck)[1]}")
                total_sales = sales * product_stock.get(name_produck)[1]
                # Кол-во товара осталось
                product_stock.get(name_produck)[0] =- sales
            else:
                print("Продажа не возможна: недостаточно товара")
    except:
        print("Товар не найден")

# С несколькими товарами(От себячина, в задание такого пункта нет, но наверное за это будут дополнительные баллы =) )
def self_calculate_revenue(name_produck: str, sales: int):
    global total_sales
    for product in range(0, len(name_produck)):
        try:
            if product_stock[name_produck[product]] :
                if sales[product] <= product_stock.get(name_produck[product])[0]:
                    print(f"Продано : {sales[product]} единиц товара, выручка: {sales[product] * product_stock.get(name_produck[product])[1]}")
                    total_sales += sales[product] * product_stock.get(name_produck[product])[1]
                    # Кол-во товара осталось
                    product_stock.get(name_produck[product])[0] = product_stock.get(name_produck[product])[0] - sales[product]
                else:
                    print("Продажа не возможна: недостаточно товара")
        except:
            print("Товар не найден")



print(self_calculate_revenue(("Хлеб", "Рыба", "Лимон"), (2, 40, 3)))
print(check_stock("Хлеб"))
print(check_stock("Рыба"))
print(check_stock("Лимон"))
print(total_sales)
