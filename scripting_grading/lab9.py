key = dict(
    q1a = dict(entrytype='var', pts=10, auto=True,
              question="Among prolific raters (those with more than 100 ratings), which user has the lowest average rating?",
              answers=[609, "609"]),
    q1b = dict(entrytype='var', pts=10, auto=True,
              question="Identify the user with the biggest discrepency in their love for Action movies over Drama movies. (min 5 ratings of each genre, either mean or median are fine)",
              answers=[(244,10), ("244", 10),
                       (378, 10), ("378", 10), # if sorted backward and taking median
                       (156, 10), ("156", 10), # if sorted backward and taking mean
                       (410, 8), # didn't filter
                       ]),
     q1c = dict(entrytype='cell', pts=15, auto=False,
              question=" Create a DataFrame of the *worst* and *best* movie by year, focusing only on movies with at least 5 reviews and using the *mean* of user ratings as your measure of good or bad",
              ),
    q2 = dict(entrytype='cell', pts=15, auto=False,
              question="Plot per-capita library revenue and per-pupil education spending",
              ),
    q3a = dict(entrytype='cell', pts=10, auto=False,
              question="Split sovereign states",
              ),
    q3b = dict(entrytype='cell', pts=5, auto=False,
              question="Ensure that common_name is in formal_name field when there isn't a formal name",
              ),

    )