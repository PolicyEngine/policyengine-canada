from policyengine_canada.model_api import *


class is_pensioner(Variable):
    value_type = bool
    entity = Person
    label = "Is a pensioner"
    definition_period = YEAR


# TODO: find out pension age in sk
# 55?
# 65?