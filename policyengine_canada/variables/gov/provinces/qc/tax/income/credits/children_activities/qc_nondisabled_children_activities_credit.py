from policyengine_canada.model_api import *


class qc_nondisabled_children_activities_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec nondisabled children's activities tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.children_activities

        age = person("age", period)
        nondisabled = ~person("is_disabled", period)
        eligible = nondisabled * p.nondisabled_children_age_eligibility.calc(
            age
        )

        eligible_fee = min_(
            person("children_activities_fees", period),
            p.nondisabled_children_activities_fee_limit,
        )
        return eligible * eligible_fee * p.rate
