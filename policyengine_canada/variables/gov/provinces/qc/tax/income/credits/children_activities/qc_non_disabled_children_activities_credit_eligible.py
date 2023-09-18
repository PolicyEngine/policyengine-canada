from policyengine_canada.model_api import *


class qc_non_disabled_children_activities_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = (
        "Eligible for the Quebec non-disabled children's activities tax credit"
    )
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.children_activities

        age = person("age", period)
        non_disabled = ~person("is_disabled", period)
        return non_disabled * p.non_disabled_children.age_eligibility.calc(age)
