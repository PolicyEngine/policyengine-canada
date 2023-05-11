from policyengine_canada.model_api import *


class sip_eligiblility(Variable):
    value_type = bool
    entity = Household
    label = "Saskatchewan Seniors Income Plan Eligiblility"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p1 = parameters(period).gov.provinces.sk.sip_benefit
        p2 = variables(period).gov.provinces.sk.benefits.sip_benefit

        receipient_age >= p.age.recipient_age_eligibility
        number_pensioner = p2.count_pensioner
        income = p2.annual_taxable_income
        home = p2.is_living_at_home
        spouse_age < p1.age.spouse_age_threshold
        spouse_allowance = p2.is_spouse_receiving_allowance

        c1 = (
            (receipient_age == True)
            & (home == True)
            & (number_pensioner == 1)
            & (income < p1.living_at_home.annual_income_limit.single)
        )
        c2 = (
            (receipient_age == True)
            & (home == True)
            & (number_pensioner == 2)
            & (
                income
                < p1.living_at_home.annual_income_limit.married_both_pensioners
            )
        )
        c3 = (
            (receipient_age == True)
            & (home == True)
            & (spouse_age == True)
            & (
                income
                < p1.living_at_home.annual_income_limit.married_spouse_below_age_threshold
            )
        )
        c4 = (
            (receipient_age == True)
            & (home == True)
            & (number_pensioner == 1)
            & (
                income
                < p1.living_at_home.annual_income_limit.married_spouse_receiving_allowance
            )
        )
        c5 = (
            (receipient_age == True)
            & (home == False)
            & (number_pensioner == 1)
            & (
                income
                < p1.living_in_special_care_home.annual_income_limit.single
            )
        )
        c6 = (
            (receipient_age == True)
            & (home == False)
            & (number_pensioner == 2)
            & (
                income
                < p1.living_in_special_care_home.annual_income_limit.married_both_pensioners
            )
        )
        c7 = (
            (receipient_age == True)
            & (home == False)
            & (spouse_age == True)
            & (
                income
                < p1.living_in_special_care_home.annual_income_limit.married_spouse_below_age_threshold
            )
        )
        c8 = (
            (receipient_age == True)
            & (home == False)
            & (number_pensioner == 1)
            & (
                income
                < p1.living_in_special_care_home.annual_income_limit.married_spouse_receiving_allowance
            )
        )

        eligibility = where(c1 | c2 | c3 | c4 | c5 | c6 | c7 | c8, True, False)
        return eligibility


# sk_seniors_income_plan_at_home.py:
# sk_seniors_income_plan_at_in_special_care_home.py:
# special_care_home.py:
# is_pensioner.py: empty variable - person level
# recieved_allowance.py: empty variable
# sk_seniors_income_plan.py: add sk_seniors_income_plan_at_home.py + sk_seniors_income_plan_at_in_special_care_home.py:
# canada_pension_plan_payouts.py: empty variable
