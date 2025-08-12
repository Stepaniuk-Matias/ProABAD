-- TABLE
CREATE TABLE Atributos (
    id_atributo INTEGER PRIMARY KEY AUTOINCREMENT,
    id_familia INTEGER NOT NULL,
    nombre_atributo TEXT NOT NULL,
    tipo_dato TEXT NOT NULL CHECK (tipo_dato IN ('int', 'float', 'bool', 'list')),
    unidad TEXT,
    obligatorio BOOLEAN DEFAULT 1,
    orden INTEGER NOT NULL,
    UNIQUE (id_familia, nombre_atributo),
    FOREIGN KEY (id_familia) REFERENCES Familia(id_familia)
);
CREATE TABLE Familias (
    id_familia INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL
);
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
