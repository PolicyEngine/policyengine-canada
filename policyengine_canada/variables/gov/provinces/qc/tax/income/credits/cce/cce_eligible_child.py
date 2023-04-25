from policyengine_canada.model_api import *


class cce_eligible_child(Variable):
    value_type = bool
    entity = Person
    label = "Quebec children care expenses tax credits eligible child"
    definition_period = YEAR
    defined_for = ProvinceCode.QC

    def formula(person, period, parameters):
        p = parameters(period).gov.provinces.qc.tax.income.credits.cce

        # the child must meet one of the following conditions:
        # (a) He or she was 16 or under at some point in the year.
        # (b) He or she had an infirmity and was your or your spouse's dependant (regardless of his or her age).

        # (a)
        age = person("age", period)

        # (b)
        # is_dependant = person("is_dependent", period) #!!!! should also considering > 18
        # is_disabled

        return age <= p.age_eligibility

        #todo: a child who was your or your spouse's dependant and whose income for the year was not more than $11,081.-> make parameter
