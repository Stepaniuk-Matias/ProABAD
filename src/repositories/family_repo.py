class FamilyRepository:
    def get_family_and_attributes(self):
        from database.queries import select_family_and_atributes
        return select_family_and_atributes()

    def update_family_name(self, id_fam, new_name):
        from database.queries import update_family_name
        return update_family_name(id_fam, new_name)

    def update_attribute_field(self, id_attr, field, new_val):
        from database.queries import update_attribute_field
        return update_attribute_field(id_attr, field, new_val)
