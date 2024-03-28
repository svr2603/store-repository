#Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.
#Шаги:
#1. Создай класс Store:
#-Атрибуты класса:
#name: название магазина.
#address: адрес магазина.
#items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
#Методы класса:
#__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
#-  метод для добавления товара в ассортимент.
#метод для удаления товара из ассортимента.
#метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
#метод для обновления цены товара.


class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
    def add_goods_assortment(self, items_name, price):
        return self.items.update({items_name : price})

    def delete_goods(self, items_name):
        return self.items.pop(items_name)

    def get_price_product(self, items_name):
        return self.items.get(items_name, None)



    def update_price(self, items_name, price):
        if items_name in self.items:
            self.items[items_name] = price
        else:
            print(f"Товар {items_name} не найден")

# Создай несколько объектов класса Store:
#Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#3. Протестировать методы:
#Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
#В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

store1 = Store('Пятерочка', 'ул. Ленина, 16')
store2 = Store('Перекресток', 'ул. Советская , 16')
store3 = Store('Карусель', 'ул. Профсоюзная')

store1.add_goods_assortment('хлеб', '25')
store1.add_goods_assortment('молоко', '85')
store1.add_goods_assortment('шоколад', '100')
print(store1.items)
store1.update_price('молоко', '92')
print(f"Новая цена молока {store1.get_price_product('молоко')}")
print(store1.items)
store1.delete_goods('хлеб')
print(store1.items)
store1.get_price_product('молоко')
print(f"Цена 1 пакета молока: {store1.get_price_product('молоко')} руб.")