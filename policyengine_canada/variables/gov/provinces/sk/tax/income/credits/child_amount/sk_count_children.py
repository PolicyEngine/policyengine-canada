from policyengine_canada.model_api import *


class sk_count_children(Variable):
    value_type = int
    entity = Household
    label = "Children"
    unit = CAD
    documentation = "Number of dependant children under the age of 18"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.tax.income.credits.child_amount
        person = household.members
        age_eligible = person("age", period) < p.age_eligibility
        child = person("is_child", period)
        return household.sum(age_eligible & child)
