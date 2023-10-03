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

        # check if full-time student
        full_time = person("is_full_time_student", period)

        # check if disabled
        disabled = person("is_disabled", period)

        tuition_addition = select(
            [full_time, disabled],
            [p.amount.full_time, p.amount.part_time.disabled],
            default=p.amount.part_time.non_disabled,
        )

        return tuition + tuition_addition
