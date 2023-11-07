from policyengine_canada.model_api import *


class sk_seniors_income_plan_at_home(Variable):
    value_type = float
    entity = Person
    label = "Saskatchewan seniors income plan client category - living at home"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.sk.benefits.sip
        household = person.household
        cpp = person("canada_pension_plan_payout", period)
        income = person("individual_net_income", period)
        age = person("age", period)
        eligible = ~(person("special_care_home", period))
        pensioner = person("is_pensioner", period)
        married = household("is_married", period)
        count_pensioners = household.sum(pensioner)
        spouse_ineligible = person("is_spouse", period) & (age < p.age.spouse_threshold)
        received_allowance = person("received_allowance", period)
        gis_reduction = person("gis_reduction", period)
        gis_reduction_spouse_receiving_allowance = where(gis_reduction % 3 == 0,
                                                         (gis_reduction / 3),
                                                         ((gis_reduction // 3)+1)
                                                         )

        sip_benefit_at_home = eligible * (select(
            # Conditions.
            [(~married) & (pensioner == 1) & (cpp < p.living_at_home.cpp_income.single) & (income < p.living_at_home.annual_income_limit.single), 
             (married) & (count_pensioners == 2) & (cpp < p.living_at_home.cpp_income.married_both_pensioners) & (income < p.living_at_home.annual_income_limit.married_both_pensioners), 
             (married) & spouse_ineligible & (cpp < p.living_at_home.cpp_income.married_spouse_below_age_threshold) & (income < p.living_at_home.annual_income_limit.married_spouse_below_age_threshold), 
             (married) & (received_allowance > 0) & (cpp < p.living_at_home.cpp_income.married_spouse_receiving_allowance) & (income < p.living_at_home.annual_income_limit.married_spouse_receiving_allowance)],
            # Results.
            [
                p.living_at_home.max_amount.single - gis_reduction * p.living_at_home.reduction_rate.single, 
                p.living_at_home.max_amount.married_both_pensioners - gis_reduction * p.living_at_home.reduction_rate.married_both_pensioners,
                p.living_at_home.max_amount.married_spouse_below_age_threshold - gis_reduction * p.living_at_home.reduction_rate.married_spouse_below_age_threshold,
                p.living_at_home.max_amount.married_spouse_receiving_allowance - (gis_reduction_spouse_receiving_allowance) * p.living_at_home.reduction_rate.married_spouse_receiving_allowance,
            ],
            default=0
        ))
        
        sip_benefit_at_home = where(sip_benefit_at_home < 0, 0, sip_benefit_at_home)

        return sip_benefit_at_home

#TODO: add cpp payout elgibility in a separate select
# make test for variable
# do same for the special care home
# find out what the reduction is and add to formula