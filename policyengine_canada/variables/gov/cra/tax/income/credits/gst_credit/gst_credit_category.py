from policyengine_canada.model_api import *


class GSTCreditCategory(Enum):
    HEAD = "Head"
    SPOUSE = "Spouse"
    CHILD = "Child"


class gst_credit_category(Variable):
    value_type = Enum
    entity = Person
    possible_values = GSTCreditCategory
    default_value = GSTCreditCategory.HEAD
    definition_period = YEAR

    def formula(person, period, parameters):
        child = person("is_child_for_gst_credit", period)
        return select(
            [person("is_head", period), person("is_spouse", period), child],
            [
                GSTCreditCategory.HEAD,
                GSTCreditCategory.SPOUSE,
                GSTCreditCategory.CHILD,
            ],
        )
