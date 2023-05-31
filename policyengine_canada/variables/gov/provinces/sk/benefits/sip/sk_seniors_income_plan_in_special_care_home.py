from policyengine_canada.model_api import *


class sk_seniors_income_plan_in_special_care_home(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan seniors income plan client category - living in special care home"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.benefits.sip
        income = household("adjusted_family_net_income", period)
        person = household.members
        age = person("age", period)
        eligible = (person("special_care_home", period))
        pensioner = person("is_pensioner", period)
        married = household("is_married", period)
        count_pensioners = household.sum(pensioner)
        spouse_ineligible = person("is_spouse", period) & (age < p.age.spouse_threshold)
        received_allowance = person("receive_allowance")
        return eligible * (select(
            # Conditions.
            [(~married) & (pensioner == true), (married) & (count_pensioners == 2), (married) & spouse_ineligible, (married) & (received_allowance > 0)],
            # Results.
            [
                p.living_in_special_care_home.max_amount.single, #need to add reduction & CPP eligibility,
                p.living_in_special_care_home.max_amount.married_both_pensioners,
                p.living_in_special_care_home.max_amount.married_spouse_below_age_threshold,
                p.living_in_special_care_home.max_amount.married_spouse_receiving_allowance,
            ],
            default=0,
        ))
