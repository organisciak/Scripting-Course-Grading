from scripting_grading.grading import Answer, Series2DataFrame_Answer, DataFrame_Answer, Filters
import pandas as pd
import re

class L4_Q1_Answers(Series2DataFrame_Answer):
    output = {'index': ['Dumb and Dumber To', 'Alien 3', 'Moonraker', 'Shall We Dance', 'Top Gun', 'Quantum of Solace', 'Wild Hogs'], 'columns': [0], 'data': [[169837010], [159814498], [210308099], [170128460], [356830601], [586090727], [253625427]]}
    
class L4_Q3_Answers(Series2DataFrame_Answer):
    output = {'index': ['Top Gun', 'Quantum of Solace', 'Wild Hogs', 'Apollo 13', 'Cloudy with a Chance of Meatballs 2', 'Hook', "Bridget Jones's Diary", 'Les Miserables (2012)', 'Star Trek', 'Dances with Wolves', 'X-Men:First Class', 'My Big Fat Greek Wedding', 'Shark Tale'], 'columns': [0], 'data': [[356830601], [586090727], [253625427], [355237933], [274325949], [300854823], [281929795], [441809770], [385680446], [424208848], [353624124], [368744044], [367275019]]}
    
class L4_Q5_Answers(Answer):
    val_answers = 424208848
    
class L4_Q7_Answers(Series2DataFrame_Answer):
    def check(self, ns=None):
        ans = self.get_resolved(self.q, ns)
        return self._check_ans(ans)
    
    def _check_ans(self, ans):
        if (ans == ans.sort_values(ascending=False)).all():
            pts, comments = "max", ""
        elif (ans == ans.sort_values()).all():
            pts, comments = -2, "Sort is descending, not ascending order"
        else:
            pts, comments = 0, ""
        return pts, comments

class L4_Q8_Answers(DataFrame_Answer):
    output = {'index': [5, 6, 7, 8, 9], 'columns': ['manufacturer', 'model', 'displ', 'year', 'cyl', 'trans', 'drv', 'cty', 'hwy', 'fl', 'class'], 'data': [['audi', 'a4', 2.8, 1999, 6, 'manual(m5)', 'f', 18, 26, 'p', 'compact'], ['audi', 'a4', 3.1, 2008, 6, 'auto(av)', 'f', 18, 27, 'p', 'compact'], ['audi', 'a4 quattro', 1.8, 1999, 4, 'manual(m5)', '4', 18, 26, 'p', 'compact'], ['audi', 'a4 quattro', 1.8, 1999, 4, 'auto(l5)', '4', 16, 25, 'p', 'compact'], ['audi', 'a4 quattro', 2.0, 2008, 4, 'manual(m6)', '4', 20, 28, 'p', 'compact']]}

class L4_Q9_Answers(DataFrame_Answer):
    shape = ((41, 11), "max")

class L4_Q10_Answers(DataFrame_Answer):
    output = {'index': [15], 'columns': ['manufacturer', 'model', 'displ', 'year', 'cyl', 'trans', 'drv', 'cty', 'hwy', 'fl', 'class'], 'data': [['audi', 'a6 quattro', 2.8, 1999, 6, 'auto(l5)', '4', 15, 24, 'p', 'midsize']]}

class L4_Q12_Answers(DataFrame_Answer):
    hash = 'dc1020ed5bf46560105b74efceea80e0'
    
class L4_Q15_Answers(DataFrame_Answer):
    placeholder = True

key = dict(
    q1 = dict(entrytype='cell', pts=3, auto=True, answers=L4_Q1_Answers,
              question="Write the code to return the first 7 rows of `bodf`"),
    q2 = dict(entrytype='var', pts=3, auto=True, answers=['254060295'],
              question="What is the average box office take in this sample of films, to the nearest dollar?"),
    q3 = dict(entrytype='cell', pts=3, auto=True, answers=L4_Q3_Answers,
              question="Write the code to return just the movies that have made more than $250m."),
    q4 = dict(entrytype='var', pts=3, auto=False, question="What does bodf.cumsum() do?"),
    q5 = dict(entrytype='cell', pts=3, auto=True, answers=L4_Q5_Answers,
              question="How would you return the Box Office take for Dances with Wolves?"),
    q6 = dict(entrytype='var', pts=3, auto=True, answers=["ORDER BY"],
              question="What SQL clause is comparable to bodf.sort_values()?"),
    q7 = dict(entrytype='cell', pts=3, auto=True, answers=L4_Q7_Answers,
              question="How would you sort bodf in descending order?"),
    q8 = dict(entrytype='cell', pts=3, auto=True, answers=L4_Q8_Answers,
              question="What is the code to select rows 5 to 10 of mpg?"),
    q9 = dict(entrytype='cell', pts=4, auto=True, answers=L4_Q9_Answers,
              question="How would you select all rows with a class of 'midsize'?"),
    q10 = dict(entrytype='cell', pts=4, auto=True, answers=L4_Q10_Answers,
              question="How would you select all rows with a class of 'midsize' and hwy economy of 24 miles per gallon?"),
    q11 = dict(entrytype='var', pts=4, auto=True, answers=['20.1'],
              question="What is the average city fuel economy for compact cars?"),
    q12 = dict(entrytype='cell', pts=6, auto=True, answers=L4_Q12_Answers,
              question="Convert the SQL to the equivalent in Pandas."),
    q13 = dict(entrytype='var', pts=6, auto=True, answers=['Volkswagen New Beetle'],
              question="Which car had the best city fuel economy in 1999?"),
    q14 = dict(entrytype='var', pts=6, auto=True, answers=[8],
              question="How many cars have a highway economy that's more than 10 MPG better on highways than in cities?"),
    q15a = dict(entrytype='var', pts=4, auto=False, question="Describe how: Get the number of cars from each manufacturer."),
    q15b = dict(entrytype='var', pts=4, auto=False, question="Describe how: Figure out how cylinders affect fuel economy."),
    q16a = dict(entrytype='var', pts=1, auto=True, answers=["pd.read_csv()"], question="Method"),
    q16b = dict(entrytype='var', pts=1, auto=True, answers=['3.1415'], question="Float"),
    q16c = dict(entrytype='var', pts=1, auto=True, answers=["Python"], question="Programming Language"),
    q16d = dict(entrytype='var', pts=1, auto=True, answers=["SELECT * FROM heights;"], question="SQL Statement"),
    q16e = dict(entrytype='var', pts=1, auto=True, answers=[">"], question="Logical Operator"),
    q16f = dict(entrytype='var', pts=1, auto=True, answers=["[1, 2, 3]"], question="List"),
    q16g = dict(entrytype='var', pts=1, auto=True, answers=["sep=' ', as in print(\"hello world\", sep=' ')"], question="Named Argument"),
    q16h = dict(entrytype='var', pts=1, auto=True, answers=["42"], question="Integer"),
    q16i = dict(entrytype='var', pts=1, auto=True, answers=["WHERE"], question="SQL Clause"),
    q16j = dict(entrytype='var', pts=1, auto=True, answers=["_"], question="LIKE wildcard"),
    q16k = dict(entrytype='var', pts=1, auto=True, answers=["SQLite"], question="DBMS"),
    q16l = dict(entrytype='var', pts=1, auto=True, answers=["print()"], question="Function"),
    q16m = dict(entrytype='var', pts=1, auto=True, answers=["Pandas"], question="Library"),
)