from policyengine_canada.model_api import *


class on_child_care_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Care Tax Credit (CARE Credit)"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.ONT
    reference = (
        "https://www.ontario.ca/laws/statute/07o11#BK181",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5006-tca/5006-tca-24e.pdf#page=1",
    )

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.on.tax.income.credits.child_care

        # Per ON479-A: adjusted income = net income + CCED + social benefits repayment
        # social_benefits_repayment is not modeled, so we approximate with:
        # family_net_income (line 23600 sum) + child_care_expense_deduction (line 21400)
        family_net_income = household("family_net_income", period)
        cced = household("child_care_expense_deduction", period)
        adjusted_income = family_net_income + cced

        eligible = adjusted_income <= p.income_limit

        # Per ON479-A: credit = rate(adjusted_income) x federal CCED (line 21400)
        credit_rate = p.rate.calc(adjusted_income)
        credit = credit_rate * cced

        return where(eligible, credit, 0)
