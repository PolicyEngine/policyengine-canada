from policyengine_canada.model_api import *


class qc_solidarity_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec Solidarity Tax Credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.QC
    reference = "https://www.revenuquebec.ca/en/citizens/tax-credits/solidarity-tax-credit/"

    adds = [
        "qc_solidarity_housing_component",
        "qc_solidarity_qst_component",
    ]
