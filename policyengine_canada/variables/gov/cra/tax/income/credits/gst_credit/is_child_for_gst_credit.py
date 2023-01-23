from policyengine_canada.model_api import *


class is_child_for_gst_credit(Variable):
    value_type = bool
    entity = Person
    label = "Is the child below the age limit for a household to get a credit for this child?"
    definition_period = YEAR

    def formula(person, period, parameters):
        dependent = person("is_dependent", period)
        age = person("age", period)
        adult_age = parameters(
            period
        ).gov.cra.tax.income.credits.gst_credit.adult_age
        return dependent & (age < adult_age)
