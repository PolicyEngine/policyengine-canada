from policyengine_canada.model_api import *


class ns_low_income_tax_reduction_eligible_children(Variable):
    value_type = int
    entity = Household
    label = "Nova Scotia low income tax reduction eligible children"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    adds = ["ns_low_income_tax_reduction_eligible_child"]
