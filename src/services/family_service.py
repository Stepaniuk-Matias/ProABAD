class FamilyService:
    def __init__(self, repository):
        self.repo = repository

    def load_tree_data(self):
        rows = self.repo.get_family_and_attributes()
        # Aquí solo devuelves datos crudos o un objeto de dominio
        return rows

    def update_attribute(self, id_attr, field, new_val):
        self.repo.update_attribute_field(id_attr, field, new_val)

    def update_family(self, id_fam, new_name):
        self.repo.update_family_name(id_fam, new_name)
