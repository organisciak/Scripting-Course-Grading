import json
import nbformat
import re
import sys
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import clear_output
import types
import time
import re
import pandas as pd
import logging
import hashlib

class LabNotebook():    
    def __init__(self, path):
        self.path = path
        self.nb = nbformat.read(path, 4)
        self._code_answers = None
        
        self.mod = types.ModuleType(self.path)
        self.mod.__file__ = self.path
        self.mod.__loader__ = self
        self.mod.__dict__['get_ipython'] = get_ipython
        
        self.shell = InteractiveShell(user_module=self.mod).instance()
        self.shell.prepare_user_module(self.mod)
        
        # For saving the last line outputof iPython cells
        self.cell_outs = dict()
            
    def code_cells(self):
        for cell in self.nb.cells:
            if cell.cell_type != 'markdown':
                yield cell

    def code_answers(self):
        if self._code_answers is None:
            code_answers = {}
            for cell in self.code_cells():
                matches = re.findall('Answer-(Q[\d\w]+)', cell.source, flags=re.IGNORECASE)
                if len(matches) > 0:
                    q= matches[0].lower()
                    try:
                        assert len(matches) == 1
                        assert q not in code_answers
                    except:
                        logging.warn("{} cell shows up more that once".format(q))
                    code_answers[q] = self.strip_comments(cell.source)
            self._code_answers = code_answers
        return self._code_answers
    
    def strip_comments(self, source):
        return re.sub("^ *#.*$", '', source, flags=re.MULTILINE)
    
    def run_as_module(self):

        #sys.modules[fullname] = mod

        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        ns = self.save_ns()
        try:
            for cell in self.code_cells():
                self.run_string_cell_in_module(cell.source, save_ns=False)
        finally:
            # If anything crashes, need to fix the namespace
            self.restore_ns(ns)
        return self.mod
    
    def run_string_cell_in_module(self, source, name=None, save_ns=True, silent=False):
        if name is None:
            matches = re.findall('Answer-(Q[\d\w]+)', source, flags=re.IGNORECASE)
            if len(matches) > 0:
                name = matches[0].lower() + '_resolved'
                
        if save_ns:
            ns = self.save_ns()
        try:
            if 'grade check' in source.lower():
                return
            comments_stripped = self.strip_comments(source)
            #transformed = self.shell.input_transformer_manager.transform_cell(comments_stripped)
            out = self.shell.run_cell(comments_stripped, silent=silent)
            
            #exec(transformed, self.mod.__dict__)
            if name:
                self.mod.__dict__[name] = out.result
            
        finally:
            pass
            if save_ns:
                self.restore_ns(ns)
        #return out
                
    def get_var_answer(self, q):
        ans, err = None, None
        qname = q + '_answer'
        if not hasattr(self.mod, qname):
            err = "Can't find the answer"
        
        ans = getattr(self.mod, qname)
        if type(ans) is str:
            ans = ans.strip()
            if ans == "":
                err = "Answer is empty."
        
        return ans, err
    
    def get_cell_answer(self, q):
        ans, err = None, None
        if q not in self.code_answers():
            err = "Can't find the cell with the answer. Did you include # Answer-{} at the top?".format(q.upper())
        else:
            ans = self.code_answers()[q]
        return ans, err
        
    def run_method(self, method, **kwargs):
        return method(**kwargs)
        
    def save_ns(self):
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = self.mod.__dict__
        return save_user_ns
        
    def restore_ns(self, save_user_ns):
        self.shell.user_ns = save_user_ns
        
    def _handgrade(self, q, ans, max_pts, last_pts=None, last_comment=None, debug=False,
                   question_text=None):
        if debug:
            return max_pts, "DEBUGGING"
        clear_output()
        print(q.center(100, '-'))
        if question_text:
            print("Q:", question_text, "\n--")
        print(ans)
        while True:
            time.sleep(.5)
            msg = "How many points, out of {}? (default is {}, can subtract from max with -x)".format(max_pts, "max" if last_pts is None else last_pts)
            pts = input(msg)
            if pts.strip() == "":
                pts = "max" if not last_pts else last_pts
            if pts in ["max"] or pts.strip('-').replace('.','').isdigit():
                break
            else:
                time.sleep(1)
                last_comment = pts # Assume an accidental comment
                print('Looks like a bad input for pts, try again.')
        
        msg = "Any comments?"
        if last_comment:
            msg += "PREVIOUS COMMENT (will stay if empty, use single hyphen to wipe):" +  last_comment
        time.sleep(.5)
        comments = input(msg)
        time.sleep(.5)
        comments = comments.strip()
        if comments == "" and last_comment:
            comments = last_comment
        elif comments == "-":
            comments = ""
        return pts, comments
        
    def autograde_var_answer(self, q, ans, correct_answers, filters=[]):
        pts, comments = None, ""
        filtered_ans = self.run_filters(ans, filters)
        comment_for_answer = ""
        
        for correct in correct_answers:
            if type(correct) is tuple:
                if len(correct) == 2:
                    correct, pts_for_answer = correct
                elif len(correct) == 3:
                    correct, pts_for_answer, comment_for_answer = correct
                else:
                    raise Exception("unexpected length for tuple answer")
            else:
                pts_for_answer = "max"

            correct = self.run_filters(correct, filters)
            if filtered_ans == correct:
                pts = pts_for_answer
                comments = comment_for_answer
                break
            pts = 0

        if pts == 0:
            comments += "Your answer: {}".format(ans)
            comments += "\nExample of correct answer is:\n{}".format(correct_answers[0])
        
        return pts, comments
        
    def run_filters(self, ans, filters):
        for filter in filters:
            if callable(filter):
                ans = filter(ans)
            elif hasattr(Filters, filter):
                ans = getattr(Filters, filter)(ans)
            else:
                print(filter)
                raise Exception("unknown filter")
        return ans
    
    def grade_answer(self, q, params, prev_grade=None, debug=False):
        if prev_grade is None:
            grade = dict(pts=None, max_pts=params['pts'], comments="", question=None)
        else:
            # Regrading
            grade = prev_grade
        if 'question' in params:
            grade['question'] = params['question']
        
        if params['entrytype'] == 'cell':
            ans, err = self.get_cell_answer(q)
        elif params['entrytype'] == 'var':
            ans, err = self.get_var_answer(q)
        if err:
            grade['comments'] += err
            return grade
        
        if prev_grade:
            # Forces auto-grading
            pts, comments = self._handgrade(q, ans, grade['max_pts'], 
                                      last_pts=grade['pts'],
                                      last_comment=grade['comments'],
                                      debug=debug, question_text=grade['question'])
            
        elif params['auto'] & (params['entrytype'] == 'var'):
            try:
                filters =params['filters'] if 'filters' in params else []
                pts, comments = self.autograde_var_answer(q, ans, 
                                                          params['answers'], 
                                                          filters=filters)
            except:
                if debug:
                    raise
                pts = 0
                comments = ""
        elif params['auto'] & (params['entrytype'] == 'cell'):
            try:
                pts, comments = self.autograde_cell_answer(q, ans, params['answers'])
            except:
                if debug:
                    raise
                pts = 0
                comments = ""
        elif not params['auto']:
            pts, comments = self._handgrade(q, ans, grade['max_pts'], debug=debug,
                                            question_text=grade['question'])
        if pts == 'max':
            pts = grade['max_pts']
        else:
            pts = float(pts)
            if pts < 0:
                pts = grade['max_pts'] + pts

        grade['pts'] = pts
        grade['comments'] = comments
            
        return grade
        
    def autograde_cell_answer(self, q, ans, answer_func):
        pts, comments = self._grade_cell_answer_class(ans, answer_func, q=q)
        if pts is None:
            pts = 'max'
        if comments is None:
            comments = ""
        return pts, comments
        
    def _grade_cell_answer_class(self, answer, answer_class, q=None):
        checker = answer_class(q)
        self.run_method(checker.prep)
        self.run_string_cell_in_module(answer)
        pts, errs = self.run_method(checker.check, ns=self.mod)
        return pts, errs
    
    def grade_all(self, answerkey, with_hand_doublecheck=True, hand_regrade=False, debug=False):
        grades = dict()
        try:
            for q, params in answerkey.items():
                grade = self.grade_answer(q, params, debug=debug)   
                grades[q] = grade

            if hand_regrade and not debug:
                ''' Regrade wrong answers manually'''
                new_grades = dict()
                for q, params in answerkey.items():
                    grade = grades[q] 
                    if ((grade['pts'] == 0) or (grade['pts'] is None)) and (params['auto']):
                        grade = self.grade_answer(q, params, prev_grade=grade)
                    new_grades[q] = grade
                return new_grades
            else:
                return grades
        except:
            raise
            # return incomplete grades
            return grades
    

class LabGrading():
    
    def __init__(self):
        pass

class Filters():
    
    def norm_string(ans):
        ''' Lowercase, strip whitespace and only use single quotes'''
        return ans.strip().strip(';').lower().replace('"', "'").replace('  ', ' ')
        
    def sql_where_clean(ans):
        b = Filters.norm_string(ans)
        c = re.sub('\s*(==|=|>|<|>=|<=)\s*', r'\1', b)
        parts = re.split('\s+and\s+', c)
        sorted_parts = sorted(parts)
        return " and ".join(sorted_parts)
    
    def sql_just_like_comparison(ans):
        ''' Strip full SQL statement down to just `like` comparison '''
        a = Filters.norm_string(ans)
        return re.sub(".* like +'(.*?)'", r"\1", a)


class Answer():
    
    def __init__(self, q=None):
        self.q = q
        
    def prep(self):
        pass
    
    def check(self, ns=None):
        ans = self.get_resolved(self.q, ns)
        pts, comments = 0, ""
        # Basic comparison
        if hasattr(self, 'val_answers') and self.val_answers:
            if type(self.val_answers) is not list:
                self.val_answers = [self.val_answers]
            for val_answer in self.val_answers:
                if type(val_answer) is tuple and len(val_answer) == 2:
                    val_answer, possible_pts = val_answer
                elif type(val_answer) is tuple and len(val_answer) == 3:
                    val_answer, possible_pts, possible_comments = val_answer
                else:
                    possible_pts, possible_comments = "max", ""
                    
                if val_answer == ans:
                    pts, comments = possible_pts, possible_comments
                    break
                
        return pts, comments
    
    def compare_dfs(self, submitted, real):
        if submitted.shape[0] != real.shape[0]:
            return 0, "Different number of rows than expected."
        elif submitted.shape[1] != real.shape[1]:
            return 0, "Different number of columns than expected."
        
        compare = (submitted == real)
        total_cells = compare.shape[0] * compare.shape[1]
        matched_cells = compare.sum().sum()
        if matched_cells == total_cells:
            pts = "max"
        else:
            pts = matched_cells / total_cells
            # Round to nearest half
            pts = int(pts * 2)/2
        return pts, ""
    
    def get_resolved(self, q, ns=None):
        qname = q + '_resolved'
        return getattr(ns, qname)

class DataFrame_Answer(Answer):
    output = None
    
    # A tuple with the correct shape of the output,
    # or a list of (shape_tuple, pts, comment) tuples
    # If a side of shape doesn't matter, use None, i.e. (2, None)
    shape = None 
    
    def check(self, ns=None):
        ans = self.get_resolved(self.q, ns)
        return self._check_df(ans)
        
    def _check_df(self, ans):
        if hasattr(self, 'hash') and self.hash:
            import hashlib
            ans_hash = hashlib.md5(ans.to_json().encode()).hexdigest()
            if self.hash == ans_hash:
                pts = "max"
                err = ""
            else:
                pts = 0
                err = "hash mismatch"
            
        if hasattr(self, 'output') and self.output:
            key_df = self._parse_output()
            pts, err = self.compare_dfs(ans, key_df)
            return pts, err
        
        if hasattr(self, 'shape') and self.shape:
            if type(self.shape) is not list:
                pts, err = self.compare_shapes(ans, *self.shape)
            else:
                for option in self.shape:
                    pts, err = self.compare_shapes(ans, *option)
                    if pts != 0:
                        break
                
        return pts, err
    
    def _parse_output(self):
        if list(self.output.keys()) == ['index', 'columns', 'data']:
            ''' This style was saved with df.to_dict(orient='split'), and is the 
            least lossy.
            '''
            df = pd.DataFrame(**self.output)
        else:
            df = pd.DataFrame(self.output)
        return df
    
    def show_output(self):
        if self.output:
            return self._parse_output()
                
    def compare_shapes(self, ans, expected_shape, pts="max", comment=None):
        l, w = expected_shape
        if l is None and w == ans.shape[1]:
            pts = pts
        elif w is None and l == ans.shape[0]:
            pts = pts
        elif (l, w) == ans.shape:
            pts = pts
        else:
            pts = 0
        return pts, comment
    
class SQL2DataFrame_Answer(DataFrame_Answer):
    def check(self, ns=None):
        ans = self.get_resolved(self.q, ns).DataFrame()
        return self._check_df(ans)
    
class Series2DataFrame_Answer(DataFrame_Answer):
    def check(self, ns=None):
        ans = self.get_resolved(self.q, ns).to_frame()
        return self._check_df(ans)
    
    def show_output(self):
        if self.output:
            out = self._parse_output().iloc[:, 0]
            out.name = None
            return out

def print_grade_report(grades, name=None):
    if name:
        print("name: {}".format(name))
    pts = [g['pts'] for g in grades.values() if g['pts']]
    print("Total: {}\n-----".format(sum(pts)))
    for q, grade in grades.items():
        if 'question' in grade:
            print("\n# {}: {}\n{}/{}".format(q.upper(), grade['question'], 
                                             grade['pts'], grade['max_pts']))
        else:
            print("\n# {}: {}/{}".format(q.upper(), grade['pts'], grade['max_pts']))
        if grade['comments'].strip() != "":
            print(' Comments: ' + grade['comments'])