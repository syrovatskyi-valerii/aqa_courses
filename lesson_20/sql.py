import sqlite3

try:
    connection = sqlite3.connect('test_homework.db')

    print("DB was created!")

    cursor = connection.cursor()
    # create categories table
    cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")
    # create products table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    ''')

    categories = [
        ('electronics',),
        ('clothes',),
        ('books',)
    ]

    products = [
        ('Iphone', '15 Pro MAX 512GB', 7999.99, 1),
        ('T-shirt', '100% cotton', 299.99, 2),
        ('The Catcher in the Rye', 'A novel by the American writer Jerome Salinger', 199.50, 3),
        ('AirPods', 'TWS', 1299.00, 1),
        ('AppleWatch', 'Fitness tracker 512GB with Wi-Fi', 1599.00, 1),
        ('Jeans', 'Levi Strauss & Co.', 699.00, 2),
    ]

    # add all categories from list 'categories' in categories table
    cursor.executemany('INSERT INTO categories (name) VALUES (?)', categories)

    # add all products from list 'products' in products table
    cursor.executemany('''INSERT INTO products (name, description, price, category_id) VALUES (?, ?, ?, ?)''', products)

    connection.commit()

    # JOIN-request
    cursor.execute('''
    SELECT products.name AS product_name, 
           products.description, 
           products.price, 
           categories.name AS category_name
    FROM products
    JOIN categories ON products.category_id = categories.id
    ''')


    print(cursor.fetchall())


except Exception as error:
    print("Error while connecting to DB", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("DB connection is closed")