from policyengine_canada.model_api import *


class ns_low_income_tax_reduction_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Nova Scotia low income tax reduction eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.NS

    def formula(person, period, parameters):
        age = person("age", period)
        return (
            age
            <= parameters(
                period
            ).gov.provinces.ns.tax.income.credits.low_income_tax_reduction.base.dependant.age_eligibility
        )
