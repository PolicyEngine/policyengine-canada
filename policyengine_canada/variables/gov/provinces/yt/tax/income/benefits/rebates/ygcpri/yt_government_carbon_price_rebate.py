from policyengine_canada.model_api import *


class yt_government_carbon_price_rebate(Variable):
    value_type = float
    entity = Household
    label = "Yukon government carbon price rebate"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/yukon.html#YGCPRI"
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.yt.benefits.rebates.ygcpri
        person = household.members
        child = person("age", period) < p.child_ineligible_age
        children = household.sum(child)
        spouse = person("is_spouse", period)
        spouses = household.sum(spouse)
        in_whitehorse = household("in_whitehorse", period)
        non_whitehorse_supplement = ~in_whitehorse * (
            (p.non_whitehorse_supplement.child * children)
            + (p.non_whitehorse_supplement.spouse * spouses)
            + p.non_whitehorse_supplement.self
        )
        base = (
            (p.amount.child * children)
            + (p.amount.spouse * spouses)
            + p.amount.self
        )
        return base + non_whitehorse_supplement
