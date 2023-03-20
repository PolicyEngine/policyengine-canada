from policyengine_canada.model_api import *


class nu_cost_of_living_credit_post_supplement(Variable):
    value_type = float
    entity = Person
    label = "Nunavut cost of living credit post supplement"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.NU

    def formula(person, period, parameters):
        credit = person("nu_cost_of_living_credit", period)
        supplement = person("nu_cost_of_living_credit_supplement", period)
        return credit + supplement
