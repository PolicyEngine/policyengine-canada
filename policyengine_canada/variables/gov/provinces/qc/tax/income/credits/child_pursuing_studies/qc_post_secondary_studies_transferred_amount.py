from policyengine_canada.model_api import *


class qc_post_secondary_studies_transferred_amount(Variable):
    value_type = float
    entity = Person
    label = "Quebec amount transferred by a child enrolled in post-secondary studies"
    definition_period = YEAR
    defined_for = "qc_post_secondary_studies_transferred_amount_eligibility"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.child_pursuing_studies.transferred_amount

        # Amount that you can transfer
        base_amount = p.base_amount
        post_secondary_studies_amount = person(
            "qc_post_secondary_studies_amount", period
        )

        # TODO: REDUCTION line 8-16
        # https://www.revenuquebec.ca/documents/en/formulaires/tp/2022-12/TP-1.D.S-V%282022-12%29.pdf

        # reduction when turned 18
        # line 358 https://www.revenuquebec.ca/en/citizens/income-tax-return/completing-your-income-tax-return/how-to-complete-your-income-tax-return/line-by-line-help/350-to-398-1-non-refundable-tax-credits/line-358/
        # solidarity
        solidarity_reduction = (
            household("qc_solidarity_credit", period) * p.solidarity_multiplier
        )
        reduction = solidarity_reduction

        credit = max_(
            0, base_amount + post_secondary_studies_amount - reduction
        )

        taxable_income = person("qc_taxable_income", period)

        return max_(0, credit - taxable_income)
