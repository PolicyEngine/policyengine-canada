from policyengine_canada.model_api import *


class cce_eligible_nondisabled_child(Variable):
    value_type = bool
    entity = Person
    label = (
        "Quebec children care expenses tax credits eligible nondisabled child"
    )
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce
        age = person("age", period)
        return age <= p.age_eligibility
