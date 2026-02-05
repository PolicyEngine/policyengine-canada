from policyengine_canada.model_api import *


class qc_disabled_children_activities_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec disabled children's activities tax credit"
    definition_period = YEAR
    defined_for = "qc_disabled_children_activities_credit_eligible"

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.children_activities

        fees = person("physical_activities_fees", period)
        additional_credit_amount = p.disabled_children.subsidy.calc(fees)
        capped_credit = min_(
            fees + additional_credit_amount, p.disabled_children.fee_limit
        )

        return capped_credit * p.rate
