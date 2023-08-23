from policyengine_canada.model_api import *


class qc_fa_supplement(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance supplement"
    reference = "https://www.legisquebec.gouv.qc.ca/en/document/cs/I-3?langCont=en#se:1029_8_61_18"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.fa

        person = household.members

        # check if the child is full custody of the head
        full_custody = person("full_custody", period)
        shared_custody_multiplier = where(
            full_custody, 1, p.shared_custody_multiplier
        )

        # Supplement for Handicapped Children
        handicapped = person("is_disabled", period)
        supplement_handicapped = (
            handicapped * p.supplement.handicapped_child.base_amount
        )

        # Supplement for the Purchase of School Supplies
        age = person("age", period)
        supplement_school_supplies = where(
            handicapped,
            p.supplement.school_supplies.handicapped_child.calc(age),
            p.supplement.school_supplies.non_handicapped_child.calc(age),
        )

        # Supplement for Handicapped Children Requiring Exceptional Care
        handicapped_tier1 = person("qc_fa_exceptional_care_tier1", period)
        supplement_handicapped_tier1 = (
            handicapped
            * handicapped_tier1
            * p.supplement.handicapped_child.exceptional_care_amount.tier1
        )

        handicapped_tier2 = person("qc_fa_exceptional_care_tier2", period)
        supplement_handicapped_tier2 = (
            handicapped
            * handicapped_tier2
            * p.supplement.handicapped_child.exceptional_care_amount.tier2
        )

        supplements = shared_custody_multiplier * (
            supplement_school_supplies
            + supplement_handicapped
            + supplement_handicapped_tier1
            + supplement_handicapped_tier2
        )

        return household.sum(supplements)
