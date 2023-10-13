from policyengine_canada.model_api import *


class qc_post_secondary_studies_amount(Variable):
    value_type = float
    entity = Person
    label = (
        "Quebec amount for a child under 18 enrolled in post-secondary studies"
    )
    definition_period = YEAR
    defined_for = "qc_post_secondary_studies_amount_eligible"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.dependant_amount.child_in_post_secondary_studies.amount

        # Dependent child’s income
        net_income = person("individual_net_income", period)
        # Line 236: deduction for residents of designated remote area
        designated_remote_area_travel_benefit = person(
            "qc_designated_remote_area_travel_benefit", period
        )
        # Line 154: Scholarships, bursaries or any similar financial assistance
        other_income = person("qc_other_income", period)

        income = max_(
            0,
            net_income + designated_remote_area_travel_benefit - other_income,
        )  # +remote deduction

        return max_(0, p.post_secondary_studies_amount - income)
