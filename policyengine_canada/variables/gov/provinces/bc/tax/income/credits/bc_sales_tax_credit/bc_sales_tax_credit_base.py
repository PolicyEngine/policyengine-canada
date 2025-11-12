from policyengine_canada.model_api import *


class bc_sales_tax_credit_base(Variable):
    value_type = float
    entity = Person
    label = "British Columbia sales tax credit base"
    unit = CAD
    documentation = "Base amount of BC sales tax credit before reduction"
    definition_period = YEAR
    defined_for = ProvinceCode.BC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.sales_tax_credit
        # Each person gets the base amount ($75 in 2024)
        # Only the individual and their spouse/common-law partner are eligible
        household = person.household
        is_adult = person("age", period) >= 18
        return where(is_adult, p.amount, 0)
