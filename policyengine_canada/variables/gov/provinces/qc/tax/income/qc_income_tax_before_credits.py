from policyengine_canada.model_api import *


class qc_income_tax_before_credits(Variable):
    value_type = float
    entity = Person
    label = "Quebec income tax"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/income-tax-rates/"
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        income = person("qc_taxable_income", period)
        p = parameters(period).gov.provinces.qc.tax.income.rate
        return p.calc(income)
