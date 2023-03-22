from policyengine_canada.model_api import *


class acfb_working_component_phase_in(Variable):
    value_type = float
    entity = Household
    label = "Alberta child and family benefit working component base amount"
    definition_period = YEAR
    defined_for = ProvinceCode.AB

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ab.tax.income.benefits.acfb.working_component
        employment_income = household("family_employment_income", period)
        max_amount = household("acfb_working_component_base", period)
        rate = p.phase_in.rate
        start = p.phase_in.start
        eligible = employment_income > start
        return eligible * min_(max_amount, (employment_income * rate))
