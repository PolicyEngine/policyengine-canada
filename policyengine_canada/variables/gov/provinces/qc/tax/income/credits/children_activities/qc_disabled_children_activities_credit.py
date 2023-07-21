from policyengine_canada.model_api import *


class qc_disabled_children_activities_credit(Variable):
    value_type = float
    entity = Person
    label = "Quebec disabled children's activities tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.children_activities

        age = person("age", period)
        disabled = person("is_disabled", period)

        eligible = disabled * p.disabled_children.age_eligibility.calc(age)

        fee = person("physical_activities_fees", period)
        fee_subsidy = p.disabled_children.subsidy.calc(fee)
        eligible_fee = min_(fee + fee_subsidy, p.disabled_children.fee_limit)

        return eligible * eligible_fee * p.rate
