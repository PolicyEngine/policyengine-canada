from policyengine_canada.model_api import *


class mb_tuition_amount_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Manitoba tuition amount credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.tuition_amount

        tuition = person("tuition_expenses", period)
        tuition_eligible = tuition > p.tuition_threshold

        return tuition_eligible
