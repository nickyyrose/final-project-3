from models.__init__ import CONN, CURSOR

class Inventory:

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS inventorys (
                id INTEGER PRIMARY KEY,
                store_id INTEGER,
                instrument_id INTEGER,
                stock INTEGER,
                FOREIGN KEY (store_id) REFERENCES stores(id),
                FOREIGN KEY (instrument_id) REFERENCES instruments(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS inventorys;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def __init__(self, store_id, instrument_id, stock, id=None):
        self.id = id
        self.store_id = store_id
        self.instrument_id = instrument_id
        self.stock = stock

    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO inventorys (store_id, instrument_id, stock)
                VALUES (?, ?, ?);
            """
            CURSOR.execute(sql, (self.store_id, self.instrument_id, self.stock))
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE inventorys
                SET store_id = ?, instrument_id = ?, stock = ?
                WHERE id = ?;
            """
            CURSOR.execute(sql, (self.store_id, self.instrument_id, self.stock, self.id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, inventory_id):
        sql = """
            SELECT * FROM inventorys WHERE id = ?;
        """
        CURSOR.execute(sql, (inventory_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], store_id=row[1], instrument_id=row[2], stock=row[3])
        return None

    @classmethod
    def get_all_inventorys(cls):
        sql = """
            SELECT * FROM inventorys;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(id=row[0], store_id=row[1], instrument_id=row[2], stock=row[3]) for row in rows]

    @classmethod
    def create(cls, store_id, instrument_id, stock):
        inventory = cls(store_id, instrument_id, stock)
        inventory.save()
        return inventory

    def update(self):
        sql = """
            UPDATE inventorys
            SET store_id = ?, instrument_id = ?, stock = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.store_id, self.instrument_id, self.stock, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM inventorys WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    def __repr__(self):
        return f"Inventory(id={self.id}, store_id={self.store_id}, instrument_id={self.instrument_id}, stock={self.stock})"
