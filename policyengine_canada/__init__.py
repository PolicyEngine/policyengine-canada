import logging
import os
from pathlib import Path
from typing import Dict, Type

from policyengine_canada.entities import entities
from policyengine_canada.data.datasets.country_template_dataset import (
    CountryTemplateDataset,
)
from policyengine_core.data.dataset import Dataset
from policyengine_core.populations.population import Population
from policyengine_core.simulations import (
    Microsimulation as CoreMicrosimulation,
)
from policyengine_core.simulations import Simulation as CoreSimulation
from policyengine_core.taxbenefitsystems import TaxBenefitSystem

from .constants import COUNTRY_DIR

DATASETS = [CountryTemplateDataset]  # Important: must be instantiated


class CountryTaxBenefitSystem(TaxBenefitSystem):
    entities = entities
    variables_dir = COUNTRY_DIR / "variables"
    parameters_dir = COUNTRY_DIR / "parameters"
    auto_carry_over_input_variables = True
    basic_inputs = [
        "employment_income",
    ]


system = CountryTaxBenefitSystem()


class Simulation(CoreSimulation):
    default_tax_benefit_system = CountryTaxBenefitSystem
    default_tax_benefit_system_instance = system
    default_role = "parent"
    default_calculation_period = 2023
    default_input_period = 2023


class Microsimulation(CoreMicrosimulation):
    default_tax_benefit_system = CountryTaxBenefitSystem
    default_dataset = CountryTemplateDataset
    default_tax_benefit_system_instance = system
    default_dataset_year = 2023
    default_calculation_period = 2023


if 2022 not in CountryTemplateDataset.years:
    logging.warn("Default country template dataset not found. Building it.")
    CountryTemplateDataset.generate(2022)
