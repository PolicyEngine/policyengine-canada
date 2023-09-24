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
        ).gov.provinces.qc.tax.income.credits.children_activities.non_disabled_children

        # your or your spouse's child or a person of whom you or your spouse has the custody and supervision
        is_child_of_filer = person("is_child_of_filer", period)
        is_custodied_by_filer = person("is_custodied_by_filer", period)
        eligible_child = is_child_of_filer | is_custodied_by_filer

        age = person("age", period)
        non_disabled = ~person("is_disabled", period)
        return eligible_child & non_disabled & p.age_eligibility.calc(age)
