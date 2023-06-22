from policyengine_canada.model_api import *


class mb_dependent_grandparents_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba care giver tax credits eligible on household's dependent grandparent"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.caregiver_amount

        age_eligible = person("age", period) >= 65
        dependent_grandparent = person("is_grandparent", period)

        return dependent_grandparent & age_eligible
