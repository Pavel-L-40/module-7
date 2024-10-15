class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        res = f'{self.name}, {self.weight}, {self.category}'
        return res

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products_shop = file.read()
        file.close()
        return products_shop


    def add(self, *products):
        for product in products:
            if str(product) not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(f'{str(product)}\n')
                file.close()
            else: print(f'продукт {str(product)} уже есть в магазине')

# ================ Test =================================

# перед проверкой работы кода необходимо создать файл products.txt в той же директории что и запускаемый файл

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # str

s1.add(p1, p2, p3)

print('\nсписок продуктов магазина: ')
print(s1.get_products())