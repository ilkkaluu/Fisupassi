import sqlite3
from flask import g

def get_connection():
    con = sqlite3.connect("database.db")
    con.execute("PRAGMA foreign_keys = ON")
    con.row_factory = sqlite3.Row
    return con

def execute(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params)
    con.commit()
    g.last_insert_id = result.lastrowid
    con.close()

def last_insert_id():
    return g.last_insert_id

def query(sql, params=[]):
    con = get_connection()
    result = con.execute(sql, params).fetchall()
    con.close()
    return result

def add_fish(user_id, fish_name, weight):
    sql = "INSERT INTO fish (user_id, fish_name, weight) VALUES (?, ?, ?)"
    execute(sql, [user_id, fish_name, weight])

def remove_fish(id):
    sql = "DELETE FROM fish WHERE id = ?"
    execute(sql, [id])

def get_user_fish(user_id):
    sql = "SELECT id, fish_name, weight FROM fish WHERE user_id = ?"
    return query(sql, [user_id])