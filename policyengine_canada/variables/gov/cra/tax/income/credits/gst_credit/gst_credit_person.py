from policyengine_canada.model_api import *


class gst_credit_person(Variable):
    value_type = float
    entity = Person
    label = "GST credit amount for a particular individual in a household. We'll sum these in a separate variable."
    unit = CAD
    documentation = "Determination of the amount per individual"
    definition_period = YEAR

    def formula(person, period, parameters):
        category = person("gst_credit_category", period)
        amounts = parameters(
            period
        ).gov.cra.tax.income.credits.gst_credit.base_amounts
        return amounts[category]
