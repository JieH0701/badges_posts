import sqlite3
from toolkit.data_provision import inital_load_posts, inital_load_bagdes


def add_badges(data):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO badges VALUES(?,?,?,?,?,?);", data)
    print('We have inserted', cursor.rowcount, 'records to the table badges.')
    conn.commit()
    conn.close()


def add_posts(data):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.executemany("INSERT OR IGNORE INTO posts VALUES(?,?,?,?,?, ?,?,?,?,?, ?,?,?,?,?,?,?,?);", data)
    print('We have inserted', cursor.rowcount, 'records to the table posts.')
    conn.commit()
    conn.close()


@app.before_first_request
def create_tables():
    db.create_all()
    badges = inital_load_bagdes('data/Badges.xml')
    add_badges(badges)
    posts = inital_load_posts('data/Posts.xml')
    add_posts(posts)
