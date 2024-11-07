#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:45:16 2024

@author: jeanettereisig
"""

ak = 15000 # årlig kilometer
fe = 5000 # forsikring elbil
fb = 7500 # forsikring bensinbil
k = 0.2 * ak #kwh
de = 2 * k #strømpris
ta = 8.38 # traffikavgift

x = fe + 365 * ta + de + ak * 0.1 # årlig kostnader elbil

y = fb + 365 * ta + ak + ak * 0.3 # årlig kostnader bensinbil

z = y - x # differanse

print("Elbil =", x, "kr", "Bensinbil =", y, "kr","Kostnadsdifferanse =", z, "kr")