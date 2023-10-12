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
        ).gov.provinces.qc.tax.income.credits.child_pursuing_studies.amount

        # Dependent child’s income
        net_income = person("individual_net_income", period)
        # TODO: add remote deduction line 236
        other_income = person("qc_other_income", period)
        income = max_(0, net_income - other_income)  # +remote deduction

        return max_(
            0, p.post_secondary_studies_amount - income
        )  # TODO: check per term
