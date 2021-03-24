from graph import graph
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from plant import plant
from graph import graph

def main():

    aloe = plant("Aloe")
    big_root = plant("Big Root")
    succulent = plant("Suculant")

    plants = [aloe, big_root, succulent]

    moisture = graph("Moisture Over Time", "Time (days)", "Moisture level", plants)
    temp = graph("Temp Over Time", "Time (Days)", "Temp. (Degrees F)", plants)

    moisture.show_graph()

main()