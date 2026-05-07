from policyengine_canada.model_api import *


class gis_income(Variable):
    value_type = float
    entity = Person
    label = "Income for GIS purposes"
    unit = CAD
    definition_period = YEAR
    documentation = "Income used to calculate GIS benefits (excludes OAS and GIS itself)"

    def formula(person, period, parameters):
        # GIS income calculation excludes OAS and GIS payments
        # But includes most other income sources
        
        # Employment and self-employment income
        employment_income = person("employment_income", period)
        self_employment_income = person("self_employment_income", period)
        
        # CPP/QPP income (when implemented, this would include CPP retirement benefits)
        # cpp_benefits = person("cpp_retirement_pension", period)  # TODO: implement
        cpp_benefits = 0  # Placeholder
        
        # Private pension income
        # pension_income = person("pension_income", period)  # TODO: implement if exists
        pension_income = 0  # Placeholder
        
        # Investment income
        # investment_income = person("investment_income", period)  # TODO: implement
        investment_income = 0  # Placeholder
        
        # EI benefits (when implemented)
        # ei_benefits = person("ei_benefits", period)  # TODO: implement
        ei_benefits = 0  # Placeholder
        
        # Total GIS income (OAS and GIS are excluded)
        total_gis_income = (
            employment_income +
            self_employment_income +
            cpp_benefits +
            pension_income +
            investment_income +
            ei_benefits
        )
        
        return total_gis_income