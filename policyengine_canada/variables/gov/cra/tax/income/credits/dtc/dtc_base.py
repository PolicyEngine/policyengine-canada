from policyengine_canada.model_api import *


class dtc_base(Variable):
    value_type = float
    entity = Person
    label = "Disability tax credit base"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.tax.income.credits.dtc
        eligible = person("dtc_eligible", period)
        return p.base * eligible
