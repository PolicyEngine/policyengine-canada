from policyengine_canada.model_api import *


class qc_disabled_children_activities_credit_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for the Quebec disabled children's activities tax credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(
            period
        ).gov.provinces.qc.tax.income.credits.children_activities.disabled_children

        age = person("age", period)
        disabled = person("is_disabled", period)

        # your or your spouse's child or a person of whom you or your spouse has the custody and supervision
        is_dependant = person("is_dependant", period)

        return is_dependant & disabled & p.age_eligibility.calc(age)
