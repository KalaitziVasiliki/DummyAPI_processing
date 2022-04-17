# DummyAPI_processing

Selected Toolkit
• Python 3.8.3 
• Postgres relational database
• Tool for the automation or monitoring aspects: Cron, Oozie scheduling can also be an option, there is a lot of gained experience in scheduling with Oozie, so feel free to ask anything..

Exercise 1: Data Ingestion and Validation
Please fetch the following objects from the source:
- Users (full)
- Posts (full)
- Comments
Try and be mindful of the fact that Users and Posts by default are fetched as “preview” items,
therefore you’ll have to make sure that all columns are fetched.
Feel free to use the documentation https://dummyapi.io/docs/models to validate the incoming
data. Examples of data validation rules would be “No posts without owners”, “No comments
without owners”, “No posts with negative likes” etc. Any checks for duplications should also
happen in this step.
As this will be the “raw” extract, you may keep any nested JSON in that form, but please make
sure that we don’t waste space by keeping duplicate data. For example, the user preview item
within Posts and Comments is redundant, a simple ID will suffice.

Exercise 2: Data Loading
After fetching and validating the data, you will need to load it to the data warehouse. For the
scope of this exercise, you may use any relational database of your choice.
Before loading the data, it’s also necessary to unnest the “Location” object that exists within
the User entity. This could also happen during the data modelling step, but it would save some
costs to do this processing before loading.
Please make sure that you have taken into account all data integrity constraints, and that all
data structures are properly stored for analytics purposes.

Exercise 3: Data Transformation
Now that the data has been loaded within the warehouse, we will build an abstraction layer on
top of it. Please create the relevant fact and dimension tables so that an analyst can answer
the following questions:
- How many new users are added daily?
- What is the average time between registration and first comment?
- Which cities have the most activity, in terms of posts per day?
- Which tags are most frequently encountered, across user posts?
Bonus points, if you can also provide the relevant SQL queries that prove your data pipeline is
robust and can handle all these questions.

Exercise 4: Orchestration & Monitoring
After the data pipeline has been successfully designed and implemented, please share your
thoughts and suggestions regarding pipeline orchestration and monitoring. Feel free to discuss
tools and frameworks that you are familiar with, or would consider suitable for the needs of this
fictional business.

________Code Execution________

In order to run the code, please follow one of the alternatives given below:
  1. Run manually the commands included in  DummyAPI_processing/main/scheduling_proposal/main.sh shell script.
  2. Submit main.sh shell script in your cmd.
