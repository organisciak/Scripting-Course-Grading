from scripting_grading.grading import Answer, SQL2DataFrame_Answer, DataFrame_Answer, Filters
import pandas as pd
import re

class L3_Q1_Answers(SQL2DataFrame_Answer):
    # To save as this format:
    #   records = %sql SELECT * FROM books WHERE author LIKE "Tim %" OR author LIKE "Tom %"
    #   records.DataFrame().to_dict(orient='list')
    output = {'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'title': ['Sun Tzu: Art Of War', 'The Way and Its Power: A Study of the Tao T? Ching and Its Place in Chinese Thought', 'En Attendant Godot', 'They Came to Baghdad', 'Гарри Поттер и философский камень (Harry Potter, #1)', "Slaughterhouse Five, or The Children's Crusade", 'Dr Jekyll and Mr Hyde', 'The Devil Wears Prada', 'Nineteen Eighty-Four', 'The Hobbit or There and Back Again'], 'author': ['Sun Tzu', 'Arth Estate the', 'Samuel Beckett', 'Agatha Christie', 'J.K. Rowling', 'Kurt Vonnegut Jr.', 'Robert Louis Stevenson', 'Lauren Weisberger', 'George Orwell', 'J.R.R. Tolkien'], 'isbn': ['0-433-19939-3', '0-213-70445-5', '1-75624-696-3', '0-272-39105-0', '0-13-839638-8', '0-307-53448-0', '0-625-41598-1', '0-386-71659-5', '0-401-69650-2', '1-160-78240-7']}


class L3_Q2_Answers(SQL2DataFrame_Answer):
    output = {'id': [78, 89, 152, 221, 232, 238, 302, 339, 341, 385, 486, 516, 519, 526, 572, 638, 799, 856, 892, 911, 989], 'name': ['Jennifer Martin', 'Jennifer Bradley', 'Jessica Ramirez', 'David Hammond DDS', 'Kelly Blackburn', 'Christopher James', 'Hannah Simon', 'Sandra Tapia', 'Derek Carson', 'Shannon Smith', 'Christopher Williams', 'Latoya Clark', 'Brian Rubio', 'Dawn Jones', 'Matthew Walsh', 'Derrick Sanders', 'Jennifer Walker', 'Carrie Ramirez', 'Sean Macias', 'Jackie Arias', 'Peter Choi'], 'age': [65, 79, 68, 74, 68, 78, 70, 74, 73, 79, 69, 82, 65, 66, 73, 66, 67, 68, 77, 80, 76], 'email': ['garrett63@hotmail.com', 'jacquelinenoble@williams-ayala.com', 'timothy64@vasquez.com', 'christopher42@salazar-thomas.info', 'tblack@butler-davis.org', 'cookchristopher@yahoo.com', 'jacksonbrian@buckley.net', 'mark60@mitchell.com', 'bethgriffin@yahoo.com', 'christinamullen@yahoo.com', 'csanchez@everett.org', 'lanceosborne@hotmail.com', 'mchambers@rice.com', 'thaynes@yahoo.com', 'stanley25@rivera-wood.com', 'krystal27@yahoo.com', 'sstephens@gmail.com', 'llam@simpson.com', 'jonathan35@gmail.com', 'sandra83@ramirez-wheeler.com', 'jill19@booker.biz'], 'zipcode': ['49168', '63196', '30496', '54252', '45744', '71849', '16332', '27624', '29157', '24061', '13593', '79851', '80314', '66603', '27152', '87877', '73042', '36689', '94666', '53858', '83760'], 'city': ['South Danielport', 'Port Stephanie', 'Whitneymouth', 'Romerofort', 'Normanville', 'Cooperton', 'North Stephenfort', 'Romerofort', 'Lake Marissa', 'Walkerview', 'New Terri', 'Deborahbury', 'Thomasmouth', 'Rothton', 'Loganchester', 'East Brookefort', 'Loganchester', 'Loganchester', 'North Stephenfort', 'Michelefurt', 'Cooperton'], 'activity': [5, 4, 3, 1, 3, 4, 4, 3, 2, 0, 3, 9, 7, 8, 7, 0, 4, 8, 6, 9, 0]}


class L3_Q3_Answers(SQL2DataFrame_Answer):
    output = {'id': [630], 'name': ['Ms. Erin Walsh DDS'], 'age': [8], 'email': ['richardlowery@duncan.biz'], 'zipcode': ['49044'], 'city': ['Marystad'], 'activity': [9]}
    
class L3_Q7_Answers(SQL2DataFrame_Answer):
    output = {'id': [116, 792, 925, 1096, 1235, 1337, 1422, 1501, 1953], 'title': ['Rosencrantz & Guildenstern are Dead: A Play in Three Acts (Favorite Broadway Dramas)', 'Assassins: An Experience in Sound and Drama: Assignment: Jerusalem, Target: Antichrist', 'Soul Harvest: The World Takes Sides', 'Peopleware: Productive Projects and Teams', 'Patriot Games (Jack Ryan, #1)', 'Clear and Present Danger (Jack Ryan, #5)', 'The Things They Carried', 'Rubicon: The Triumph and Tragedy of the Roman Republic', 'The Hunt For Red October (Jack Ryan, #3)'], 'author': ['Tom Stoppard', 'Tim LaHaye', 'Tim LaHaye', 'Tom DeMarco', 'Tom Clancy', 'Tom Clancy', "Tim O'Brien", 'Tom Holland', 'Tom Clancy'], 'isbn': ['0-7497-3986-X', '0-14-358843-5', '1-194-70365-8', '1-9822-9941-X', '0-388-73648-8', '0-227-38113-0', '1-276-69413-X', '0-427-79148-0', '0-01-999660-8']}
    
class L3_Q9_Answers(SQL2DataFrame_Answer):
    output = {'id': [91, 100, 183, 186, 204, 339, 500, 699], 'name': ['Jaime Taylor', 'Linda Taylor', 'Donald Taylor', 'Adam Taylor', 'Jesse Taylor MD', 'Sandra Tapia', 'Oscar Taylor', 'Laura Taylor'], 'age': [15, 46, 12, 56, 18, 74, 28, 30], 'email': ['lindsey20@gmail.com', 'garzacindy@reyes.org', 'robinsonfrances@ingram-mcintosh.com', 'richardbrewer@robinson.net', 'kpark@peterson.com', 'mark60@mitchell.com', 'cohenangel@delgado.com', 'wendy47@hotmail.com'], 'zipcode': ['94872', '97791', '90822', '81151', '36035', '27624', '49997', '78209'], 'city': ['Deborahbury', 'Port Stephanie', 'Lake Marissa', 'Brianchester', 'Rothton', 'Romerofort', 'Lake Marissa', 'Romerofort'], 'activity': [6, 7, 8, 2, 8, 3, 9, 7]}
    
class L3_Q8_Answers(SQL2DataFrame_Answer):
    shape = ((49, None), "max")

class L3_Q14_Answers(DataFrame_Answer):
    shape = [((97, 3), "max", ""), ((97, None), -3, "Try sep='\t' to split into multiple columns, based on tab spacing")]
    
    def check(self, ns=None):
        try:
            ans = ns.data
        except:    
            ans = self.get_resolved(self.q, ns)
        return self._check_df(ans)
    
key = dict(
    q1 = dict(entrytype='cell', pts=4, auto=True, answers=L3_Q1_Answers,
              question="Write the SQL to select the first 10 records of the books table."),
    q2 = dict(entrytype='cell', pts=4, auto=True, answers=L3_Q2_Answers,
              question="Write the SQL to select the patrons that are equal to or over 65 years old."),
    q3 = dict(entrytype='cell', pts=4, auto=True, answers=L3_Q3_Answers,
              question="Write the SQL to select any patrons that are 8 years old and have the zip code 49044."),
    q4 = dict(entrytype='var', pts=4, auto=True, 
              answers=[(1977, "max", ""), (250, -2, "sort by return_time"),
                       (122, -1, "sort DESC, not ASC"), (1898, -2, "sort by return_time")],
              question="What is the id of the most recently returned book listed in the circulation table?"),
    q5 = dict(entrytype='var', pts=4, auto=True, answers=[11], question="How many records are listed in books with George Orwell as the author?"),
    q6a = dict(entrytype='var', pts=4, auto=True,
               answers=[("% C. %", 4), ("% C. %", 4), ("% _. %", 3),
                        ("%C.%", 3), ("_ C. _", 2)],
               filters=['sql_just_like_comparison'],
               question="Written by an author with the middle initial C, like in Arthur C. Clarke: WHERE author LIKE ...."),
    q6b = dict(entrytype='var', pts=4, auto=True, 
               answers=[("The %", 4), ("The _", 2), ("%The %", 2), ("_The %", 2)],
               question="Title starting with the word The:  WHERE title LIKE ...",
               filters=['sql_just_like_comparison']),
    q6c = dict(entrytype='var', pts=5, auto=True,
               answers=[("T_m %", 5), ("T_m", 4), ("T_m _", 4), ("T%m", 3)],
               question="Written by authors named like Tim or Tom (starts with a T, three characters, ends with an m): WHERE author LIKE ...",
                filters=['sql_just_like_comparison']),
    q7 = dict(entrytype='cell', pts=5, auto=True, answers=L3_Q7_Answers,
              question="Write the SQL for the last question, matching only Tim or Tom (e.g. not 'Tam'). Tip: Don't get fancy, try an or statement."),
    q8 = dict(entrytype='cell', pts=5, auto=True,
              question="How would you retrieve emails from .org domains? Write the SQL.",
             answers=L3_Q8_Answers),
    q9 = dict(entrytype='cell', pts=5, auto=True, answers=L3_Q9_Answers,
              question="Write the SQL to retrieve any people whose last name starts with Ta."),
    q10 = dict(entrytype='var', pts=7, auto=False,
               question="Write the SQL to retrieve the email addresses for all pets where the species is 'cat'."),
    q11 = dict(entrytype='var', pts=5, auto=False,
               question="Write the SQL to retrieve all the owners with a missing (i.e. null) email."),
    q12 = dict(entrytype='var', pts=7, auto=False,
               question="Write the SQL to retrieve all comments with information on whether the comment is shadow banned."),
    q13a = dict(entrytype='var', pts=3, auto=True, answers=["LEFT OUTER JOIN"],
                question="What type of JOIN is necessary to retrieve all the comments, with user names and images if available?"),
    q13b = dict(entrytype='var', pts=3, auto=True, answers=["INNER JOIN"],
                question="What type of JOIN is necessary to retrieve all the comments by active users, with user names included?"),
    # Technically not possible (nothing said about deleted comments still existing in the system)
    # But easy to make mistake
    q13c = dict(entrytype='var', pts=4, auto=True, answers=[("Not possible.", "max"),
                  ("INNER JOIN", -1, "Not possible. Nothing to suggest that deleted comments can be retrieved, but if they could, this would work."), ("LEFT OUTER JOIN", -2, "Not possible. Nothing to suggest that deleted comments can be retrieved. If they could, no need to return the user-less comments for this question, although it would still (inefficiently) work."), ("FULL OUTER JOIN", -2, "Not possible. Nothing to suggest that deleted comments can be retrieved. If they could, no need to return the user-less comments for this question, although it would still (inefficiently) work.")],
                question="What type of JOIN is necessary to retrieve all the active and deleted comments by a user?"),
    # TODO future - name the variable q14_answers, not 'data', like the other questions
    q14 = dict(entrytype='cell', pts=7, auto=True,  answers=L3_Q14_Answers,
               question="Write the code to read_csv..."),
    q15 = dict(entrytype='cell', pts=4, auto=False,
               question="What's the code for getting the means of all the columns for data?"),
    q16 = dict(entrytype='var', pts=4, auto=False, question="What does this code do: data[:5]"),
    q17 = dict(entrytype='var', pts=4, auto=False, question="What does this code do: data[['Sex', 'Bwt']]"),
    q18 = dict(entrytype='var', pts=4, auto=False, question="What does this code do: data.query('Hwt > 13')"),
)

