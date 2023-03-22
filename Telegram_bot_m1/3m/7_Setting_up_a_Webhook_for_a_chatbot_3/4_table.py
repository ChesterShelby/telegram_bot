"""
После создания нового файла базы данных следующим шагом является создание схемы для определения таблиц в базе данных.
"""
import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'
db_is_new = not os.path.exists(db_filename)
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        print('Inserting initial data')
        conn.executescript("""
       insert into project (name, description, deadline)
       values ('pymotw', 'Python Module of the Week',
       '2022-11-01');
       insert into task (details, status, deadline, project, completed_on)
       values ('write about select', 'done', '2022-04-25',
       'pymotw', '2022-04-25');
       insert into task (details, status, deadline, project, completed_on)
       values ('write about random', 'waiting', '2022—08—22',
       'pymotw', '2022—08—22');
       insert into task (details, status, deadline, project, completed_on)
       values ('write about sqlite3', 'active', '2021—07—31',
       'pymotw', '2021—07—31');
       """)
    else:
        print('Database exists, assume schema does, too.')
