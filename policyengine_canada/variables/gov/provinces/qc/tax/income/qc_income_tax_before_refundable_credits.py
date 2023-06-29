from policyengine_canada.model_api import *


class qc_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Person
    label = "Quebec income tax before refundable credits"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/income-tax-rates/"
    adds = ["qc_income_tax_before_credits"]
    defined_for = ProvinceCode.QC
