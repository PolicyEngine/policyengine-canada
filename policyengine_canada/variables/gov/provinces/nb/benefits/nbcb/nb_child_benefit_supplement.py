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
        # the supplement amount is reduced by 4% of "family earned income" in excess of $3,750 minus 5% of "family net income" in excess of $20,921.
        reduced_amount = max_(
            p.phase_in.calc(working_income) - p.phase_out.calc(income), 0
        )
        # The lesser of the base amount or teh reduced amount is utilized.
        return min_(p.base, reduced_amount)
