from models.schema_familia import Familia, Atributo

class FamilyMapper:
    @staticmethod
    def map_rows_to_objects(rows):
        familias_dict = {}

        for r in rows:
            id_fam, nombre_fam, id_attr, nom_attr, tipo, unidad, obligatorio, orden, opciones = r

            if id_fam not in familias_dict:
                familias_dict[id_fam] = Familia(
                    id_familia=id_fam,
                    nombre=nombre_fam,
                    atributos=[]
                )

            if id_attr:
                atributo = Atributo(
                    id_atributo=id_attr,
                    id_familia=id_fam,
                    nombre=nom_attr,
                    tipo=tipo,
                    unidad=unidad,
                    es_obligatorio=obligatorio,
                    orden=orden,
                    opciones=opciones or []
                )
                familias_dict[id_fam].atributos.append(atributo)

        return list(familias_dict.values())
