from policyengine_canada.model_api import *


class annual_taxable_income(Variable):
    value_type = float
    entity = Household
    label = "Household Annual Taxable Income"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.SK