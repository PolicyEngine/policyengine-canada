from policyengine_canada.model_api import *


class ns_basic_personal_credits(Variable):
    value_type = float
    entity = Person
    label = "Nova Scotia Basic Personal Amount"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.ns_basic_personal_amount
        taxable_income = person("total_individual_pre_tax_income", period)

        return select(
            [
                taxable_income <= p.lower_income_threshold,
                p.lower_income_threshold
                < taxable_income
                < p.higher_income_threshold,
                taxable_income >= p.higher_income_threshold,
            ],
            [
                p.additional_amount + p.basic_amount,
                p.basic_amount
                + 3000
                - p.applicable_rate
                * (taxable_income - p.lower_income_threshold),
                p.basic_amount,
            ],
        )
