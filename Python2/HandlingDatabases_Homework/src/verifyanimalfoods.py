import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor() 
cursor.execute("SELECT id, name, family FROM animal")
animals = cursor.fetchall()

for animal in animals:
    id = animal[0]
    name = animal[1]
    family = animal[2]
    cursor.execute("SELECT COUNT(*) FROM food WHERE anid={0}".format(id))
    count = cursor.fetchone()[0]
    
    if count == 0:
        print("{0} the {1} doesn't have food (id {2})".format(name, family, id))
    else:
        print("{0} the {1} has food (id {2})".format(name, family, id))