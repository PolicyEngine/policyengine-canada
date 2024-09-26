from policyengine_canada.model_api import *


class qc_credit_transferred_by_spouse(Variable):
    value_type = float
    entity = Person
    label = "Quebec credits transferred from one spouse to the other"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/400-to-447-income-tax-and-contributions/line-431/"
    defined_for = ProvinceCode.QC
