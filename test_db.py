import os
import pytest
import psycopg2


@pytest.fixture(scope="module")
def db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "test_db"),
        user=os.getenv("POSTGRES_USER", "test_user"),
        password=os.getenv("POSTGRES_PASSWORD", "test_password"),
        host=os.getenv("HOST", "localhost"),
        port=os.getenv("PORT", 5432)
    )
    yield conn
    conn.close()


@pytest.fixture(scope="module")
def setup_table(db_connection):
    with db_connection.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        db_connection.commit()
    yield

    with db_connection.cursor() as cur:
        cur.execute("DROP TABLE IF EXISTS users")
        db_connection.commit()


def test_connection(db_connection):
    assert db_connection is not None


def test_insert_user(db_connection, setup_table):
    with db_connection.cursor() as cur:
        cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id", ("Alice",))
        user_id = cur.fetchone()[0]
        db_connection.commit()
    assert user_id is not None


def test_update_user(db_connection, setup_table):
    with db_connection.cursor() as cur:

        cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id", ("Bob",))
        user_id = cur.fetchone()[0]
        db_connection.commit()


        cur.execute("UPDATE users SET name = %s WHERE id = %s", ("Bobby", user_id))
        db_connection.commit()


        cur.execute("SELECT name FROM users WHERE id = %s", (user_id,))
        name = cur.fetchone()[0]

    assert name == "Bobby"


def test_delete_user(db_connection, setup_table):
    with db_connection.cursor() as cur:

        cur.execute("INSERT INTO users (name) VALUES (%s) RETURNING id", ("Charlie",))
        user_id = cur.fetchone()[0]
        db_connection.commit()


        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        db_connection.commit()


        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        result = cur.fetchone()

    assert result is None


def test_select_users(db_connection, setup_table):
    with db_connection.cursor() as cur:

        cur.execute("DELETE FROM users")
        db_connection.commit()


        users = [("Dave",), ("Eve",), ("Frank",)]
        cur.executemany("INSERT INTO users (name) VALUES (%s)", users)
        db_connection.commit()


        cur.execute("SELECT name FROM users ORDER BY id")
        results = cur.fetchall()

    names = [row[0] for row in results]
    assert names == ["Dave", "Eve", "Frank"]
