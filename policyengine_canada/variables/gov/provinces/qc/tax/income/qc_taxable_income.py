from policyengine_canada.model_api import *


class qc_taxable_income(Variable):
    value_type = float
    entity = Person
    label = "Quebec taxable income"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/income-tax-rates/"
    defined_for = ProvinceCode.QC
    adds = ["total_individual_pre_tax_income"]
