from policyengine_canada.model_api import *


class (Variable):
    value_type = bool
    entity = Household
    label = ""
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.sip_benefit.max_amount
        income = household("adjusted_family_net_income", period)
        person = household.members
        age = person("age", period)
        special_care_home = person("special_care_home", period)
        pensioner = person("is_pensioner", period)
        filing_status = household("filing_status", period)
        count_pensioners = household.sum(pensioner)
        amount = select(
            # Conditions.
            [(filing_status == single) & (pensioner == true), (filing_status == married) & (count_pensioners == 2), children == 3, children > 3],
            # Results.
            [
                p.single #need to add reduction & CPP eligibility,
                p.two_children.calc(income),
                p.three_children.calc(income),
                p.four_or_more_children.calc(income),
            ],
            default=0,
        )
