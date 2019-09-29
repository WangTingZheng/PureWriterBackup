import sqlite3

conn = sqlite3.connect("../res/test.db")
cursor = conn.cursor()


def get_folder(id):
    sql = "select *from Folder where id='%s'" % id
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def get_article(find_type, value):
    if find_type == "id":
        sql = "select *from Article where id='%s'" % value
    elif find_type == "title":
        sql = "select *from Article where title='%s'" % value
    elif find_type == "extension":
        sql = "select *from Article where extension='%s'" % value
    elif find_type == "folderId":
        sql = "select *from Article where folderId='%s'" % value
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

print(get_article("title","如你所愿"))