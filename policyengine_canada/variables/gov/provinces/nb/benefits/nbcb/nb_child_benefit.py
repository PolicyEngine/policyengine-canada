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
        return (
            select(
                # Conditions.
                [children == 1, children > 1],
                # Results.
                [
                    max_(base - p.one_child_phase_out.rate.calc(income), 0),
                    max_(
                        base - p.multiple_children_phase_out.rate.calc(income),
                        0,
                    ),
                ],
                default=0,
            )
            + supplement
        )
