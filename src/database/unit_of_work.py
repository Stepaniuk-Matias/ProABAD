class UnitOfWork:
    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()

# Esto se usa asi:
# with UnitOfWork(conn) as cur:
#     cur.execute("INSERT INTO familias (nombre) VALUES (%s)", ("Nueva familia",))
