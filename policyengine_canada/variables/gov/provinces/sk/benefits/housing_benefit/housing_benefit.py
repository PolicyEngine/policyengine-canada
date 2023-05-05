from policyengine_canada.model_api import *


class eligibility(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan Housing Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p1 = parameters(period).gov.provinces.sk.benefits.housing_benefit
        p2 = variables(period).household.income.household
        p3 = variables(period).household.expenses.housing

        #1 spend on rent and utilities >= 35% annual before tax household income
        housing_percentage = (p3.rent + p3.cost_on_utilities) / p2.market_income
        c1 = housing_percentage >= p1.amount.lower_threshold.threshold
        #2 have < 300000 in household assets
        c2 = household("household_assets",period) < p1.housing_assets_limit
        #3 annual before-tax household income requirement within its limitation
        annual_income_threshold = where(
            household("count_dependants",period)=0,
            annual_income_threshold = p1.income_limit.no_dependants,
            where(
                household("count_dependants",period)=1,
                annual_income_threshold = p1.income_limit.one_dependants,
                annual_income_threshold = p1.income_limit.two_or_more_dependants)
        )
        c3 = p2.market_income <= annual_income_threshold
        
        #4 Not receive support from another Government of Saskatchewan income assistance or training program;
        c4 = ~ p2.person.is_multiple_support_resources

        #5 Not rent from a housing authority under the Social Housing Program
        c5 = ~ p2.person.is_rent_socialhousing

        #6 Not a sponsored newcomer to Canada
        c6 = ~ p2.person.sponsored_newcomer

        #7 Not a full-time post-secondary student
        c7 = ~ p2.person.fulltime_postsecondary_student

        eligibility = c1 & c2 & c3 & c4 & c5 & c6 & c7

        where(
            eligibility = 0, 
            housing_benefit = 0, 
            where(
                housing_percentage <= p1.amount.higher_threshold.threshold,
                housing_benefit = where(
                    household("count_dependants",period)=0, 
                    p1.amount.lower_threshold.no_dependants,
                    where(
                        household("count_dependants",period)=1,
                        p1.amount.lower_threshold.one_dependants,
                        p1.amount.lower_threshold.two_or_more_dependants))
                housing_benefit = where(
                    household("count_dependants",period)=0, 
                    p1.amount.higher_threshold.no_dependants,
                    where(
                        household("count_dependants",period)=1,
                        p1.amount.higher_threshold.one_dependants,
                        p1.amount.higher_threshold.two_or_more_dependants))
                )
            )
            
        return housing_benefit
       
#use variables(period).household.income.household.market_income directly instead of setting a new variable
