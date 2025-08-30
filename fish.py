import db

def add_fish(user_id, fish_name, weight):
    sql = "INSERT INTO fish (user_id, fish_name, weight) VALUES (?, ?, ?)"
    db.execute(sql, [user_id, fish_name, weight])
    return db.last_insert_id()

def get_fish_list():
    sql = "SELECT * FROM fish"
    return db.query(sql)

def get_fish(id):
    sql = "SELECT id, fish_name, weight, user_id FROM fish WHERE id = ?"
    result = db.query(sql, [id])
    return result[0] if result else None

def add_fish(user_id, fish_name, weight):
    sql = "INSERT INTO fish (user_id, fish_name, weight) VALUES (?, ?, ?)"
    db.execute(sql, [user_id, fish_name, weight])

def edit_fish(id, fish_name, weight):
    sql = "UPDATE fish SET fish_name = ?, weight = ? WHERE id = ?"
    db.execute(sql, [fish_name, weight, id])

def remove_fish(id):
    sql = "DELETE FROM fish WHERE id = ?"
    db.execute(sql, [id])

def get_user_fish(user_id):
    sql = "SELECT id, fish_name, weight FROM fish WHERE user_id = ?"
    return db.query(sql, [user_id])