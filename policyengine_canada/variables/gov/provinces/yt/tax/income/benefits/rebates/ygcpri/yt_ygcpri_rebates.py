from policyengine_canada.model_api import *


class gycpri_rebates(Variable):
    value_type = float
    entity = Household
    label = "Yukon ygcpri rebates"
    unit = CAD
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/child-family-benefits/provincial-territorial-programs/yukon.html#YGCPRI"
    defined_for = ProvinceCode.YT

    def formula(household, period, parameters):
        children = household("yt_ygcpri_eligible_children", period)
        spouses = household("yt_ygcpri_spouses", period)
        remote = household("lived_outside_of_Whitehorse", period)
        p = parameters(period).gov.provinces.yt.benefits.rebates.ygcpri
        supplement = remote*(p.supplement.child*children + p.supplement.spouse*spouses + p.supplement.self)
        return p.amount.child*children + p.amount.spouse*spouses + p.amount.self + supplement