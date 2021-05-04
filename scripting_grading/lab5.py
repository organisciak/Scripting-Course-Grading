from scripting_grading.grading import DataFrame_Answer, Answer
import pandas as pd

class L5_Q1_Answers(DataFrame_Answer):
    hash = 'd2f4eaa0c4acff0e3c60996577bcced8'
    
class L5_Q2_Answer(DataFrame_Answer):
    
    def check(self, ns=None):
        ans = self.get_resolved(self.q, ns)
        if int(ans.reset_index().iloc[:, -1].mean()) == 5262:
            pts = "max"
            err = ""
        else:
            pts = 0
            err = ""
        return pts, err
    
class L5_Q7_Answer(DataFrame_Answer):
    shape = ((9055, None), "max")
    
class L5_Q10_Answer(DataFrame_Answer):
    shape = ((207, None), "max")
    
class L5_Q11_Answer(DataFrame_Answer): 
    shape = ((9055, None), "max")
    
    def check(self, ns=None):
        try:
            ans = pd.read_csv('mean_rating.csv')
            return self._check_df(ans)
        except:
            return 0, ""

class L5_Q12_Answer(DataFrame_Answer): 
    shape = ((860, None), "max")
    
class L5_Q15_Answer(DataFrame_Answer): 
    shape = [((213, None), "max"), ((214, None), -2, "Set the header with  header=0, as in the slides.")]

class L5_Q16_Answer(DataFrame_Answer): 
    shape = [((15023, None), "max")]
    
key = dict(
    q1 = dict(entrytype='cell', pts=3, auto=True,
              answers=L5_Q1_Answers,
              question="Write the code to determine the median rating by each user."),
    q2 = dict(entrytype='cell', pts=3, auto=True,
              answers=L5_Q2_Answer,
              question="Using groupby, write the code to count how many ratings there are in each genre."),
    q3 = dict(entrytype='var', pts=3, auto=True,
              question="The previous question can be answered without groupby. How?",
              answers=["b) ratings['genres'].value_counts()"]),
    q4 = dict(entrytype='var', pts=4, auto=True,
               question="Which genre has the worst average ratings?",
               answers=[("a) Horror", "max", "Great work!"), 
                        ("d) Sci-Fi", "max", "If you take into account the average of the movie averages, rather than just all ratings, Horror is the more correct answer.")]),
    q5 = dict(entrytype='var', pts=3, auto=True, answers=[['Film-Noir', 'Musical', 'War']],
              question="Select the three most out-of-vogue film genres, by median release year."),
    q6 = dict(entrytype='var', pts=3, auto=True,
              answers=["c) The Secret Life of Pets"],
              question="Which post-2011 film has the most deviation among ratings?"),
    q7 = dict(entrytype='cell', pts=4, auto=True,
              question="Get all the unique combinations of title+year.",
              answers=L5_Q7_Answer),
    q8 = dict(entrytype='var', pts=3, auto=False,
              question="Run ratings['movie']. What does the error mean?"),
    q9 = dict(entrytype='var', pts=4, auto=False, 
              question="What does the error message mean?"),
    q10 = dict(entrytype='cell', pts=8, auto=True, answers=L5_Q10_Answer,
               question="Find all titles that refer to multiple movies released in different years."),
    q11 = dict(entrytype='cell', pts=5, auto=True, answers=L5_Q11_Answer,
               question="For the movie data: write the code to save a CSV of year/title/mean_rating"),
    q12 = dict(entrytype='cell', pts=7, auto=True, answers=L5_Q12_Answer,
               question="Retrieve information on patrons that are at least 18 years old as a DataFrame."),
    q13 = dict(entrytype='var', pts=5, auto=True, answers=['a) Thomasmouth'],
               question="For patrons over 18 years old, what is the most common home city"),
    q14 = dict(entrytype='cell', pts=10, auto=False,
               question="Write the code to determine the author with the most books checked out."),
    q15a = dict(entrytype='cell', pts=8, auto=True, answers=L5_Q15_Answer,
               question="Write the code to retrieve the list of songs recorded by the Beatles from Wikipedia."),
    q15b = dict(entrytype='var', pts=3, auto=True, answers=[3],
               question="How many songs by Carl Perkins did the Beatles record?"),
    q15c = dict(entrytype='var', pts=3, auto=True, answers=[1966],
               question="What was the median recording year?"),
    q15d = dict(entrytype='var', pts=4, auto=True, answers=['Starkey'],
               question="Which Beatle has the latest mean songwriting year?"),
    q16 = dict(entrytype='cell', pts=12, auto=True, answers=L5_Q16_Answer,
               question="Write the code to select all ratings by the 10 most prolific users."),
)