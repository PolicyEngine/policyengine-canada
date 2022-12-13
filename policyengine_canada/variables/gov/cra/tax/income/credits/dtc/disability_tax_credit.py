from policyengine_canada.model_api import *


class disability_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Disability tax credit"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.tax.income.credits.dtc
        eligible = person("dtc_eligible", period)
        base_amount = p.base * eligible
        supplement = person("dtc_supplement", period) * eligible
        income_tax = person("income_tax", period)
        return min_((base_amount + supplement), income_tax)
