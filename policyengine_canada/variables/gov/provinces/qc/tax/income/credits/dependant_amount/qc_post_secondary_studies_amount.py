from policyengine_canada.model_api import *


class qc_post_secondary_studies_amount(Variable):
    value_type = float
    entity = Person
    label = (
        "Quebec amount for a child under 18 enrolled in post-secondary studies"
    )
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.depedant_amount

        # Child under 18 enrolled in post-secondary studies
        age_eligible = person("age", period) < p.age_eligibility
        full_time_student = person("is_full_time_student", period)
        unmarried = ~person("has_spouse", period)

        eligible = age_eligible & full_time_student & unmarried

        # Dependent child’s income
        net_income = person("individual_net_income", period)
        # TODO: add remote deduction line 236
        other_income = person("qc_other_income", period)
        income = max_(0, net_income - other_income)  # +remote deduction

        return max_(
            0, p.post_secondary_studies_amount - income
        )  # TODO: check per term
