from policyengine_canada.model_api import *


class qc_fa_supplement(Variable):
    value_type = float
    entity = Household
    label = "Quebec family allowance supplement"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.fa

        person = household.members

        # check if the child is full custody of the head
        full_custody = person("full_custody", period)
        reduction_rate = where(
            full_custody, full_custody, p.shared_custody_reduction
        )

        # Supplement for Handicapped Children
        handicapped = person("is_disabled", period)
        supplement_handicapped = (
            handicapped * p.handicapped_child_supplement.base_amount
        )

        # Supplement for the Purchase of School Supplies
        age = person("age", period)
        supplement_school_supplies = where(
            handicapped,
            p.school_supplies_supplement.handicapped_child.calc(age),
            p.school_supplies_supplement.non_handicapped_child.calc(age),
        )

        # Supplement for Handicapped Children Requiring Exceptional Care
        handicapped_tier1 = person("qc_fa_exceptional_care_tier1", period)
        supplement_handicapped_tier1 = (
            handicapped
            * handicapped_tier1
            * p.handicapped_child_supplement.exceptional_care_amount.tier1
        )

        handicapped_tier2 = person("qc_fa_exceptional_care_tier2", period)
        supplement_handicapped_tier2 = (
            handicapped
            * handicapped_tier2
            * p.handicapped_child_supplement.exceptional_care_amount.tier2
        )

        supplements = reduction_rate * (
            supplement_school_supplies
            + supplement_handicapped
            + supplement_handicapped_tier1
            + supplement_handicapped_tier2
        )

        return household.sum(supplements)