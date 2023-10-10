from policyengine_canada.model_api import *


class qc_fa_eligibility(Variable):
    value_type = bool
    entity = Household
    label = "Quebec family allowance eligible household"
    reference = "https://www.legisquebec.gouv.qc.ca/en/document/cs/I-3?langCont=en#se:1029_8_61_8"
    definition_period = YEAR
    defined_for = ProvinceCode.QC
    adds = ["own_children_in_household"]

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.fa

        person = household.members
        # is parent and resides with of the eligible dependent child
        is_parent = person("own_children_in_household", period) > 0

        return household.any(is_parent)
