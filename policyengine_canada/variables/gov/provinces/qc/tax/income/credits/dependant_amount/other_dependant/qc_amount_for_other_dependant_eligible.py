from policyengine_canada.model_api import *


class qc_amount_for_other_dependant_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Quebec amount for other dependants eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.dependant_amount.other_dependant

        # is dependant
        is_dependant = person("is_dependant", period)
        # age eligibility
        age_eligible = person("age", period) >= p.age_eligibility
        # not your spouse
        is_spouse = person("is_spouse", period)
        # Can not transfer the amount enrolled in post-secondary study
        post_secondary_studies_transferred_amount_eligible = (
            person("qc_post_secondary_studies_transferred_amount", period) == 0
        )

        return (
            is_dependant
            & age_eligible
            & ~is_spouse
            & post_secondary_studies_transferred_amount_eligible
        )
