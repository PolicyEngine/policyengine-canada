from policyengine_canada.model_api import *


class basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Basic Personal Amount"
    unit = CAD
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.tax.income.credits.basic_personal_amount
        supplement = person("basic_personal_amount_supplement", period)
        return p.base + supplement
