from policyengine_canada.model_api import *


class qc_children_activities_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec children's activities tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.children_activities

        # income eligibility
        income_eligible = (
            household("adjusted_family_net_income", period) < p.income_limit
        )

        person = household.members

        # child elibility
        child_eligible = person("is_dependant", period)

        eligible = child_eligible * income_eligible

        # non-disabled child
        nondisabled_child_credit = eligible * person(
            "qc_nondisabled_children_activities_credit", period
        )
        # disabled child
        disabled_child_credit = eligible * person(
            "qc_disabled_children_activities_credit", period
        )

        credit = disabled_child_credit + nondisabled_child_credit

        return household.sum(credit)
