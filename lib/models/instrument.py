from models.__init__ import CONN, CURSOR

class Instrument:

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS instruments (
                id INTEGER PRIMARY KEY,
                type TEXT,
                model TEXT,
                price INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS instruments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def __init__(self, type, model, price, id=None):
        self.id = id
        self.type = type
        self.model = model
        self.price = price

    def save(self):
        if self.id is None:
            sql = """
                INSERT INTO instruments (type, model, price)
                VALUES (?, ?, ?);
            """
            CURSOR.execute(sql, (self.type, self.model, self.price))
            self.id = CURSOR.lastrowid
        else:
            sql = """
                UPDATE instruments
                SET type = ?, model = ?, price = ?
                WHERE id = ?;
            """
            CURSOR.execute(sql, (self.type, self.model, self.price, self.id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, instrument_id):
        sql = """
            SELECT * FROM instruments WHERE id = ?;
        """
        CURSOR.execute(sql, (instrument_id,))
        row = CURSOR.fetchone()
        if row:
            return cls(id=row[0], type=row[1], model=row[2], price=row[3])
        return None

    @classmethod
    def get_all_instruments(cls):
        sql = """
            SELECT * FROM instruments;
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls(id=row[0], type=row[1], model=row[2], price=row[3]) for row in rows]

    @classmethod
    def create(cls, type, model, price):
        instrument = cls(type, model, price)
        instrument.save()
        return instrument

    def update(self):
        sql = """
            UPDATE instruments
            SET type = ?, model = ?, price = ?
            WHERE id = ?;
        """
        CURSOR.execute(sql, (self.type, self.model, self.price, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM instruments WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        self.id = None

    def __repr__(self):
        return f"Instrument(id={self.id}, type='{self.type}', model='{self.model}', price={self.price})"