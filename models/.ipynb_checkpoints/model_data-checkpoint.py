import sys
import os
import pandas as pd

def read_data(path):
    top_books = pd.read_csv(path+"/top_books.csv")
    custrew = pd.read_csv(path+"/custrew.csv")
    return top_books,custrew
