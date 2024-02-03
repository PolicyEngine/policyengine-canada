from policyengine_canada.model_api import *


class mb_tuition_amount_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba tuition amount credit"
    definition_period = YEAR
    defined_for = "mb_tuition_amount_credit_eligible"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.tuition_amount

        tuition = person("tuition_expenses", period)

        # check if full-time or disabled student
        full_time_student = person("is_full_time_student", period)

        disabled_student = person("is_disabled", period)

        full_time_or_disabled_student = full_time_student | disabled_student

        tuition_addition = (
            full_time_or_disabled_student * p.amount.full_time_or_disabled
            + ~full_time_student * p.amount.part_time.non_disabled
        )

        return tuition + tuition_addition
