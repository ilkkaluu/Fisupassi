import db

def add_fish(user_id, fish_name, weight):
    sql = "INSERT INTO fish (user_id, fish_name, weight) VALUES (?, ?, ?)"
    db.execute(sql, [user_id, fish_name, weight])
    return db.last_insert_id()

def get_fish_list():
    sql = "SELECT * FROM fish"
    return db.query(sql)