from policyengine_canada.model_api import *


class sa_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec senior assistance tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        income = household("adjusted_family_net_income", period)

        # Your spouse is an eligible individual and you were both 70 or over
        spouse_eligibility = household("sa_couple_eligibility", period)
        credit1 = spouse_eligibility * max_(
            0, 2 * p.base - p.reduction_eligible_spouse.calc(income)
        )

        # Your spouse is not an eligible individual or only one of you was 70 or over
        single_eligibility = household("sa_single_eligibility", period)
        credit2 = single_eligibility * max_(
            0, p.base - p.reduction_noneligible_spouse.calc(income)
        )

        # You did not have a spouse
        no_spouse = household("sa_no_spouse_eligibility", period)
        credit3 = no_spouse * max_(
            0, p.base - p.reduction_no_spouse.calc(income)
        )

        return credit1 + credit2 + credit3


        # todo: make the couple/single person level to household level
