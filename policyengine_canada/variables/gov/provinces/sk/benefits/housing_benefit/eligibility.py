from policyengine_canada.model_api import *


class eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Saskatchewan Housing Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p1 = parameters(period).gov.provinces.sk.benefits.housing_benefit
        p2 = variables(period).household.income.household
        p3 = variables(period).household.expenses.housing

        #1 spend on rent and utilities >= 35% annual before tax household income
        c1 = ((p3.rent + p3.cost_on_utilities) / p2.market_income) >= p1.amount.lower_threshold.threshold
        #2 have < 300000 in household assets
        c2 = p1.household_assets < p1.housing_assets_limit
        #3 annual before-tax household income requirement within its limitation
        c3 = p2.market_income <= household_classify
        
        #4 Not receive support from another Government of Saskatchewan income assistance or training program;
        c4 = ~ p2.person.is_multiple_support_resources

        #5 Not rent from a housing authority under the Social Housing Program
        c5 = ~ p2.person.is_rent_socialhousing

        #6 Not a sponsored newcomer to Canada
        c6 = ~ p2.person.sponsored_newcomer

        #7 Not a full-time post-secondary student
        c7 = ~ p2.person.fulltime_postsecondary_student

        eligibility = c1 & c2 & c3 & c4 & c5 & c6 & c7
        return eligibility
       
#use variables(period).household.income.household.market_income directly instead of setting a new variable
