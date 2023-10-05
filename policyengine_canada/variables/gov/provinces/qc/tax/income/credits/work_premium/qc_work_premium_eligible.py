from policyengine_canada.model_api import *


class qc_work_premium_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Eligible household for the Quebec work premium tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.work_premium

        person = household.members

        # You were 18 or older
        age_eligible = person("age", period) >= p.age_eligibility

        # You were younger than 18 and met all following requirements
        has_spouse = household("is_married", period)
        has_child = household("count_children", period) > 0
        emancipated = person("is_emancipated", period)

        # You were not a full-time student
        not_full_time_student = ~person("is_full_time_student", period)

        has_emancipated_member = household.any(emancipated)
        no_full_time_students = household.any(not_full_time_student)

        return (
            age_eligible | (has_spouse & has_child & has_emancipated_member)
        ) & no_full_time_students
