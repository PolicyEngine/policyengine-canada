from policyengine_canada.model_api import *


class child_disability_benefit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for Child Disability Benefit"
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/child-family-benefits/child-disability-benefit.html"

    def formula(person, period, parameters):
        dtc_eligible = person("dtc_eligible", period)
        ccb_eligible = person("child_benefit_eligible", period)
        return ccb_eligible & dtc_eligible
