from policyengine_canada.model_api import *


class ab_age_credit(Variable):
    value_type = float
    entity = Person
    label = "Alberta age benefit"
    definition_period = YEAR
    defined_for = "ab_age_credit_eligible"

    def formula(person, period, parameters):
        income = person("individual_net_income", period)
        p = parameters(period).gov.provinces.ab.tax.income.credits.age_credit
        return max_(p.base - p.phase_out_rate.calc(income), 0)
