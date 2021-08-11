#!/usr/bin/env python
"""
- Diana Esmeralda Jardon Vilchis
- Ing. Noé Vásquez Godínez

"""
# Import matplotlib
import matplotlib.pyplot as plt

# Import numpy structures
import numpy as np

# Read csv
import csv

# System
import sys

from datetime import datetime


def shockley(Idss,Vgs,Vp):
    id = Idss * ( ( 1 - (Vgs/Vp) ) * ( 1 - (Vgs/Vp) ))
    return id
    
def plot_data():
    csvfile = open("values-plot.csv",'r')
    csv_reader = csv.reader(csvfile, delimiter=',')

    start_time = datetime.now()
    print(start_time.now().strftime(" + [START] Time: %H Hours: %M Minutes: %S Seconds"))

    # extracting field names through first row
    fields = next(csv_reader)
    
    ids = []
    
    for row in csv_reader:
        ids.append( shockley(float(row[0]),float(row[1]),float(row[2])) )


    finish_time = datetime.now()
    print(finish_time.now().strftime(" + [DONE] Time: %H Hours: %M Minutes: %S Seconds"))
    print("\n")
    print("[INFO] Timestamp: ", (finish_time - start_time) )

    # Plot data
    plt.plot(ids,linestyle = 'dotted')
    # Setup plot
    plt.title("Curva característica de un transistor FET")

    plt.xlabel("+ VGS VT")
    plt.ylabel("Corriente ID")
    plt.show()

if __name__ == "__main__":
    """ The main function """
    try:
        plot_data()
    except KeyboardInterrupt:
        print(" Paátik in bin ...")
        sys.exit()