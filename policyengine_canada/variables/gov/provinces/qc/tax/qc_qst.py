from policyengine_canada.model_api import *


class qc_qst(Variable):
    value_type = float
    entity = Person
    label = "Québec sales tax (QST)"
    unit = CAD
    definition_period = YEAR
