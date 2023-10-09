from policyengine_canada.model_api import *


class yt_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Yukon basic personal amount"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.basic_personal_amount

        applicable_amount = p.applicable_amount
        base_amount = p.base_amount
        divisor = p.divisor
        income_threshold = p.income_threshold

        individual_net_income = person("individual_net_income", period)
        additional_amount = divisor - (
            individual_net_income - income_threshold
        )
        additional_amount_eligible = additional_amount <= 0

        return where(
            additional_amount_eligible,
            base_amount,
            additional_amount / divisor * applicable_amount + base_amount,
        )
