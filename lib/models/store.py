# models/store.py

from . import CONN, CURSOR

class Store:
    @classmethod
    def create_table(cls):
        sql = """
             CREATE TABLE IF NOT EXISTS stores (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
             );
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS stores;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def save(self):
        if self.id:
            self.update()
        else:
            sql = """
                INSERT INTO stores (name, location)
                VALUES (?, ?);
            """
            CURSOR.execute(sql, (self.name, self.location))
            self.id = CURSOR.lastrowid
            CONN.commit()

    @classmethod
    def find_by_id(cls, store_id):
        sql = """
            SELECT * FROM stores WHERE id = ?;
        """
        CURSOR.execute(sql, (store_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], name=row[1], location=row[2])
        return None

    @classmethod
    def get_all_stores(cls):
        sql = """
            SELECT * FROM stores;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], location=row[2]) for row in rows]
    
    @classmethod
    def create(cls, name, location):
        store = cls(name, location)
        store.save()
        return store

    def update(self):
        sql = """
            UPDATE stores
            SET name = ?, location = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM stores WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    def __repr__(self):
        return f"Store(id={self.id}, name='{self.name}', location='{self.location}')"
