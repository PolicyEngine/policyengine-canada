from policyengine_core.model_api import *
from policyengine_canada.entities import *


def in_province(province):
    def is_eligible(population, period, parameters):
        return population("province_code_str", period) == province

    return is_eligible
