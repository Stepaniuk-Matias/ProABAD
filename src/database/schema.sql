CREATE TABLE Familia (
    id_familia INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);
CREATE TABLE Atributo (
    id_atributo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_familia INTEGER NOT NULL,
    nombre_atributo TEXT NOT NULL,
    tipo_dato TEXT NOT NULL,
    obligatorio INTEGER DEFAULT 0, -- 0 = false, 1 = true
    orden SMALLINT NOT NULL,
    FOREIGN KEY (id_familia) REFERENCES Familia(id_familia)
);
CREATE TABLE AtributoOpcion (
    id_opcion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_atributo INTEGER,
    valor TEXT NOT NULL,
    orden SMALLINT,
    FOREIGN KEY (id_atributo) REFERENCES Atributo(id_atributo)
);