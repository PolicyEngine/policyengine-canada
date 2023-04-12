from policyengine_canada.model_api import *


class childrens_sport_and_culture_participation_costs(Variable):
    value_type = int
    entity = Household
    unit = CAD
    label = " Childrens Sport and Culture Participation Costs"
    definition_period = YEAR
