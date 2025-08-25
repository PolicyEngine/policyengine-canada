from policyengine_canada.model_api import *


class gst_hst(Variable):
    value_type = float
    entity = Household
    label = "GST/HST paid"
    definition_period = YEAR
    unit = CAD
    documentation = "Goods and Services Tax / Harmonized Sales Tax paid on consumption"
    
    def formula(household, period, parameters):
        consumption = household("consumption", period)
        province = household("province_code_str", period)
        p = parameters(period).gov.cra.tax.consumption.gst_hst
        
        # Get the GST/HST rate for the province
        rate = p.rate[province]
        
        # Calculate GST/HST paid
        return consumption * rate