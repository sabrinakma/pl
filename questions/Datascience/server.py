import random

import pandas as pd
import prairielearn as pl
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#datascience specific imports
import datascience
from datascience import Table

# table = Table.read_table('/Users/sabrinama/Downloads/actors.csv')
actors_table = Table.read_table('https://www.inferentialthinking.com/data/sat2014.csv')

def generate(data):
    data["correct_answers"]["operation"] = "SORT"
    data["correct_answers"]["desc"] = "TRUE"
    table = actors_table.take(np.arange(0,5))
    df = table.to_df()
    data["params"]["df"] = pl.to_json(df)    
    
    
def parse(data):
    if data["submitted_answers"]["operation"] == "":
        data["format_errors"]["operation"] = "Please select a table method."     
    if data["submitted_answers"]["desc"] == "":
        data["format_errors"]["desc"] = "Please select the descending parameter."

def grade(data):
    
    #df = actors_table.to_df()
    tbl = actors_table
    operation = data["submitted_answers"]["operation"]
    desc = data["submitted_answers"]["desc"]
    
    column = "Participation Rate"
    
    
    # if data["submitted_answers"]["mcq"] == "SORT":
    #     if data["submitted_answers"]["desc"] == "FALSE":
    #         df_sorted = df.sort_values(by="Number of Movies", ascending=True)
    #         data["params"]["df"] = pl.to_json(df_sorted)
    #     elif data["submitted_answers"]["desc"] == "TRUE":
    #         df_sorted = df.sort_values(by="Number of Movies", ascending=False)
    #         data["params"]["df"] = pl.to_json(df_sorted)
    # elif data["submitted_answers"]["mcq"] == "TAKE":
    #     df_select = df.loc[:,["Number of Movies"]]
    #     data["params"]["df"] = pl.to_json(df_select)
        
    # elif data["submitted_answers"]["mcq"] == "GROUP":
    #     df_group = df.groupby(["Number of Movies"]).size().reset_index(name="count")
    #     data["params"]["df"] = pl.to_json(df_group)
        
    # elif data["submitted_answers"]["mcq"] == "WHERE":
    #     df_where = df.where(df["Number of Movies"] > 45)
    #     data["params"]["df"] = pl.to_json(df_group)    
        
    # elif data["submitted_answers"]["mcq"] == "": #reset table?
    #     data["params"]["df"] = pl.to_json(df)
    # elif data["submitted_answers"]["mcq"] == "TAKE":
    #     df_selected = df["Number of Movies"]
    #     data["params"]["df"] = pl.to_json(df_selected)
    
        