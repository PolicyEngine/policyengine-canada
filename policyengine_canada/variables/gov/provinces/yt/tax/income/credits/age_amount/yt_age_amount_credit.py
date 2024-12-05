from policyengine_canada.model_api import *


class yt_age_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Yukon age amount credit"
    definition_period = YEAR
    defined_for = "yt_age_amount_credit_eligible_person"

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        p = parameters(period).gov.provinces.yt.tax.income.credits.age_amount
        base = p.base
        reduction = p.reduction.calc(income)
        return max_(base - reduction, 0)
