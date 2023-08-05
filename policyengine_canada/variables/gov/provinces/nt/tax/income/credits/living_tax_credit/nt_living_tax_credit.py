from policyengine_canada.model_api import *


class nt_living_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Northwest Territories cost of living tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.NT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.nt.tax.income.credits.living_tax_credit

        net_income = person("individual_net_income", period)

        living_tax_credit = p.reduction.calc(net_income)

        return min_(living_tax_credit, p.max_amount)
