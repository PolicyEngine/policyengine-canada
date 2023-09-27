from policyengine_canada.model_api import *


class nb_tuition_credit_amount_income(Variable):
    value_type = float
    entity = Person
    label = "New Brunswick income pre tax income for tuition credit amount"
    unit = CAD
    definition_period = YEAR
    reference = (
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-c/5004-c-22e.pdf#page=2",
        "https://www.canada.ca/content/dam/cra-arc/formspubs/pbg/5004-s11/5004-s11-22e.pdf#page=1",
    )
    defined_for = ProvinceCode.NB
