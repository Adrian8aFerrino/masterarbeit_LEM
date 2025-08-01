import os
import pandas as pd

from prep_consumption.consumption import sektor_demand_chow_lin
from prep_transmission.transmission import monte_carlo_loss
# TODO: Functions not yet written from prep_generation => lcoe_generation, ep_costs_generation, offset_generation
from config import select_folder



consumption_path = select_folder(message="Consumption")