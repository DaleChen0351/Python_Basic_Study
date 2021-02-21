import pandas as pd
import numpy as np


def get_circumcircle_area(l,h):
    r = np.sqrt(l**2+h**2) / 2
    return r**2*np.pi

rects = pd.read_excel("data/30.xlsx",index_col="ID")

rects["area"] = rects.apply(lambda row:get_circumcircle_area(row["Length"],row["Height"]),axis=1)
print(rects)