import random
import pandas as pd
import prairielearn as pl

from flask import Flask, request, jsonify

#import d8 package?
# from datascience import *
import datascience as ds


def generate(data):
    data["correct_answers"]["mcq"] = "SORT"
    data["correct_answers"]["desc"] = "TRUE"
    
    #next: import CSV instead of manually typing out table
    
    d = {
        "Actor": ["Harrison Ford", "Samuel L. Jackson", "Morgan Freeman", "Tom Hanks", "Robert Downey Jr.", "Eddie Murphy"],
        "Total Gross": [4871.7, 4772.8, 4468.3, 4340.8, 3947.3, 3810.4],
        "Number of Movies": [41,69,61,44,53,38],
        "Avg per Movie": [118.8,69.2,73.3,98.7,74.5,100.3],
        "#1 Movie": ["Star Wars: The Force Awakens", "The Avengers", "The Dark Knight", "Toy Story 3", "The Avengers", "Shrek 2"],
        "Gross": [936.7,623.4,534.9,415,623.4,441.2]
            }
    df = pd.DataFrame(data=d)
    data["params"]["df"] = pl.to_json(df)    
    
    # if data["submitted_answers"].get(["mcq"],"") and data["submitted_answers"].get(["desc"],""):
    #     mcq = data["submitted_answers"].get("mcq", "")
    #     desc = data["submitted_answers"].get("desc","")    
            
    #     if (mcq == "SORT"):
    #         if (desc == "TRUE"):
    #             df_sorted = df.sort_values(by="Number of Movies", ascending=False)
    #             data["params"]["df"] = pl.to_json(df_sorted)
    #         elif (desc == "FALSE"):
    #             df_sorted = df.sort_values(by="Number of Movies", ascending=True)
    #             data["params"]["df"] = pl.to_json(df_sorted)
    #     else:    
    #         data["params"]["df"] = pl.to_json(df)
    # else:
    #     data["params"]["df"] = pl.to_json(df)  

def generate_2(data, mcq, desc):
    # Based on the selected options for mcq and desc, generate the DataFrame
    
    d = {
        "Actor": ["Harrison Ford", "Samuel L. Jackson", "Morgan Freeman", "Tom Hanks", "Robert Downey Jr.", "Eddie Murphy"],
        "Total Gross": [4871.7, 4772.8, 4468.3, 4340.8, 3947.3, 3810.4],
        "Number of Movies": [41,69,61,44,53,38],
        "Avg per Movie": [118.8,69.2,73.3,98.7,74.5,100.3],
        "#1 Movie": ["Star Wars: The Force Awakens", "The Avengers", "The Dark Knight", "Toy Story 3", "The Avengers", "Shrek 2"],
        "Gross": [936.7,623.4,534.9,415,623.4,441.2]
    }
    
    df = pd.DataFrame(data=d)
    
    # Apply operations based on mcq and desc
    if mcq == "SORT":
        if desc == "TRUE":
            df_sorted = df.sort_values(by="Number of Movies", ascending=False)
            data["params"]["df"] = pl.to_json(df_sorted)
        elif desc == "FALSE":
            df_sorted = df.sort_values(by="Number of Movies", ascending=True)
            data["params"]["df"] = pl.to_json(df_sorted)

    
def parse(data):
    if data["submitted_answers"]["mcq"] == "":
        data["format_errors"]["mcq"] = "Please select a table method."     
    if data["submitted_answers"]["desc"] == "":
        data["format_errors"]["desc"] = "Please select the descending parameter."

def grade(data):
    d = {
        "Actor": ["Harrison Ford", "Samuel L. Jackson", "Morgan Freeman", "Tom Hanks", "Robert Downey Jr.", "Eddie Murphy"],
        "Total Gross": [4871.7, 4772.8, 4468.3, 4340.8, 3947.3, 3810.4],
        "Number of Movies": [41,69,61,44,53,38],
        "Avg per Movie": [118.8,69.2,73.3,98.7,74.5,100.3],
        "#1 Movie": ["Star Wars: The Force Awakens", "The Avengers", "The Dark Knight", "Toy Story 3", "The Avengers", "Shrek 2"],
        "Gross": [936.7,623.4,534.9,415,623.4,441.2]
            }
    df = pd.DataFrame(data=d)
    if data["submitted_answers"]["mcq"] == "SORT":
        if data["submitted_answers"]["desc"] == "FALSE":
            df_sorted = df.sort_values(by="Number of Movies", ascending=True)
            data["params"]["df"] = pl.to_json(df_sorted)
        elif data["submitted_answers"]["desc"] == "TRUE":
            df_sorted = df.sort_values(by="Number of Movies", ascending=False)
            data["params"]["df"] = pl.to_json(df_sorted)
    elif data["submitted_answers"]["mcq"] == "TAKE":
        df_select = df.loc[:,["Number of Movies"]]
        data["params"]["df"] = pl.to_json(df_select)
        
    elif data["submitted_answers"]["mcq"] == "GROUP":
        df_group = df.groupby(["Number of Movies"]).size().reset_index(name="count")
        data["params"]["df"] = pl.to_json(df_group)
        
    elif data["submitted_answers"]["mcq"] == "WHERE":
        df_where = df.where(df["Number of Movies"] > 45)
        data["params"]["df"] = pl.to_json(df_group)    
        
    # elif data["submitted_answers"]["mcq"] == "": #reset table?
    #     data["params"]["df"] = pl.to_json(df)
    # elif data["submitted_answers"]["mcq"] == "TAKE":
    #     df_selected = df["Number of Movies"]
    #     data["params"]["df"] = pl.to_json(df_selected)
        
            
    
# def parse(data):
#     # use get() for submitted_answers in case no answer was submitted
#     # get the submitted answer, defaulting to empty string if it's missing
#     mcq = data["submitted_answers"].get("mcq", "")
#     desc = data["submitted_answers"].get("desc","")
    
#     d = {
#         "Actor": ["Harrison Ford", "Samuel L. Jackson", "Morgan Freeman", "Tom Hanks", "Robert Downey Jr.", "Eddie Murphy"],
#         "Total Gross": [4871.7, 4772.8, 4468.3, 4340.8, 3947.3, 3810.4],
#         "Number of Movies": [41,69,61,44,53,38],
#         "Avg per Movie": [118.8,69.2,73.3,98.7,74.5,100.3],
#         "#1 Movie": ["Star Wars: The Force Awakens", "The Avengers", "The Dark Knight", "Toy Story 3", "The Avengers", "Shrek 2"],
#         "Gross": [936.7,623.4,534.9,415,623.4,441.2]
#         }
#     df = pd.DataFrame(data=d)
    
#     if mcq == "SORT" and desc == "TRUE":
#         df_sorted = df.sort_values(by="Number of Movies", ascending=False)
#         #data["params"]["df_correct"] = pl.to_json(df_sorted) --> errors!! can't modify params???
#     elif mcq == "SORT" and desc == "FALSE":
#         df_sorted = df.sort_values(by="Number of Movies", ascending=True)
#         #data["params"]["df_incorrect"] = pl.to_json(df_sorted)
    
root_path = '/Users/sabrinama/Downloads/pl'
app = Flask(__name__, root_path = root_path)
@app.route('/pl/course/1/question/8/',methods=['POST'])
def grade_question():
    if request.method == 'POST':
        mcq = request.json.get('mcq','')
        desc = request.json.get('desc','')
        generate_2(request.json,mcq,desc)
        return jsonify({'message':'data is sent'})
    
# #dummy test
# @app.route('/pl/course/test')
# def test():
#     return 'This is a test route.'    

if __name__ == '__main__':
    app.run(debug=True)
    


