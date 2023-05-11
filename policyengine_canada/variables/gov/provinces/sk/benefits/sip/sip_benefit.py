from policyengine_canada.model_api import *


class sip_benefit(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan Seniors Income Plan Benefit"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p1 = parameters(period).gov.provinces.sk.SIP_benefit
        p2 = variables(period).gov.provinces.sk.benefits.sip_benefit
        
        number_pensioner = p2.count_pensioner
        income = p2.annual_taxable_income
        home = p2.is_living_at_home
        spouse_age < p1.age.spouse_age_threshold
        spouse_allowance = p2.is_spouse_receiving_allowance
        eligible = p2.sip_eligibility

        c1 = (receipient_age == True) & (home == True) & (number_pensioner == 1) & (income < p1.living_at_home.annual_income_limit.single) & (eligible == True)
        c2 = (receipient_age == True) & (home == True) & (number_pensioner == 2) & (income < p1.living_at_home.annual_income_limit.married_both_pensioners) & (eligible == True)
        c3 = (receipient_age == True) & (home == True) & (spouse_age == True) & (income < p1.living_at_home.annual_income_limit.married_spouse_below_age_threshold) & (eligible == True)
        c4 = (receipient_age == True) & (home == True) & (number_pensioner == 1) & (income < p1.living_at_home.annual_income_limit.married_spouse_receiving_allowance) & (eligible == True)
        c5 = (receipient_age == True) & (home == False) & (number_pensioner == 1) & (income < p1.living_in_special_care_home.annual_income_limit.single) & (eligible == True)
        c6 = (receipient_age == True) & (home == False) & (number_pensioner == 2) & (income < p1.living_in_special_care_home.annual_income_limit.married_both_pensioners) & (eligible == True)
        c7 = (receipient_age == True) & (home == False) & (spouse_age == True) & (income < p1.living_in_special_care_home.annual_income_limit.married_spouse_below_age_threshold) & (eligible == True)
        c8 = (receipient_age == True) & (home == False) & (number_pensioner == 1) & (income < p1.living_in_special_care_home.annual_income_limit.married_spouse_receiving_allowance) & (eligible == True)

    
        sip = where(c1, p1.living_at_home.max_sip_benefit.single, 
                            where(c2, p1.living_at_home.max_sip_benefit.married_both_pensioners, 
                                  where(c3, p1.living_at_home.max_sip_benefit.married_spouse_below_age_threshold,
                                        where(c4, p1.living_at_home.max_sip_benefit.married_spouse_receiving_allowance, 
                                              where(c5, p1.living_in_special_care_home.max_sip_benefit.single,
                                                    where(c6, p1.living_in_special_care_home.max_sip_benefit.married_both_pensioners, 
                                                          where(c7, p1.living_in_special_care_home.max_sip_benefit.married_spouse_below_age_threshold,
                                                                where(c8, p1.living_in_special_care_home.max_sip_benefit.married_spouse_receiving_allowance, 0)))
    
        c9 = (receipient_age == True) & (home == True) & (number_pensioner == 1) & (income < p1.living_at_home.annual_income_limit.single) & (eligible == False)
        c10 = (receipient_age == True) & (home == True) & (number_pensioner == 2) & (income < p1.living_at_home.annual_income_limit.married_both_pensioners) & (eligible == False)
        c11 = (receipient_age == True) & (home == True) & (spouse_age == True) & (income < p1.living_at_home.annual_income_limit.married_spouse_below_age_threshold) & (eligible == False)
        c12 = (receipient_age == True) & (home == True) & (number_pensioner == 1) & (income < p1.living_at_home.annual_income_limit.married_spouse_receiving_allowance) & (eligible == False)
        c13 = (receipient_age == True) & (home == False) & (number_pensioner == 1) & (income < p1.living_in_special_care_home.annual_income_limit.single) & (eligible == False)
        c14 = (receipient_age == True) & (home == False) & (number_pensioner == 2) & (income < p1.living_in_special_care_home.annual_income_limit.married_both_pensioners) & (eligible == False)
        c15 = (receipient_age == True) & (home == False) & (spouse_age == True) & (income < p1.living_in_special_care_home.annual_income_limit.married_spouse_below_age_threshold) & (eligible == False)
        c16 = (receipient_age == True) & (home == False) & (number_pensioner == 1) & (income < p1.living_in_special_care_home.annual_income_limit.married_spouse_receiving_allowance) & (eligible == False)


        ccp = where(c9, p1.living_at_home.ccp_income.single, 
                            where(c10, p1.living_at_home.ccp_income.married_both_pensioners, 
                                  where(c11, p1.living_at_home.ccp_income.married_spouse_below_age_threshold,
                                        where(c12, p1.living_at_home.ccp_income.married_spouse_receiving_allowance,
                                                where(c13, p1.living_in_special_care_home.ccp_income.single,
                                                    where(c14, p1.living_in_special_care_home.ccp_income.married_both_pensioners, 
                                                          where(c15, p1.living_in_special_care_home.ccp_income.married_spouse_below_age_threshold,
                                                                where(c16, p1.living_in_special_care_home.ccp_income.married_spouse_receiving_allowance, 0))) 

    
        benefit = sip + ccp
        return benefit