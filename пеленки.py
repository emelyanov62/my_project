import sqlite3

# Создаем базу данных и таблицу для товаров
conn = sqlite3.connect('my_store.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        price REAL,
        quantity INTEGER,
        image BLOB
    )
''')

conn.commit()

def add_product(name, description, price, quantity, image_path):
    # Загрузка изображения из файла
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Добавляем товар в базу данных
    cursor.execute('INSERT INTO products (name, description, price, quantity, image) VALUES (?, ?, ?, ?, ?)',
                   (name, description, price, quantity, image_data))

    conn.commit()

def update_product_quantity(product_id, new_quantity):
    # Обновляем количество товара в базе данных
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    conn.commit()

# Пример добавления товара
add_product('пеленка', 'пеленка мишка', 19.99, 100, 'C:\\Users\\User\\Desktop\\photo.jpg')

# Пример обновления количества товара
#update_product_quantity(1, 150)

# Закрываем соединение с базой данных
conn.close()


# Создаем соединение с базой данных
conn = sqlite3.connect('my_store.db')
cursor = conn.cursor()

# Выполняем SQL-запрос для извлечения данных
cursor.execute('SELECT * FROM products')  # Извлекаем данные о товарах

# Получаем результаты запроса
products = cursor.fetchall()

# Закрываем соединение
conn.close()

# Теперь у вас есть список товаров, и каждый товар представлен в виде кортежа
# с полями, соответствующими столбцам таблицы
for product in products:
    print(product)
