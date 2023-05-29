from policyengine_canada.model_api import *


class nl_seniors_benefit(Variable):
    value_type = float
    entity = Household
    label = "Newfoundland and Labrador Seniors Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.NL

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.nl.tax.income.benefits

        # The person should be senior (which means whoes age over 65) or a family contains one senior
        person_eligibility = (person("age", period) >= p.age_eligible) | (person("age", period) >= p.age_eligible & person("is_spouse", period))

        net_income = person("household_net_income", period)
        income_eligibility = (net_income > p.lower_income_threshold) & (net_income <= p.higher_income_threshold)

        senior_benefit = p.max_amount * person_eligibility * income_eligibility * p.rate

        return min_(senior_benefit, p.max_amount)