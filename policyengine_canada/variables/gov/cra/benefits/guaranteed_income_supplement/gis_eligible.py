from policyengine_canada.model_api import *


class gis_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Guaranteed Income Supplement eligibility"
    definition_period = YEAR
    documentation = "Eligibility for the Guaranteed Income Supplement based on OAS eligibility and income"

    def formula(person, period, parameters):
        # Must be receiving OAS to get GIS
        oas_eligible = person("oas_eligibility", period)
        
        # Income test - simplified for now, will be refined with proper income calculation
        # GIS uses a special income definition that excludes OAS but includes most other income
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period)
        
        # For now, use basic income for eligibility
        # This will need to be expanded to include other income sources
        gis_income = employment_income + self_employment_income
        
        p_gis = parameters(period).gov.cra.benefits.guaranteed_income_supplement
        
        # For singles, check if income would still result in positive GIS
        # Maximum GIS phases out at twice the maximum amount (at 50% reduction rate)
        # TODO: Add proper couple handling
        max_gis = p_gis.amount.single * 12
        phase_out_income = max_gis / p_gis.reduction_rate
        income_eligible = gis_income < phase_out_income
        
        return oas_eligible & income_eligible