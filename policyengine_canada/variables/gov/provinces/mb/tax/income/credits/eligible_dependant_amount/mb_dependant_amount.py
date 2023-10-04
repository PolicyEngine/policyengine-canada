from policyengine_canada.model_api import *


class mb_dependant_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba eligible dependant amount credit"
    definition_period = YEAR
    defined_for = "mb_dependant_amount_eligibility"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.eligible_dependant_amount

        credit = p.max_amount - person("dependant_income", period)

        return credit
