from policyengine_canada.model_api import *


class nb_child_benefit(Variable):
    value_type = int
    entity = Household
    label = "New Brunswick child tax benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        children = household("nb_child_benefit_eligible_children", period)
        p = parameters(period).gov.provinces.nb.benefits.nbcb
        base = p.base * children
        supplement = household("nb_child_benefit_supplement", period)
        one_child_amount = max_(base - p.phase_out.one_child.calc(income), 0)
        multiple_children_amount = max_(
            base - p.phase_out.multiple_children.calc(income),
            0,
        )
        pre_supplement_amount = select(
            # Conditions.
            [children == 1, children > 1],
            # Results.
            [
                one_child_amount,
                multiple_children_amount,
            ],
            default=0,
        )
        return pre_supplement_amount + supplement
