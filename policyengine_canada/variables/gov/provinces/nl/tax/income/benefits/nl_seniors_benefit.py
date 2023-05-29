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
        total_family_income = household.sum(net_income)

        income_eligibility = (total_family_income > p.lower_income_threshold) & (total_family_income < p.higher_income_threshold)

        senior_benefit = p.max_amount * person_eligibility * income_eligibility * p.rate * (p.max_amount + total_family_income - p.higher_income_threshold)

        return senior_benefit