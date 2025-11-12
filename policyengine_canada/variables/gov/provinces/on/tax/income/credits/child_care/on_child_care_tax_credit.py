from policyengine_canada.model_api import *


class on_child_care_tax_credit(Variable):
    value_type = float
    entity = Household
    label = "Ontario Child Care Tax Credit (CARE Credit)"
    documentation = "Ontario Childcare Access and Relief from Expenses (CARE) Tax Credit - refundable credit based on childcare expenses and family income"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.ONT
    reference = "https://www.ontario.ca/page/ontario-child-care-tax-credit"

    def formula(household, period, parameters):
        # Get adjusted family net income
        income = household("adjusted_family_net_income", period)
        p = parameters(period).gov.provinces.on.tax.income.credits.child_care

        # Income must be at or below $150,000
        eligible = income <= p.income_limit

        # Get the credit rate based on income
        credit_rate = p.rate.calc(income)

        # Get childcare expenses and maximum amounts for each child
        person = household.members
        expenses = person("childcare_expense", period)
        age = person("age", period)
        is_disabled = person("is_disabled", period)

        # Calculate maximum credit per child based on age/disability
        max_credit_per_child = where(
            is_disabled,
            p.max_amount.disabled,
            where(
                age < p.max_amount.age_threshold,
                p.max_amount.under_7,
                p.max_amount.over_7,
            ),
        )

        # Credit is rate * min(expenses, max_amount)
        credit_per_child = credit_rate * min_(expenses, max_credit_per_child)

        # Sum across all children
        total_credit = household.sum(credit_per_child)

        return where(eligible, total_credit, 0)
