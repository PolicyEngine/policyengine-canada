from policyengine_canada.model_api import *


class gis_reduction(Variable):
    value_type = float
    entity = Person
    label = "Guaranteed Income Supplement Reduction"
    unit = CAD
    documentation = "The amount by which the base GIS is reduced, based on personal net income and the number of pensioners in the household. Equivalent of imgismax in the SPSD/M variable guide."
    definition_period = YEAR
