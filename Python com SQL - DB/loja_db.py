CREATE TABLE pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        produto TEXT,
        valor REAL,
        data TEXT,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    );
