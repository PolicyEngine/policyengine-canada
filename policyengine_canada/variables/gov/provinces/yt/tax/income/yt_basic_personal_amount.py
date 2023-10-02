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
        division = p.division
        income_threshold = p.income_threshold
        individual_net_income = person("individual_net_income", period)

        eligible = (division - (individual_net_income - income_threshold)) <= 0
        eligible_amount = division - (individual_net_income - income_threshold)

        return where(
            eligible,
            base_amount,
            eligible_amount / division * applicable_amount + base_amount,
        )
