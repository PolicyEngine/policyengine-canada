from policyengine_canada.model_api import *


class nt_living_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Max for living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.living_tax_credit
        income = Person("individual_net_income", period)

        return (
            p.max_amount * (p.income_threshold <= income)
        )

#max_(x, y)

# x = 934 

# y = lower + middle + higher 

# TODO: add folder credits tax/income/credits/living_tax_credit