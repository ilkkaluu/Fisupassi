import db

def add_fish(name, species, length, weight):
    sql = "INSERT INTO fish (name, species, length, weight) VALUES (?, ?, ?, ?)"
    db.execute(sql, [name, species, length, weight])
    return db.last_insert_id()

def get_fish_list():
    sql = "SELECT * FROM fish"
    return db.query(sql)