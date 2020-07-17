import sqlite3
import psycopg2
from keys.py import elephant_user, elephant_password


dbname = elephant_user
user = elephant_user
password = elephant_password
host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user,
                              password = password, host = host)

pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('rpg_db.sqlite3')

sl_curs = sl_conn.cursor()

get_characters = """
SELECT *
FROM charactercreator_character;
"""

characters = sl_curs.execute(get_characters).fetchall()

create_character_table = """
CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(40),
    level INTEGER,
    exp INTEGER,
    hp INTEGER,
    strength INTEGER,
    intelligence INTEGER,
    dexterity INTEGER,
    wisdom INTEGER
);
"""

pg_curs.execute(create_character_table)

for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)

pg_conn.commit()