from policyengine_canada.model_api import *


class dtc_child_supplement(Variable):
    value_type = float
    entity = Person
    label = "Disability child supplement"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.tax.income.credits.dtc
        eligible = person("dtc_eligible", period)
        supplement_eligible = (
            person("age", period) < p.supplement_ineligible_age
        ) & eligible
        return p.child_supplement * supplement_eligible
