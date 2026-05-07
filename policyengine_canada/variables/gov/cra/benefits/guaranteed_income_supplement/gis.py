from policyengine_canada.model_api import *


class gis(Variable):
    value_type = float
    entity = Person
    label = "Guaranteed Income Supplement"
    unit = CAD
    definition_period = YEAR
    documentation = "Annual Guaranteed Income Supplement payment for low-income seniors"

    def formula(person, period, parameters):
        # Check eligibility
        eligible = person("gis_eligible", period)
        
        if not eligible.any():
            return person.empty_array()
        
        # Get GIS-specific income
        gis_income = person("gis_income", period)
        
        # Get marital status at person level
        is_head = person("is_head", period)
        is_spouse = person("is_spouse", period)
        
        # Check if household is single (will be same for all household members)
        is_single_household = person.household("is_single", period)
        
        # Get parameters
        p_gis = parameters(period).gov.cra.benefits.guaranteed_income_supplement
        
        # Calculate base amount and threshold based on marital status
        # For now, simplified to single vs couple where both get OAS
        # TODO: Add other couple scenarios (spouse no OAS, spouse gets Allowance)
        max_amount = where(
            is_single_household,
            p_gis.amount.single * 12,  # Convert monthly to annual
            p_gis.amount.couple_both_oas * 12
        )
        
        income_threshold = where(
            is_single_household,
            p_gis.threshold.single,
            p_gis.threshold.couple_both_oas
        )
        
        # For couples, use combined income
        # Aggregate household income for GIS calculation
        household_gis_income = where(
            is_single_household,
            gis_income,
            person.household.sum(gis_income)  # Sum all household members' GIS income
        )
        
        # Calculate reduction based on income
        # GIS is reduced by 50 cents for every dollar of income
        # The threshold is actually the maximum income to receive any GIS
        reduction = household_gis_income * p_gis.reduction_rate
        
        # Calculate final benefit
        gis_benefit = max_(0, max_amount - reduction)
        
        # Apply eligibility
        return where(eligible, gis_benefit, 0)