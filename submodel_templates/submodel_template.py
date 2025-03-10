import aas_core3.types as aas_types


class SubmodelTemplate(aas_types.Submodel):
    @classmethod
    def get_id_short(cls) -> str:
        """Static variable that must be defined in subclasses"""
        raise NotImplementedError("Subclasses must implement get_id_short()")

    @classmethod
    def get_html_from_submodel(cls, submodel: aas_types.Submodel) -> str:
        """Static html generation can be created by each submodel"""
        return ""

    def __init__(self, new_id: str):
        super().__init__(id=new_id, id_short=self.get_id_short())

    @classmethod
    def get_submodel_from_env(cls, env: aas_types.Environment):
        for submodel in env.submodels:
            if submodel.id_short == cls.get_id_short():
                return submodel
        return None
