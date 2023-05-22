from policyengine_canada.model_api import *


class sk_housing_benefit_eligible(Variable):
    value_type = bool
    entity = Household
    label = "Saskatchewan Housing Benefit Eligibility"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.benefits.housing_benefit
        income = household("adjusted_family_net_income.py", period)
        rent = household("rent", period)
        dependants = household("count_dependants",period)
        utility_costs = household("utilities_costs", period)
        #1 spend on rent and utilities >= 35% annual before tax household income
        precentage_spend_housing = (rent + utility_costs) / income
        shelter_costs_eligibility = precentage_spend_housing >= p1.amount.lower_threshold.threshold
        #2 have < 300000 in household assets
        household_assets_eligibility = household("household_assets",period) < p1.housing_assets_limit
        #3 annual before-tax household income requirement within its limitation
        annual_income_threshold = select(
            [
                dependants == 0, 
                dependants == 1, 
                dependants >= 2
        ],
        [
            p.income_limit.no_dependants,  
            p.income_limit.one_dependants, 
            p.income_limit.two_or_more_dependants
            ], 
        )
        income_eligibility = income <= annual_income_threshold
        
        #4 Not receive support from another Government of Saskatchewan income assistance or training program;
        sk_income_assitance = household("sk_income_assistance", period)
        income_assistance_eligibility = sk_income_assitance == 0

        #5 Not rent from a housing authority under the Social Housing Program
        sk_social_housing_program = household("sk_social_housing_program", period)
        social_housing_eligibility = sk_social_housing_program == 0

        #6 Not a full-time post-secondary student
        person = household.members
        student = person("is_full_time_student", period)
        students = household.any(student)
        student_eligibility = (students == 0)

        return shelter_costs_eligibility & household_assets_eligibility & income_eligibility & income_assistance_eligibility & social_housing_eligibility & student_eligibility


       
