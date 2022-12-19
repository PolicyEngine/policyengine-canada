from policyengine_canada.model_api import *


class canada_workers_benefit_disability_supplement_phase_in(Variable):
    value_type = float
    entity = Household
    label = "Canada workers benefit disability supplement phase in"
    definition_period = YEAR

    def formula(household, period, parameters):
        income = household.person("working_income", period)
        p = parameters(period).gov.cra.benefits.cwb
        disabled = household.person(
            "canada_workers_benefit_disability_supplement_eligible", period
        )
        return disabled & p.phase_in.disability_supplement.calc(income)
