from policyengine_canada.model_api import *


class nb_child_benefit_supplement(Variable):
    value_type = int
    entity = Household
    label = "New Brunswick child benefit supplement"
    definition_period = YEAR
    defined_for = ProvinceCode.NB

    def formula(household, period, parameters):
        income = household("adjusted_family_net_income", period)
        p = parameters(
            period
        ).gov.provinces.nb.benefits.nbcb.working_income_supplement
        working_income = household("family_working_income", period)
        return min_(
            p.base,
            max_(
                p.phase_in.calc(working_income) - p.phase_out.calc(income), 0
            ),
        )
