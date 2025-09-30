INSERT INTO opciones_atributos (id_atributo, nombre, orden)
VALUES ()

INSERT INTO atributos (id_familia,nombre_atributo,tipo_dato,unidad,es_obligatorio,orden,opciones_atributos)
VALUES (2, 'Cubo', 'list', 'cantidad', 'True', 3, '{"Saliente", "Deprimido", "Rasante"}');

UPDATE atributos SET opciones_atributos TO 