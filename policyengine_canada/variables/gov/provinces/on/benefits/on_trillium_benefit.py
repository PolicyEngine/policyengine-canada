from policyengine_canada.model_api import *


class on_trillium_benefit(Variable):
    value_type = float
    entity = Household
    label = "Ontario trillium benefit"
    documentation = "Sum of the Ontario energy and property tax credit, the Northern Ontario energy credit, and the Ontario sales tax credit programs."
    definition_period = YEAR

    adds = ["oeptc", "on_sales_tax_credit", "northern_ontario_energy_credit"]
