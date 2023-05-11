from policyengine_canada.model_api import *


class sk_seniors_income_plan_at_home(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan seniors income plan client category - living at home"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.benefits.sip
        income = household("adjusted_family_net_income", period)
        person = household.members
        age = person("age", period)
        eligible = ~(person("special_care_home", period))
        pensioner = person("is_pensioner", period)
        filing_status = household("filing_status", period)
        count_pensioners = household.sum(pensioner)
        spouse_ineligible = person("is_spouse", period) & (age < p.age.spouse_threshold)
        received_allowance = person("receive_allowance")
        return eligible * (select(
            # Conditions.
            [(filing_status == single) & (pensioner == true), (filing_status == married) & (count_pensioners == 2), (filing_status == married) & spouse_ineligible, (filing_status == married) & (received_allowance > 0)],
            # Results.
            [
                p.living_at_home.max_amount.single, #need to add reduction & CPP eligibility,
                p.living_at_home.max_amount.married_both_pensioners,
                p.living_at_home.max_amount.married_spouse_below_age_threshold,
                p.living_at_home.max_amount.married_spouse_receiving_allowance,
            ],
            default=0,
        ))
