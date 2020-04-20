from scripting_grading.grading import Answer

class L2_Q1_Answers(Answer):
    
    def prep(self):
        get_ipython().run_line_magic('reload_ext', 'sql')
        get_ipython().run_line_magic('sql', 'sqlite://')
        get_ipython().run_line_magic('sql', 'DROP TABLE IF EXISTS worker_wages')
        get_ipython().run_line_magic('sql', 'CREATE TABLE worker_wages (role, num_workers, wage);')
        get_ipython().run_line_magic('sql', 'INSERT INTO worker_wages ("test", 12, 34);')
        
    def check(self, ns=None):
        pts, errs = None, None
        sqlresults = get_ipython().run_line_magic('sql', 'SELECT * FROM worker_wages')
        df = sqlresults.DataFrame()
        for role, num_workers, wage in [('Drawer',  375, 328.98), ('Warehouseman', 1586, 308.73)]:
            subset = df[df.role == role]
            
            if not subset.shape[0] > 0:
                pts, errs = 0, "I don't see '{}' in the data.".format(role)
            
            elif not subset.shape[0] == 1:
                errs = '''I see '{}' more than once. Did you add the
                data more than once? (This doesn't affect this question - you probably did
                it right, but ran it twice, which is something to look out for. Try
                dropping the table and creating it anew).'''.format(role)
                
            elif not subset.iloc[-1].num_workers == num_workers:
                pts, errs = "Num workers doesn't seem right for {}".format(role)
                
            elif not subset.iloc[-1].wage == wage:
                pts, errs = "Num workers doesn't seem right for {}".format(role)
        return pts, errs
    

class L2_Q3_Answers(Answer):
    def prep(self):
        get_ipython().run_line_magic('sql', 'DROP TABLE IF EXISTS heights')
        
    def check(self, ns=None):
        pts, errs = None, None
        sqlresults = get_ipython().run_line_magic('sql', 'PRAGMA table_info(heights)')
        df = sqlresults.DataFrame()[['name', 'type']].sort_values('name')
        
        headers = ['height', 'repht', 'repwt', 'sex', 'weight']
        types = ['INTEGER', 'INTEGER', 'INTEGER', 'TEXT', 'INTEGER']
        count = (df['name'] == headers).sum()
        count += (df['type'] == types).sum()
        if count == 10:
            pts = 'max'
        else:
            pts = (count-10)/2
            errs = "Headers should be {} and types should be {}".format(headers, types)
            errs += "\nYour table created\n{}".format(df.to_string())
        return pts, errs
    
class L2_Q7_Answers(Answer):
    def check(self, ns=None):
        x = ns.x
        if x == 0:
            pts = 0
            err = "The final value of x is 0. You didn't add anything to it!"
        elif x == 21:
            pts = -2
            err = "The final value of x is 21 (the last number) - that means you're not adding to x each loop."
        elif type(x) is not int:
            pts = 0
            err = "x should be a number, but your response is type: {}".format(type(x))
        elif x != 54:
            pts = 0
            err = "x should be 54, you have {}".format(x)
        else:
            pts = "max"
            err = ""
        return pts, err
    
class L2_Q13_Answers(Answer):
    def check(self, ns=None):
        pts, err = None, None
        ans = ns.q13_resolved

        if ans == "====HEADING====":
            pts = "max"
        elif ans.strip('=') == "HEADING":
            pts = -1
            err = 'Close. Try "HEADING".center(15, "=") (or set "HEADING" to a variable first)'
        else:
            pts = 0
            err = 'Try "HEADING".center(15, "=") (or set "HEADING" to a variable first)'
        return pts, err
    
key = dict(
    q1 = dict(entrytype='cell', pts=5, auto=True, answers=L2_Q1_Answers),
    q2 = dict(entrytype='var', pts=5, auto=False),
    q3 = dict(entrytype='cell', pts=5, auto=True, answers=L2_Q3_Answers),
    q4a = dict(entrytype='var', pts=5, auto=True,
               answers=["sex == 'M' AND repht > 100"],
               filters=['sql_where_clean']
              ),
    q4b = dict(entrytype='var', pts=5, auto=True,
               answers=['height < repht', 'repht > height'],
               filters=['sql_where_clean']
              ),
    q4c = dict(entrytype='var', pts=10, auto=True,
               answers=['sex == "F" AND height < repht AND weight < repwt', 
                        'sex == "F" AND repht > height AND weight < repwt', 
                        'sex == "F" AND height < repht AND repwt > weight', 
                        'sex == "F" AND repht > height AND repwt > weight'],
               filters=['sql_where_clean']
              ),
    q5 = dict(entrytype='var', pts=5, auto=False),
    q6 = dict(entrytype='cell', pts=5, auto=False),
    q7 = dict(entrytype='cell', pts=5, auto=True, answers=L2_Q7_Answers),
    # TODO future iteration - 8a question is confusing because of the space
    # For now allowing both answer
    q8a = dict(entrytype='var', pts=4, auto=True, answers=['False', 'True']),
    q8b = dict(entrytype='var', pts=4, auto=True, answers=['True']),
    q8c = dict(entrytype='var', pts=4, auto=True, answers=['True']),
    # TODO clarify language of 'equivalence'
    q9a = dict(entrytype='var', pts=4, auto=True, answers=['No']),
    q9b = dict(entrytype='var', pts=4, auto=True, answers=['Yes']),
    # TODO future iteration, lower pts here, add them to q7 instead
    q10 = dict(entrytype='var', pts=8, auto=False),
    # TODO future iteration, lower pts here
    q11 = dict(entrytype='var', pts=7, auto=True, answers=['False']),
    q12 = dict(entrytype='var', pts=5, auto=True, answers=[
        "all characters in S are alphabetic and there is at least one character in S"
    ]),
    q13 = dict(entrytype='cell', pts=10, auto=True, answers=L2_Q13_Answers),
)