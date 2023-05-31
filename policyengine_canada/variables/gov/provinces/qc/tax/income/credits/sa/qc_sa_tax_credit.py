from policyengine_canada.model_api import *


class qc_sa_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Quebec senior assistance tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.sa

        income = household("adjusted_family_net_income", period)

        # Your spouse is an eligible individual and you were both 70 or over
        married_both_eligible = household(
            "qc_sa_married_both_eligible", period
        )
        credit_married_both_eligible = married_both_eligible * max_(
            0,
            p.amount.married_both_eligible - p.reduction.married.calc(income),
        )

        # Your spouse is not an eligible individual or only one of you was 70 or over
        married_one_eligible = household("qc_sa_married_one_eligible", period)
        credit_married_one_eligible = married_one_eligible * max_(
            0, p.amount.married_one_eligible - p.reduction.married.calc(income)
        )

        # You did not have a spouse
        single = household("qc_sa_single", period)
        credit_single = single * max_(
            0, p.amount.single - p.reduction.single.calc(income)
        )

        return (
            credit_married_both_eligible
            + credit_married_one_eligible
            + credit_single
        )
