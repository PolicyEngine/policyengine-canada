from policyengine_canada.model_api import *


class mb_education_property_tax_credit_amount(Variable):
    value_type = float
    entity = Person
    label = "Manitoba education property tax credit"
    unit = CAD
    definition_period = YEAR
    defined_for = ProvinceCode.MB

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.mb.tax.income.credits.education_property_tax_credit

        property_tax = p.applicable_percentage * (
            person("education_property_tax_received", period)
            + person("net_school_tax", period)
        )

        age = person("age", period)
        age_eligible = age >= p.age_amount
        age_ineligible = age < p.age_amount

        # household net income
        net_income = person("adjusted_family_net_income", period)

        eligible_age_credit = age_eligible * (
            p.basic_credit_age_eligible
            - p.family_income_applicable_rate * net_income
        )
        eligible_age_credit_max = max_(
            eligible_age_credit, p.basic_credit_age_ineligible
        )

        ineligible_age_credit = age_ineligible * p.basic_credit_age_ineligible

        time_at_education_property = (
            person("days_owning_education_property", period) / p.time_amount
        )

        education_property_tax_credit_amount = max_(
            0,
            (
                min_(
                    ineligible_age_credit * time_at_education_property,
                    property_tax,
                )
            )
            - person("education_property_tax_received", period),
        )

        return education_property_tax_credit_amount
