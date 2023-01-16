from policyengine_canada.model_api import *

class gis_eligible(Variable):
    value_type = bool
    entity = Person
    label = "Eligible for guaranteed income supplement"
    definition_period = YEAR

    def formula(person, period, parameters):
        p = parameters(period).gov.cra.benefits.gis
        age = person("age", period) 
        # using the pre-repayment amount here because the documentation says "receives the OAS". 
        oas = person("old_age_security_pension_pre_repayment", period)
        income = 3

        # MAKE A 'type of household' variable!!
        # MAKE A 'maximum amount' parameter based on 'type of household'!!
        # MAKE A 'reduction rate' parameter based on 'type of household'? Copy GISRLS for example.
