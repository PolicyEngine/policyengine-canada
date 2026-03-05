from policyengine_canada.model_api import *


class is_family_child_care(Variable):
    value_type = bool
    entity = Person
    label = "Whether the child attends family or in-home multi-age child care (as opposed to group child care)"
    definition_period = YEAR
    default_value = False
    reference = "https://www2.gov.bc.ca/assets/gov/family-and-social-supports/child-care/childcarebc-programs/ccfri/ccfri_funding_guidelines_24_25.pdf#page=5"
