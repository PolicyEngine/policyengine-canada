from policyengine_canada.model_api import *


class bc_sales_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "British Columbia sales tax credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.BC
    reference = "https://www2.gov.bc.ca/gov/content/taxes/income-taxes/personal/credits/sales-tax"

    def formula(person, period, parameters):
        base = person("bc_sales_tax_credit_base", period)
        reduction = person("bc_sales_tax_credit_reduction", period)
        return max_(0, base - reduction)
