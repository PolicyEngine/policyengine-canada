from policyengine_canada.model_api import *


class qc_non_disabled_children_activities_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec nondisabled children's activities tax credit"
    definition_period = YEAR
    defined_for = "qc_non_disabled_children_activities_credit_eligible"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.children_activities

        eligible_fee = min_(
            person("physical_activities_fees", period),
            p.non_disabled_children.fee_limit,
        )
        return eligible_fee * p.rate
