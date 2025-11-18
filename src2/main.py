from infraestructure.database.connection import create_connection

from domain.familias.entities.familia import Familia
from domain.familias.entities.atributo import Atributo
from domain.familias.value_objects.tipo_dato import TipoDato
from domain.familias.value_objects.unidad import Unidad
from uuid import uuid4

conn = create_connection()

# prueba

f1 = Familia(uuid4, "Familia 1")
f2 = Familia(uuid4, "Familia 2")

atrib = Atributo(uuid4,"diámetro", TipoDato.NUMERO_DECIMAL.value, Unidad("mm"), True, 1)

f1.add_atributo(atrib)

print(f1)
print(f2)
print(atrib)
