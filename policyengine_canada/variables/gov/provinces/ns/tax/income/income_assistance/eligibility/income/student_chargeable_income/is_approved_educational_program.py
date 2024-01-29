from policyengine_canada.model_api import *


class is_approved_educational_program(Variable):
    value_type = bool
    entity = Person
    label = "Is attending approved educational program"
    definition_period = YEAR

# is attending a high school, adult day school, upgrading or literacy program, or
# technical or professional training of up to 2 years;