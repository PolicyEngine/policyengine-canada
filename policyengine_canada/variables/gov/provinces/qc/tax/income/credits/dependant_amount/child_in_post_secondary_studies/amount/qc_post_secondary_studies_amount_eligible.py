from policyengine_canada.model_api import *


class qc_post_secondary_studies_amount_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Quebec amount for a child under 18 enrolled in post-secondary studies eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.dependant_amount.child_in_post_secondary_studies.amount

        # age eligibility
        age_eligible = person("age", period) < p.age_eligibility
        # is dependent
        is_dependant = person("is_dependant", period)
        # is full time student
        is_full_time_student = person("is_full_time_student", period)

        # no spouse or the spouse is not claiming an amount for credits transferred from one spouse to the other
        has_spouse = person("has_spouse", period)
        credit_transferred_by_spouse = person(
            "qc_credit_transferred_by_spouse", period
        )
        spouse_eligible = ~has_spouse | (credit_transferred_by_spouse == 0)

        return (
            age_eligible
            & is_dependant
            & is_full_time_student
            & spouse_eligible
        )
