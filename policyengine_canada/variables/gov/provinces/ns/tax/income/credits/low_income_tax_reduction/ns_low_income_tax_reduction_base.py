from policyengine_canada.model_api import *


class ns_low_income_tax_reduction_base(Variable):
    value_type = float
    entity = Household
    label = "Nova Scotia low income tax reduction base"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(household, period, parameters):
        person = household.members
        p = parameters(
            period
        ).gov.provinces.ns.tax.income.credits.low_income_tax_reduction
        age = person("age", period)
        eligible = age > p.age_eligibility
        base = p.base.base
        spouse = person("is_spouse", period)
        spouse_amount = spouse * p.base.spouse
        dependant = person("is_dependant", period)
        dependant_amount = dependant * p.base.eligible_dependant
        return min_(
            p.base.max_amount,
            household.sum(
                eligible * (base + spouse_amount + dependant_amount)
            ),
        )
