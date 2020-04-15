from scripting_grading.grading import Answer

class L3_Q1_Answers(Answer):
    output = {'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'title': ['Sun Tzu: Art Of War', 'The Way and Its Power: A Study of the Tao T? Ching and Its Place in Chinese Thought', 'En Attendant Godot', 'They Came to Baghdad', 'Гарри Поттер и философский камень (Harry Potter, #1)', "Slaughterhouse Five, or The Children's Crusade", 'Dr Jekyll and Mr Hyde', 'The Devil Wears Prada', 'Nineteen Eighty-Four', 'The Hobbit or There and Back Again'], 'author': ['Sun Tzu', 'Arth Estate the', 'Samuel Beckett', 'Agatha Christie', 'J.K. Rowling', 'Kurt Vonnegut Jr.', 'Robert Louis Stevenson', 'Lauren Weisberger', 'George Orwell', 'J.R.R. Tolkien'], 'isbn': ['0-433-19939-3', '0-213-70445-5', '1-75624-696-3', '0-272-39105-0', '0-13-839638-8', '0-307-53448-0', '0-625-41598-1', '0-386-71659-5', '0-401-69650-2', '1-160-78240-7']}

class L3_Q2_Answers(Answer):
    output = {'id': [78, 89, 152, 221, 232, 238, 302, 339, 341, 385, 486, 516, 519, 526, 572, 638, 799, 856, 892, 911, 989], 'name': ['Jennifer Martin', 'Jennifer Bradley', 'Jessica Ramirez', 'David Hammond DDS', 'Kelly Blackburn', 'Christopher James', 'Hannah Simon', 'Sandra Tapia', 'Derek Carson', 'Shannon Smith', 'Christopher Williams', 'Latoya Clark', 'Brian Rubio', 'Dawn Jones', 'Matthew Walsh', 'Derrick Sanders', 'Jennifer Walker', 'Carrie Ramirez', 'Sean Macias', 'Jackie Arias', 'Peter Choi'], 'age': [65, 79, 68, 74, 68, 78, 70, 74, 73, 79, 69, 82, 65, 66, 73, 66, 67, 68, 77, 80, 76], 'email': ['garrett63@hotmail.com', 'jacquelinenoble@williams-ayala.com', 'timothy64@vasquez.com', 'christopher42@salazar-thomas.info', 'tblack@butler-davis.org', 'cookchristopher@yahoo.com', 'jacksonbrian@buckley.net', 'mark60@mitchell.com', 'bethgriffin@yahoo.com', 'christinamullen@yahoo.com', 'csanchez@everett.org', 'lanceosborne@hotmail.com', 'mchambers@rice.com', 'thaynes@yahoo.com', 'stanley25@rivera-wood.com', 'krystal27@yahoo.com', 'sstephens@gmail.com', 'llam@simpson.com', 'jonathan35@gmail.com', 'sandra83@ramirez-wheeler.com', 'jill19@booker.biz'], 'zipcode': ['49168', '63196', '30496', '54252', '45744', '71849', '16332', '27624', '29157', '24061', '13593', '79851', '80314', '66603', '27152', '87877', '73042', '36689', '94666', '53858', '83760'], 'city': ['South Danielport', 'Port Stephanie', 'Whitneymouth', 'Romerofort', 'Normanville', 'Cooperton', 'North Stephenfort', 'Romerofort', 'Lake Marissa', 'Walkerview', 'New Terri', 'Deborahbury', 'Thomasmouth', 'Rothton', 'Loganchester', 'East Brookefort', 'Loganchester', 'Loganchester', 'North Stephenfort', 'Michelefurt', 'Cooperton'], 'activity': [5, 4, 3, 1, 3, 4, 4, 3, 2, 0, 3, 9, 7, 8, 7, 0, 4, 8, 6, 9, 0]}

class L3_Q3_Answers(Answer):
    output = {'id': [630], 'name': ['Ms. Erin Walsh DDS'], 'age': [8], 'email': ['richardlowery@duncan.biz'], 'zipcode': ['49044'], 'city': ['Marystad'], 'activity': [9]}

    
key = dict(
    q1 = dict(entrytype='cell', pts=4, auto=True, question="Write the SQL to select the first 10 records of the books table."),
    q2 = dict(entrytype='cell', pts=4, auto=True, question="Write the SQL to select the patrons that are equal to or over 65 years old."),
    q3 = dict(entrytype='cell', pts=4, auto=True, question="Write the SQL to select any patrons that are 8 years old and have the zip code 49044."),
    q4 = dict(entrytype='var', pts=4, auto=True, question="What is the id of the most recently returned book listed in the circulation table?"),
    q5 = dict(entrytype='var', pts=4, auto=True, answers=[11], question="How many records are listed in books with George Orwell as the author?"),
    q6a = dict(entrytype='var', pts=4, auto=True,
               answers=[("% C. %", 4), ("% C. %", 4), ("% _. %", 3), ("%C.%", 3), ("_ C. _", 2)],
               question="Written by an author with the middle initial C, like in Arthur C. Clarke: WHERE author LIKE ...."),
    q6b = dict(entrytype='var', pts=4, auto=True, 
               answers=[("The %", 4), ("The _", 2), ("%The %", 2), ("_The %", 2)],
               question="Title starting with the word The:  WHERE title LIKE ..."),
    q6c = dict(entrytype='var', pts=5, auto=True,
               answers=[("T_m %", 5), ("T_m", 4), ("T_m _", 4), ("T%m", 3)],
               question="Written by authors named like Tim or Tom (starts with a T, three characters, ends with an m): WHERE author LIKE ..."),
    q7 = dict(entrytype='cell', pts=5, auto=True, question="Write the SQL for the last question, matching only Tim or Tom (e.g. not 'Tam'). Tip: Don't get fancy, try an or statement."),
    q8 = dict(entrytype='cell', pts=5, auto=True, question="How would you retrieve emails from .org domains? Write the SQL."),
    q9 = dict(entrytype='cell', pts=5, auto=True, question="Write the SQL to retrieve any people whose last name starts with Ta."),
    q10 = dict(entrytype='var', pts=7, auto=True, question="Write the SQL to retrieve the email addresses for all pets where the species is 'cat'."),
    q11 = dict(entrytype='var', pts=5, auto=True, question="Write the SQL to retrieve all the owners with a missing (i.e. null) email."),
    q12 = dict(entrytype='var', pts=7, auto=True, question="Write the SQL to retrieve all comments with information on whether the comment is shadow banned."),
    q13a = dict(entrytype='var', pts=3, auto=True, answers=["LEFT OUTER JOIN"],
                question="What type of JOIN is necessary to retrieve all the comments, with user names and images if available?"),
    q13b = dict(entrytype='var', pts=3, auto=True, answers=["INNER JOIN"],
                question="What type of JOIN is necessary to retrieve all the comments by active users, with user names included?"),
    q13c = dict(entrytype='var', pts=4, auto=True, answers=["Not possible."], question="What type of JOIN is necessary to retrieve all the active and deleted comments by a user?"),
    q14 = dict(entrytype='cell', pts=7, auto=True, question="Write the code to read_csv..."),
    q15 = dict(entrytype='cell', pts=4, auto=True, question="What's the code for getting the means of all the columns for data?"),
    q16 = dict(entrytype='var', pts=4, auto=False, question="What does this code do: data[:5]"),
    q17 = dict(entrytype='var', pts=4, auto=False, question="What does this code do: data[['Sex', 'Bwt']]"),
    q18 = dict(entrytype='var', pts=4, auto=False, question="What does this code do: data.query('Hwt > 13')"),
)