from policyengine_canada.model_api import *


class qc_amount_for_other_dependant(Variable):
    value_type = float
    entity = Person
    label = "Quebec amount for other dependants"
    definition_period = YEAR
    defined_for = "qc_amount_for_other_dependant_eligible"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.dependant_amount.other_dependant

        # Dependent’s income
        net_income = person("individual_net_income", period)
        # Line 236: deduction for residents of designated remote area
        designated_remote_area_travel_benefit = person(
            "qc_designated_remote_area_travel_benefit", period
        )
        # Line 154: Scholarships, bursaries or any similar financial assistance
        other_income = person("qc_other_income", period)

        dependent_income = max_(
            0,
            net_income + designated_remote_area_travel_benefit - other_income,
        )

        return max_(0, p.base_amount - dependent_income)
