from policyengine_core.model_api import *
from policyengine_canada.entities import *

from policyengine_canada.variables.household.demographic.geographic.province_code import (
    ProvinceCode,
)
from functools import reduce
from policyengine_core.model_api import *
from policyengine_canada.entities import *
from policyengine_canada.tools.general import *
from pathlib import Path
from policyengine_canada.typing import *
import warnings

CAD = "currency-CAD"

warnings.filterwarnings("ignore")

REPO = Path(__file__).parent


def all_of_variables(variables: List[str]) -> Formula:
    def formula(entity, period, parameters):
        value = True
        for variable in variables:
            value = value & (add(entity, period, [variable]) > 0)
        return value

    return formula


PROVINCES = [
    "AB",
    "BC",
    "MB",
    "NB",
    "NL",
    "NS",
    "NT",
    "NU",
    "ON",
    "QC",
    "SK",
    "YT",
]
