from policyengine_canada.model_api import *


class qc_other_income(Variable):
    value_type = float
    entity = Person
    label = "Quebec other income"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/96-to-164-total-income/line-154/"
    defined_for = ProvinceCode.QC
