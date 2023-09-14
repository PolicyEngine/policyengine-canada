from policyengine_canada.model_api import *


class ab_disability_tax_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Alberta disability tax credit eligbility"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(person, period):
        return person("is_disabled", period)
