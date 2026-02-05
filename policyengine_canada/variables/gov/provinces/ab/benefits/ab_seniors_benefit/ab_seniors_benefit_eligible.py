from policyengine_canada.model_api import *


class ab_seniors_benefit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Alberta Seniors Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period, parameters):
        # Must be 65 or older
        age = person("age", period)

        # Must be receiving Old Age Security
        receives_oas = person("oas_net", period) > 0

        return (age >= 65) & receives_oas
