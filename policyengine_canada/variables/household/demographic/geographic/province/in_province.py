from policyengine_canada.model_api import *


def create_in_province_variable(province: str) -> Type[Variable]:
    return type(
        province,
        (Variable,),
        {
            "definition_period": YEAR,
            "label": f"In {province}",
            "value_type": bool,
            "entity": Household,
            "formula": in_province(province),
            "module_name": "",
            "hidden_input": True,
        },
    )


def create_10_province_variables() -> List[Type[Variable]]:
    return [create_in_province_variable(province) for province in PROVINCES]
