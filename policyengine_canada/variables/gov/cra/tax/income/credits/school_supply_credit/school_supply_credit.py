from policyengine_canada.model_api import *


class school_supply_credit(Variable):
    value_type = float
    entity = Person
    label = "School supply credit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        expenses = person("teaching_supplies_expenses", period)
        p = parameters(period).gov.cra.tax.income.credits.school_supply_credit
        rate = p.amount
        cap = p.cap
        return min_(expenses * rate, cap)
