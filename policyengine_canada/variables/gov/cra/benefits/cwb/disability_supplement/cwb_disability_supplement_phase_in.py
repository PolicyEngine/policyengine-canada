from policyengine_canada.model_api import *


class cwb_disability_supplement_phase_in(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit disability supplement phase in"
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household("family_working_income", period)
        p = parameters(
            period
        ).gov.cra.benefits.cwb.phase_in.disability_supplement
        return p.calc(income)
