from policyengine_canada.model_api import *


class nb_pension_benefit(Variable):
    value_type = float
    entity = Person
    label = "New Brunswick pension benefit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(person, period, parameters):
        age = person("age", period)
        pension_income = person("pension_and_savings_plan_income", period)
        max_amount = parameters(
            period
        ).gov.provinces.nb.benefits.pension_benefit.cap
        # Capped at a certain amount
        return min_(max_amount, pension_income)
