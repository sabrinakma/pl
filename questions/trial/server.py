import random, math
import pandas as pd
import prairielearn as pl
import datascience
from datascience import Table

def generate(data):
    
    bikes_cat = ['Start Station', 'End Station', 'Subscriber Type']
    bikes_num = ['Start Terminal', 'End Terminal', 'Duration', 'Bike #']

    health_cat = ['Red Blood Cells', 'Pus Cell', 'Pus Cell clumps', 'Bacteria', 'Hypertension', 'Diabetes Mellitus', 'Coronary Artery Disease', 'Appetite', 'Pedal Edema', 'Anemia']
    health_num = ['Age', 'Blood Pressure', 'Specific Gravity', 'Albumin', 'Sugar', 'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 'White Blood Cell Count', 'Red Blood Cell Count']

    nba_cat = ['Name', 'Position']
    nba_num = ['Height', 'Weight', 'Age in 2013']

    flights_cat = ['Date', 'Destination']
    flights_num = ['Flight Number', 'Delay']


    def question_generator():
        question = random.randrange(4)
        data = [[0, bikes_cat, bikes_num, 'bikes', 'https://www.inferentialthinking.com/data/trip.csv'],
            [0, health_cat, health_num, 'health', 'https://www.inferentialthinking.com/data/ckd.csv'], 
            [0, nba_cat, nba_num, 'nba', 'https://www.inferentialthinking.com/data/nba2013.csv'], 
            [0, flights_cat, flights_num, 'flights', 'https://www.inferentialthinking.com/data/united_summer2015.csv']][random.randrange(4)]
        data[0] = pd.read_csv(data[4])
        cat = data[1][random.randrange(len(data[1]))]
        num = data[2][random.randrange(len(data[2]))]
        cat_2 = data[1][random.randrange(len(data[1]))]
        choices = list(data[0].value_counts(cat).index)
        choice = choices[random.randrange(len(choices))]
        while cat == cat_2:
            cat_2 = data[1][random.randrange(len(data[1]))]
        if question == 0: #table -> column -> item practice
            index = random.randrange(2)
            flip = ['highest', 'lowest'][index]
            order = [True, False][index]
            answer = f"{data[3]}.where('{cat}', '{choice}').sort('{num}', descending={order}).column('{cat_2}').item(0)"
            question = f"find the {cat_2} value where {cat} is {choice} and where {num} is the {flip}."
            return [question, answer, data[4], data[3]]
        elif question == 1: #.where practice
            index = random.randrange(4)
            flip = ['is below', 'is less than or equal to', 'is above', 'is greater than or equal to'][index]
            comp = ['are.below', 'are.below_or_equal_to', 'are.above', 'are.above_or_equal_to'][index]
            values = list(data[0][num])
            value = values[random.randrange(len(values))]
            answer = f"{data[3]}.where('{num}', {comp}({value})).num_rows/{data[3]}.num_rows"
            question =  f"find the proportion of values in the dataset where {num} {flip} {value}."
            return [question, answer, data[4], data[3]]
        elif question == 2: #.group practice
            cat_num = random.randrange(2)
            ind = random.randrange(2)
            flip = ['ascending', 'descending'][ind]
            order = [False, True][ind]
            index = random.randrange(5)
            collect = ['average', 'median', 'max', 'min', 'sum'][index]
            func = ['np.average', 'np.median', 'max', 'min', 'sum'][index]
            if cat_num == 0:
                answer = f"{data[3]}.group('{cat}', {func}).sort('{num} {collect}', descending={order}).select('{cat}')"
                question = f"create a table containing {cat} that is sorted in {flip} order by the {collect} of {num} for each unique {cat} value."
            elif cat_num == 1:
                answer = f"{data[3]}.group(['{cat}', '{cat_2}'], {func}).sort('{num} {collect}', descending={order}).select('{cat}', '{cat_2}')"
                question = f"create a table containing {cat} and {cat_2} that is sorted in {flip} order by the {collect} {num} for each pair of {cat} and {cat_2}."
            return [question, answer, data[4], data[3]]
        elif question == 3: #.pivot practice
            index = random.randrange(5)
            collect = ['average', 'median', 'maximum', 'minimum', 'sum'][index]
            func = ['np.average', 'np.median', 'max', 'min', 'sum'][index]
            answer = f"{data[3]}.pivot('{cat}', '{cat_2}', '{num}', {func})"
            question = f"create a table containing the {collect} of {num} for every unique combination of {cat} and {cat_2} with {cat} values being the columns and {cat_2} values as the rows."
            return [question, answer, data[4], data[3]]

    q_a = question_generator()
    question = q_a[0]
    answer = q_a[1]
    a = random.randint(100, 200)
    ans = "{0:b}".format(a)
    data["params"]["a"] = a
    data["params"]["question"] = question
    data["correct_answers"]["b"] = answer
    df = pd.read_csv(q_a[2]).head(5)
    data['params']['df'] = pl.to_json(df)
    data["params"]["tbl_name"] = q_a[3]
    return data
