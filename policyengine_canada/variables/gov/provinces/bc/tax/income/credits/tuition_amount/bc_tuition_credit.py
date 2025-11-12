from policyengine_canada.model_api import *


class bc_tuition_credit(Variable):
    value_type = float
    entity = Person
    label = "British Columbia tuition credit"
    definition_period = YEAR
    defined_for: "bc_tuition_credit_eligibility"
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5010-s11/5010-s11-22e.pdf#page=1",  # BC(S11) line 10
        "https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/96215_00_multi#section4.62",  # section 4.62
    )

    def formula(person, period, parameters):
        age = person("age", period)
        tuition = person("tuition_expenses", period)
        taxable_income = person("bc_taxable_income", period)
        comprehensive_tax_credits = person(
            "bc_comprehensive_tax_credits", period
        )
        p = parameters(
            period
        ).gov.provinces.bc.tax.income.credits.tuition_amount
        net_income = max_(taxable_income - comprehensive_tax_credits, 0)
        tax_on_taxable_income = p.tax_bracket_rate.calc(taxable_income)
        net_tax = max_(
            (tax_on_taxable_income / p.lowest_tax_rate)
            - comprehensive_tax_credits,
            0,
        )
        return select(
            [
                taxable_income <= p.tax_bracket_rate.thresholds[1],
                taxable_income > p.tax_bracket_rate.thresholds[1],
            ],
            [
                min_(net_income, tuition),
                min_(net_tax, tuition),
            ],
        )
