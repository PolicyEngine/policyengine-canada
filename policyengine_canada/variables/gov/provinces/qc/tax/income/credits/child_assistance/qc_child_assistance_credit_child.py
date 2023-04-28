from policyengine_canada.model_api import *


class qc_child_assistance_credit_child(Variable):
    value_type = bool
    entity = Person
    label = "Is a child for the Quebec Child Assitance Tax Credit"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        age = person("age", period)
        return age < parameters(period).gov.provinces.qc.tax.income.credits.child_assistance.age_eligibility
