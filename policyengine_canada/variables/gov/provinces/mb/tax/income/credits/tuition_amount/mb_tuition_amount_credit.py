from policyengine_canada.model_api import *

class mb_tuition_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba tuition amount credit"
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.mb.tax.income.credits.tuition_amount

        tuition = person("tuition_expenses", period)
        tuition_eligible = tuition > p.eligible_tuition_amount

        # check if full-time student
        full_time = person("is_full_time_student", period)
        part_time = ~full_time

        # check if disabled
        disabled = person("is_disabled", period)
        nondisabled = ~disabled

        return tuition_eligible * (tuition + full_time * p.full_time_students + part_time * nondisabled * p.part_time_students + part_time * disabled * p.part_time_disabled)
