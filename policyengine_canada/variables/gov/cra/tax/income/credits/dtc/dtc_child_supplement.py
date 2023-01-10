from policyengine_canada.model_api import *


class dtc_child_supplement(Variable):
    value_type = float
    entity = Person
    label = "Disability child supplement"
    unit = CAD
    definition_period = YEAR
    defined_for = "dtc_eligible"

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.tax.income.credits.dtc
        supplement_eligible = (
            person("age", period) < p.supplement_ineligible_age
        )
        return p.child_supplement * supplement_eligible
