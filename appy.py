from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)
# Подключение к базе
connection = sqlite3.connect('my_database.db', check_same_thread=False)
cursor = connection.cursor()

def product_oneDB(id):
    listDB=cursor.execute('SELECT * FROM product where id='+id)
    return listDB.fetchall()

def product_twoDB(id):
    listDB=cursor.execute('SELECT * FROM product where id='+id)
    return listDB.fetchall()

# Функция для получения товаров определённой категории
def productDB(category):
    cursor.execute("SELECT * FROM product WHERE category=?", (category,))
    return cursor.fetchall()

# Функция для главной (главная + новинки/тишки/худи по имени)
def productDB_main():
    cursor.execute("""
        SELECT * FROM product
        WHERE category='главная'
           OR name LIKE '%новинки%'
           OR name LIKE '%тишка%'
           OR name LIKE '%худи%'
    """)
    return cursor.fetchall()

# Главная страница
@app.route('/')
def index():
    shop = productDB_main()
    return render_template("index.html", shop=shop)

# Каталог (все товары)
@app.route('/catalog')
def catalog():
    cursor.execute("SELECT * FROM product")
    shop = cursor.fetchall()
    return render_template("catalog.html", shop=shop)

# Футболки
@app.route('/T-shorts')
def Tshirts():
    shop = productDB("футболка")
    return render_template("T-short.html", shop=shop)

# Худи
@app.route('/hoodie')
def hoodie():
    shop = productDB("худи")
    return render_template("hoodie.html", shop=shop)

# Аксессуары
@app.route('/accessories')
def accessories():
    shop = productDB("аксессуар")
    return render_template("accessories.html", shop=shop)

#корзина
@app.route("/basket/<item>" )
def basket(item):
    shop= product_twoDB(item)
    print(shop)
    return render_template('basket.html', shop=shop)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("q")  # .
    shop = []

    if query:
        cursor.execute("SELECT * FROM product WHERE name LIKE ? OR category LIKE ?", (f"%{query}%", f"%{query}%"))
        shop = cursor.fetchall()

    return render_template("search.html", shop=shop, query=query)




if __name__ == '__main__':
    app.run(debug=True)