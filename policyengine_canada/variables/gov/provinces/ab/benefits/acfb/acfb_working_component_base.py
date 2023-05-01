from policyengine_canada.model_api import *


class acfb_working_component_base(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit working component phased-in base amount"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.ab.benefits.acfb.working_component
        employment_income = household("family_employment_income", period)
        eligible_children = household("acfb_eligible_children", period)
        max_amount = (
            (p.base.one_child * (eligible_children > 0))
            + (p.base.two_children * (eligible_children > 1))
            + (p.base.three_children * (eligible_children > 2))
            + (p.base.four_or_more_children * (eligible_children > 3))
        )
        eligible = employment_income > p.phase_in.start
        phase_in = (employment_income - p.phase_in.start) * p.phase_in.rate
        phased_in = min_(max_amount, phase_in)
        return eligible * phased_in
