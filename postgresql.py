import psycopg2


dbname = 'vvqfwreu'
user = 'vvqfwreu'
password = 'x2V1_pasp_QsYLoNKDjsAUyUyRV1WDui'
host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user,
                              password = password, host = host)

pg_curs = pg_conn.cursor()

create_table_statement = """
CREATE TABLE test_table (
    Id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
);
"""

pg_curs.execute(create_table_statement)
pg_conn.commit()

insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
    'A row name',
    null
),
(
    'Another row, with JSON this time',
    '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB
)
"""

pg_curs.execute(insert_statement)
pg_conn.commit()