from policyengine_canada.model_api import *


class mb_renters_tax_credit(Variable):
    value_type = float
    entity = Person
    label = "Manitoba renters tax credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.renters_tax_credit

        age = person("age", period)
        age_eligible = age >= p.age_amount

        # household net income
        net_income = person("adjusted_family_net_income", period)

        # rent
        rent = person("rent", period)

        # education property tax credit
        ### waiting for issue418 to use this variable
        education_property_tax_credit = person(
            "mb_education_property_tax_credit_amount", period
        )

        max_amount_allowed = min_(
            p.max_value, net_income * p.applicable_percentage
        )

        age_eligible_credit = age_eligible * (
            (p.base_amount - max_amount_allowed) / p.months_in_year
        )
        max_tax_credit = max_(age_eligible_credit, p.credit_value)

        number_of_months_in_rentals = person(
            "months_living_in_rentals", period
        )

        renters_tax_credit_amount = (
            min_(max_tax_credit * number_of_months_in_rentals, rent)
            + education_property_tax_credit
        )

        return renters_tax_credit_amount
