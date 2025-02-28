
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

# Создание объектов класса Store
store1 = Store("Green Grocer", "123 Main St")
store2 = Store("Tech Hub", "456 Tech Ave")
store3 = Store("Fashion Fiesta", "789 Fashion Blvd")

# Добавление товаров в каждый магазин
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("laptop", 999.99)
store2.add_item("headphones", 199.99)

store3.add_item("jeans", 49.99)
store3.add_item("t-shirt", 19.99)

# Тестирование методов для одного из магазинов
# Выберем магазин store1 для тестирования
print("--- Тестирование методов для магазина store1 ---")

# Добавление товара
store1.add_item("oranges", 0.65)
print("После добавления апельсинов:", store1.items)

# Обновление цены товара
store1.update_price("apples", 0.55)
print("После обновления цены на яблоки:", store1.items)

# Удаление товара
store1.remove_item("bananas")
print("После удаления бананов:", store1.items)

# Получение цены товара
apple_price = store1.get_price("apples")
print("Цена на яблоки:", apple_price)

# Попытка получить цену несуществующего товара
grape_price = store1.get_price("grapes")
print("Цена на виноград:", grape_price)