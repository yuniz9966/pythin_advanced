# Задание 1. Наполнение данными
# Добавьте в базу данных категории и продукты.
# 1. Добавление категорий: Добавьте в таблицу categories следующие категории:
# ○ Название: "Электроника", Описание: "Гаджеты и устройства."
# ○ Название: "Книги", Описание: "Печатные книги и электронные книги."
# ○ Название: "Одежда", Описание: "Одежда для мужчин и женщин."

# 2. Добавление продуктов: Добавьте в таблицу products следующие продукты, убедившись, что каждый
# продукт связан с соответствующей категорией:
# ○ Название: "Смартфон", Цена: 299.99, Наличие на складе: True, Категория: Электроника
# ○ Название: "Ноутбук", Цена: 499.99, Наличие на складе: True, Категория: Электроника
# ○ Название: "Научно-фантастический роман", Цена: 15.99, Наличие на складе: True, Категория: Книги
# ○ Название: "Джинсы", Цена: 40.50, Наличие на складе: True, Категория: Одежда
# ○ Название: "Футболка", Цена: 20.00, Наличие на складе: True, Категория: Одежда


from SQLAlchemy_lesson.practice.hw4.hw4_models import User, Order, Category, Product
from SQLAlchemy_lesson.practice.hw4.db_connection import engine, Base, session
from datetime import datetime, timedelta
from sqlalchemy import func

Base.metadata.create_all(engine)

# Добавление пользователей
user1 = User(name="Alice", age=30)
user2 = User(name="Bob", age=22)

session.add_all([user1, user2])
session.commit()


# Добавление заказов
order1 = Order(user_id=user1.id, amount=100.50, created_at=datetime.now() - timedelta(days=1))
order2 = Order(user_id=user1.id, amount=200.75, created_at=datetime.now())
order3 = Order(user_id=user2.id, amount=80.99, created_at=datetime.now() - timedelta(days=2))

session.add_all([order1, order2, order3])
session.commit()


# Добавление категорий
category_electronics = Category(name="Электроника", description="Гаджеты и устройства.")
category_books = Category(name="Книги", description="Печатные книги и электронные книги.")
category_clothing = Category(name="Одежда", description="Одежда для мужчин и женщин.")

session.add_all([category_electronics, category_books, category_clothing])
session.commit()


# Добавление продуктов
product_smartphone = Product(name="Смартфон", price=299.99, in_stock=True, category_id=category_electronics.id)
product_laptop = Product(name="Ноутбук", price=499.99, in_stock=True, category_id=category_electronics.id)
product_book = Product(name="Научно-фантастический роман", price=15.99, in_stock=True, category_id=category_books.id)
product_jeans = Product(name="Джинсы", price=40.50, in_stock=True, category_id=category_clothing.id)
product_tshirt = Product(name="Футболка", price=20.00, in_stock=True, category_id=category_clothing.id)

session.add_all([product_smartphone, product_laptop, product_book, product_jeans, product_tshirt])
session.commit()


# Задание 2. Чтение данных
# Извлеките все записи из таблицы categories. Для каждой категории извлеките и выведите все связанные с
# ней продукты, включая их названия и цены.

categories = (session.query(
    Category.name,
    Product.name.label('product_name'),
    Product.price.label('product_price')
)
              .join(Product, Product.category_id == Category.id)
              .all())

for elem in categories:
    print(f"Category: {elem.name}, Product_name: {elem.product_name}, Price: {elem.product_price}")


# Задание 3. Обновление данных
# Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на
# 349.99.

product = session.query(Product).filter(Product.name == "Смартфон").first()

if product:
    product.price = 349.99
    session.commit()
    print("Цена обновлена.")
else:
    print("Продукт 'Смартфон' не найден.")

# ЛИБО
# session.execute(update(Product).where(Product.name == "Смартфон").values(price=349.99))
# session.commit()


# Задание 4. Агрегация и группировка
# Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой
# категории.

category_counts = (
    session.query(Category.name, func.count(Product.id).label("product_count"))
    .join(Product, Product.category_id == Category.id)
    .group_by(Category.name)
    .all()
)

for category_name, product_count in category_counts:
    print(f"Категория: {category_name}, Количество товаров: {product_count}")


# Задание 5. Группировка с фильтрацией
# Отфильтруйте и выведите только те категории, в которых более одного продукта.

filter_category = (
    session.query(Category.name, func.count(Product.id).label("product_count"))
    .join(Product, Product.category_id == Category.id)
    .group_by(Category.name)
    .having(func.count(Product.id) > 1)
    .all()
)

for category_name, product_count in filter_category:
    print(f"Категория: {category_name}, Количество товаров: {product_count}")



session.close()



