import random, math
import pandas as pd
import numpy as np
import prairielearn as pl
# import datascience
# from datascience import Table

### To author, only edit this portion ###
authoring = False #TYPE: BOOL. change to True!

# For the columns you want to be included in the question:
change_columns = False #TYPE: BOOL. Change to True if you wish to use your own columns instead of random selection.

#   One has to be the categorical column (cat)
#cv options = ['Sugar', 'Albumin', 'Blood Pressure', 'Age', 'Bacteria', 'Hypertension', 'Coronary Artery Disease', 'Pedal Edema', 'Anemia']
categorical = '' #TYPE: STRING, must use quotations

#   One has to be the numerical column (nv)
#nv options = ['Specific Gravity', 'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 'White Blood Cell Count', 'Red Blood Cell Count']
numerical = '' #TYPE: STRING, must use quotations

# For the first .group function:
group_by = 'average' #TYPE: STRING. Change to: "average", "max", OR "min". MUST have single quotations!

# For the second function
function = 'sort' # TYPE: STRING. change to "sort", "select", OR "where". MUST have single quotations!

# For sort (leave as is if not applicable):
descending_true = False #TYPE: BOOL. change to True (descending) or False (ascending)

# For where (leave as is if not applicable):
are_above = False #TYPE: BOOL. change to True (are.above) or False (are.below)

# For select (leave as is if not applicable):
column = None #TYPE: STRING. change to the column you want selected as part of the .select call.

### End portion ###

def generate(data):
    
    def question_generator():
        df = pd.read_csv('https://www.inferentialthinking.com/data/ckd.csv')
        cv = ['Sugar', 'Albumin', 'Blood Pressure', 'Age', 'Bacteria', 'Hypertension', 'Coronary Artery Disease', 'Pedal Edema', 'Anemia']
        nv = ['Specific Gravity', 'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 'White Blood Cell Count', 'Red Blood Cell Count']
        cat = cv[random.randrange(len(cv))]
        num = nv[random.randrange(len(nv))]
        q = random.randrange(3)
        index = random.randrange(3)
        collect = ['average', 'max', 'min'][index]
        func = ['np.average', 'max', 'min'][index]
        pd_func = ['mean', 'max', 'min'][index]
        number = 0 
        if q == 0: #.where
            value = round(np.mean(list(df.groupby(cat)[num].agg(pd_func))), 3)
            i = random.randrange(2)
            where_arg = ['are.above', 'are.below'][i]
            flip = ['above', 'below'][i]
            number = value
            question = f"create a table containing only the values where the {collect} of {num} for each unique {cat} value is {flip} {value}."
            answer = f"health.group('{cat}', {func}).where('{num} {collect}', {where_arg}({value}))"
        elif q == 1: #.sort
            i = random.randrange(2)
            flip = ['ascending', 'descending'][i]
            boolean = ['False', 'True'][i]
            question = f"create a table that is sorted in {flip} order by the {collect} of {num} for each unique {cat} value."
            answer = f"health.group('{cat}', {func}).sort('{num} {collect}', descending={boolean})"
        elif q == 2: #.select
            col = nv[random.randrange(len(nv))]
            question = f"create a 2 column table containing {cat} and {col} {collect} respectively for each unique {cat} value."
            answer = f"health.group('{cat}', {func}).select('{cat}', '{col} {collect}')"
        return [question, answer, 'https://www.inferentialthinking.com/data/ckd.csv', 'health', number]

    def authoring_question():
        df = pd.read_csv('https://www.inferentialthinking.com/data/ckd.csv')
        
        if not change_columns: #columns are randomly selected
            cv = ['Sugar', 'Albumin', 'Blood Pressure', 'Age', 'Bacteria', 'Hypertension', 'Coronary Artery Disease', 'Pedal Edema', 'Anemia']
            nv = ['Specific Gravity', 'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 'White Blood Cell Count', 'Red Blood Cell Count']
            cat = cv[random.randrange(len(cv))]
            num = nv[random.randrange(len(nv))]
        else:
            cat = categorical
            num = numerical
            
        number = 0
        collect = group_by.lower()
        pd_func = group_by.lower()
        func = group_by.lower()
        
        if pd_func == 'average': #change to correct word
            pd_func = 'mean'
        if func == 'average': #change to correct word
            func = 'np.average'
        
        if function.lower() == 'where':
            value = round(np.mean(list(df.groupby(cat)[num].agg(pd_func))), 3)
            flip = 'above'
            where_arg = 'are.above'
            if not are_above: #are_above:
                flip = 'below'
                where_arg = 'are.below'
            number = value
            question = f"create a table containing only the values where the {collect} of {num} for each unique {cat} value is {flip} {value}."
            answer = f"health.group('{cat}', {func}).where('{num} {collect}', {where_arg}({value}))"
            
        elif function.lower() == 'sort':
            flip = 'descending'
            boolean = 'True'
            if not descending_true: #desc = false
                flip = 'ascending'
                boolean = 'False'
            question = f"create a table that is sorted in {flip} order by the {collect} of {num} for each unique {cat} value."
            answer = f"health.group('{cat}', {func}).sort('{num} {collect}', descending={boolean})"
            
        elif function.lower() == 'select':
            if not column:
                col = nv[random.randrange(len(nv))]
            else:
                col = column
            question = f"create a 2 column table containing {cat} and {col} {collect} respectively for each unique {cat} value."
            answer = f"health.group('{cat}', {func}).select('{cat}', '{col} {collect}')"
            
        return [question, answer, 'https://www.inferentialthinking.com/data/ckd.csv', 'health', number]


    if not authoring: #this is the implemented pseudorandom question generator.
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
        data["params"]["number"] = q_a[4]
        return data
    
    elif authoring:
        q_a = authoring_question()
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
        data["params"]["number"] = q_a[4]
        return data
        
        




"""
# import random, math
# import pandas as pd
# import prairielearn as pl
# import datascience
# from datascience import Table

# def generate(data):
    
#     bikes_cat = ['Start Station', 'End Station', 'Subscriber Type']
#     bikes_num = ['Start Terminal', 'End Terminal', 'Duration', 'Bike #']

#     health_cat = ['Red Blood Cells', 'Pus Cell', 'Pus Cell clumps', 'Bacteria', 'Hypertension', 'Diabetes Mellitus', 'Coronary Artery Disease', 'Appetite', 'Pedal Edema', 'Anemia']
#     health_num = ['Age', 'Blood Pressure', 'Specific Gravity', 'Albumin', 'Sugar', 'Blood Glucose Random', 'Blood Urea', 'Serum Creatinine', 'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 'White Blood Cell Count', 'Red Blood Cell Count']

#     nba_cat = ['Name', 'Position']
#     nba_num = ['Height', 'Weight', 'Age in 2013']

#     flights_cat = ['Date', 'Destination']
#     flights_num = ['Flight Number', 'Delay']


#     def question_generator():
#         question = random.randrange(4)
#         data = [[0, bikes_cat, bikes_num, 'bikes', 'https://www.inferentialthinking.com/data/trip.csv'],
#             [0, health_cat, health_num, 'health', 'https://www.inferentialthinking.com/data/ckd.csv'], 
#             [0, nba_cat, nba_num, 'nba', 'https://www.inferentialthinking.com/data/nba2013.csv'], 
#             [0, flights_cat, flights_num, 'flights', 'https://www.inferentialthinking.com/data/united_summer2015.csv']][random.randrange(4)]
#         data[0] = pd.read_csv(data[4])
#         cat = data[1][random.randrange(len(data[1]))]
#         num = data[2][random.randrange(len(data[2]))]
#         cat_2 = data[1][random.randrange(len(data[1]))]
#         choices = list(data[0].value_counts(cat).index)
#         choice = choices[random.randrange(len(choices))]
#         while cat == cat_2:
#             cat_2 = data[1][random.randrange(len(data[1]))]
#         if question == 0: #table -> column -> item practice
#             index = random.randrange(2)
#             flip = ['highest', 'lowest'][index]
#             order = [True, False][index]
#             answer = f"{data[3]}.where('{cat}', '{choice}').sort('{num}', descending={order}).column('{cat_2}').item(0)"
#             question = f"find the {cat_2} value where {cat} is {choice} and where {num} is the {flip}."
#             return [question, answer, data[4], data[3]]
#         elif question == 1: #.where practice
#             index = random.randrange(4)
#             flip = ['is below', 'is less than or equal to', 'is above', 'is greater than or equal to'][index]
#             comp = ['are.below', 'are.below_or_equal_to', 'are.above', 'are.above_or_equal_to'][index]
#             values = list(data[0][num])
#             value = values[random.randrange(len(values))]
#             answer = f"{data[3]}.where('{num}', {comp}({value})).num_rows/{data[3]}.num_rows"
#             question =  f"find the proportion of values in the dataset where {num} {flip} {value}."
#             return [question, answer, data[4], data[3]]
#         elif question == 2: #.group practice
#             cat_num = random.randrange(2)
#             ind = random.randrange(2)
#             flip = ['ascending', 'descending'][ind]
#             order = [False, True][ind]
#             index = random.randrange(5)
#             collect = ['average', 'median', 'max', 'min', 'sum'][index]
#             func = ['np.average', 'np.median', 'max', 'min', 'sum'][index]
#             if cat_num == 0:
#                 answer = f"{data[3]}.group('{cat}', {func}).sort('{num} {collect}', descending={order}).select('{cat}')"
#                 question = f"create a table containing {cat} that is sorted in {flip} order by the {collect} of {num} for each unique {cat} value."
#             elif cat_num == 1:
#                 answer = f"{data[3]}.group(['{cat}', '{cat_2}'], {func}).sort('{num} {collect}', descending={order}).select('{cat}', '{cat_2}')"
#                 question = f"create a table containing {cat} and {cat_2} that is sorted in {flip} order by the {collect} {num} for each pair of {cat} and {cat_2}."
#             return [question, answer, data[4], data[3]]
#         elif question == 3: #.pivot practice
#             index = random.randrange(5)
#             collect = ['average', 'median', 'maximum', 'minimum', 'sum'][index]
#             func = ['np.average', 'np.median', 'max', 'min', 'sum'][index]
#             answer = f"{data[3]}.pivot('{cat}', '{cat_2}', '{num}', {func})"
#             question = f"create a table containing the {collect} of {num} for every unique combination of {cat} and {cat_2} with {cat} values being the columns and {cat_2} values as the rows."
#             return [question, answer, data[4], data[3]]

#     q_a = question_generator()
#     question = q_a[0]
#     answer = q_a[1]
#     a = random.randint(100, 200)
#     ans = "{0:b}".format(a)
#     data["params"]["a"] = a
#     data["params"]["question"] = question
#     data["correct_answers"]["b"] = answer
#     df = pd.read_csv(q_a[2]).head(5)
#     data['params']['df'] = pl.to_json(df)
#     data["params"]["tbl_name"] = q_a[3]
#     return data
"""