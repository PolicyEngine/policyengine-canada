from policyengine_canada.model_api import *


class yt_additional_basic_personal_amount(Variable):
    value_type = float
    entity = Person
    label = "Yukon additional basic personal amount"
    definition_period = YEAR
    defined_for = ProvinceCode.YT

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.yt.tax.income.credits.basic_personal_amount.additional

        individual_net_income = person("individual_net_income", period)
        additional_amount = p.divisor - (
            individual_net_income - p.income_threshold
        )
        additional_amount_eligible = additional_amount > 0
        yt_additional_amount = additional_amount_eligible * additional_amount
        yt_additional_amount = yt_additional_amount / p.divisor

        return yt_additional_amount * p.applicable_amount
