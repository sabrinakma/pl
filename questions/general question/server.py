import random, math
import pandas as pd
import numpy as np
import prairielearn as pl
import datascience
from datascience import Table

def generate(data):
    
    def question_generator():
        df = pd.read_csv('https://www.inferentialthinking.com/data/ckd.csv')
        cv = ['Sugar', 'Albumin', 'Blood Pressure', 'Age', 'Bacteria', 'Hypertension', 'Coronary Artery Disease', 'Pedal Edema', 'Anemia']
        nv = ['Specific Gravity', 'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 'White Blood Cell Count', 'Red Blood Cell Count']
        cat = cv[random.randrange(len(cv))]
        num = nv[random.randrange(len(nv))]
        q = random.randrange(3)
        index = random.randrange(5)
        collect = ['average', 'median', 'max', 'min', 'sum'][index]
        func = ['np.average', 'np.median', 'max', 'min', 'sum'][index]
        pd_func = ['mean', 'median', 'max', 'min', 'sum'][index]
        if q == 0: #.where
            value = round(np.mean(list(df.groupby(cat)[num].agg(pd_func))), 3)
            i = random.randrange(2)
            where_arg = ['are.above', 'are.below'][i]
            flip = ['above', 'below'][i]
            question = f"create a table containing only the values where the {collect} of {num} for each unique {cat} value is {flip} {value}."
            answer = f"health.group('{cat}', {func}).where('{num} {collect}', {where_arg}({value}))"
        elif q == 1: #.sort
            i = random.randrange(2)
            flip = ['ascending', 'descending'][i]
            boolean = ['False', 'True'][i]
            question = f"create a table that is sorted in {flip} order by the {collect} of {num} for each unique {cat} value."
            answer = f"health.group('{cat}', {func}).sort('{num} {collect}', descending={boolean})"
        elif q == 2: #.select
            i = random.randrange(4)
            num_col = range(1, 5)[i]
            nv_copy = nv[:]
            columns = []
            for i in range(num_col):
                columns.append(nv_copy.pop(random.randrange(len(nv_copy))))
            to_join = f', the {collect} of '
            question = f"create a {num_col + 1} column table containing {cat}, the {collect} of {to_join.join(columns)} respectively for each unique {cat} value."
            cols = ", ".join(f"'{col} {collect}'" for col in columns)
            answer = f"health.group('{cat}', {func}).select('{cat}', {cols})"
        return [question, answer, 'https://www.inferentialthinking.com/data/ckd.csv', 'health']

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
