from policyengine_canada.model_api import *


class provincial_sales_tax(Variable):
    value_type = float
    entity = Household
    label = "Provincial sales tax paid"
    definition_period = YEAR
    unit = CAD
    documentation = "Provincial Sales Tax (PST/QST) paid on consumption"
    
    def formula(household, period, parameters):
        consumption = household("consumption", period)
        province = household("province_code_str", period)
        p = parameters(period).gov.provinces.sales_tax
        
        # Get the PST rate for the province
        rate = p.pst_rate[province]
        
        # Calculate PST paid
        return consumption * rate