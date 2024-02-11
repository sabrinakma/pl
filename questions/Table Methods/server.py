import random

import pandas as pd
import prairielearn as pl


def generate(data):    
    d = {
    "Actor": ["Harrison Ford", "Samuel L. Jackson", "Morgan Freeman", "Tom Hanks", "Robert Downey Jr.", "Eddie Murphy"],
    "Total Gross": [4871.7, 4772.8, 4468.3, 4340.8, 3947.3, 3810.4],
    "Number of Movies": [41,69,61,44,53,38],
    "Avg per Movie": [118.8,69.2,73.3,98.7,74.5,100.3],
    "#1 Movie": ["Star Wars: The Force Awakens", "The Avengers", "The Dark Knight", "Toy Story 3", "The Avengers", "Shrek 2"],
    "Gross": [936.7,623.4,534.9,415,623.4,441.2]
        }
    df = pd.DataFrame(data=d)
    #df_sorted = df.sort_values(by="Number of Movies", ascending=False)

    data["params"]["df"] = pl.to_json(df)
    data["correct_answers"]["mcq"] = "SORT"
    data["correct_answers"]["desc"] = "TRUE"
    
def parse(data):
    # use get() for submitted_answers in case no answer was submitted
    # get the submitted answer, defaulting to empty string if it's missing
    mcq = data["submitted_answers"].get("mcq", "")
    desc = data["submitted_answers"].get("desc","")
    
    d = {
        "Actor": ["Harrison Ford", "Samuel L. Jackson", "Morgan Freeman", "Tom Hanks", "Robert Downey Jr.", "Eddie Murphy"],
        "Total Gross": [4871.7, 4772.8, 4468.3, 4340.8, 3947.3, 3810.4],
        "Number of Movies": [41,69,61,44,53,38],
        "Avg per Movie": [118.8,69.2,73.3,98.7,74.5,100.3],
        "#1 Movie": ["Star Wars: The Force Awakens", "The Avengers", "The Dark Knight", "Toy Story 3", "The Avengers", "Shrek 2"],
        "Gross": [936.7,623.4,534.9,415,623.4,441.2]
        }
    df = pd.DataFrame(data=d)
    
    if mcq == "SORT" and desc == "TRUE":
        df_sorted = df.sort_values(by="Number of Movies", ascending=False)
        #data["params"]["df_correct"] = pl.to_json(df_sorted) --> errors!! can't modify params???
    elif mcq == "SORT" and desc == "FALSE":
        df_sorted = df.sort_values(by="Number of Movies", ascending=True)
        #data["params"]["df_incorrect"] = pl.to_json(df_sorted)
        
# def generate(data):
    # # Generates number of events.
    # x_events = random.randint(4, 7)

    # # Control rounding
    # n_digits = 2

    # # Generate random integers up to a number
    # r = [float(random.randint(1, 100)) for i in range(x_events)]

    # # Sum events
    # s = sum(r)

    # # Divide each value by sum to bring into [0, 1]
    # # Round events
    # a = [round(i / s, n_digits) for i in r]

    # # Enforce probability summation constraint
    # prob_sum = sum(a)
    # capped_sum = round(1 - prob_sum, n_digits)

    # # Truncate
    # if not capped_sum.is_integer():
    #     max_val = max(a)
    #     max_ind = a.index(max_val)
    #     a[max_ind] += capped_sum

    # d = {"P(X)": a}
    # df = pd.DataFrame(data=d)

    # data["params"]["df"] = pl.to_json(df)

    # data["correct_answers"]["p_sum"] = sum(a)
    # data["correct_answers"]["big_event"] = a.index(max(a))