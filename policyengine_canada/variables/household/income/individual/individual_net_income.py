from policyengine_canada.model_api import *


class individual_net_income(Variable):
    value_type = float
    entity = Person
    label = "Individual Net Income"
    unit = CAD
    documentation = "The sum income from all sources, minus all eligible deductions such as RRSP contributions, childcare expenses, moving expenses, etc"
    definition_period = YEAR
    reference = "https://www.canada.ca/en/revenue-agency/services/tax/individuals/topics/about-your-tax-return/tax-return/completing-a-tax-return/deductions-credits-expenses/line-23600-net-income.html"

    def formula(tax_unit, period, parameters):
        total_income = tax_unit("total_individual_pre_tax_income", period)
        deductions_from_total_to_net_income = tax_unit(
            "deductions_from_total_to_net_income", period
        )
        return total_income - deductions_from_total_to_net_income
