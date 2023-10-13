from policyengine_canada.model_api import *


class qc_post_secondary_studies_transferred_amount_eligibility(Variable):
    value_type = bool
    entity = Person
    label = "Quebec transferred amount for a child 18 or over enrolled in post-secondary studies eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.dependant_amount.child_in_post_secondary_studies.transferred_amount

        age_eligible = person("age", period) >= p.age_eligibility
        is_full_time_student = person("is_full_time_student", period)

        # a child can transfer to his/her mother or father
        is_child_of_filer = person("is_child_of_filer", period)

        # TODO: cannot claimany any work premium related credit

        return age_eligible & is_full_time_student & is_child_of_filer
