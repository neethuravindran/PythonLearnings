# PythonTrainingSamples
Python Samples gives you essential elements you need to kickstart your journey in Python programming. Explore the foundational concepts for Python development. 
These samples are well suited for beginners and also for experienced programmers. 

    NumPy
    https://www.geeksforgeeks.org/introduction-to-numpy/
    Pandas
    https://www.geeksforgeeks.org/introduction-to-pandas-in-python/
    Data Visualization
    https://www.geeksforgeeks.org/data-visualization-and-its-importance/
    File Operations
    https://www.geeksforgeeks.org/file-handling-python/
    Functions OOPs
    https://www.geeksforgeeks.org/python-oops-concepts/

**Prerequisites :**
 
  Download and Install Python 3 Latest Version
  Install Pycharm setup / Make use of VS studio Code.
  

Explore and do work out on each python files in this repo w.r.t to questions added below 

The below are questions which is worked out as part of python certification training program
  
**Training Sample Workout Questions:**

1. Write a program which will find factors of given number and find whether the factor is even or odd
2. Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically
3. Write a program, which will find all the numbers between **1000 and 3000** (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
4. Write a program that accepts a sentence and calculate the number of letters and digits.
5. Design a code which will find the given number is Palindrome number or not.
6. Write a program which accepts a string from console and print it in reverse order.
7. Write a program which count and print the numbers of each character in a string input by console.
8. With two given lists **[1,3,6,78,35,55]** and **[12,24,35,24,88,120,155]**, write a program to make a list whose elements are intersection of the above given lists.
9. With a given list **[12,24,35,24,88,120,155,88,120,155]**, write a program to print this list after removing all duplicate values with original order reserved.
10. By using list comprehension, please write a program to print the list after removing the value **24** in **[12,24,35,24,88,120,155]**.
11. By using list comprehension, please write a program to print the list after removing the **0th,4th,5th** numbers in **[12,24,35,70,88,120,155]**.
12. By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by **5** and **7** in **[12,24,35,70,88,120,155]**.
13. Please write a program to randomly generate a list with 5 numbers, which are divisible by **5** and **7**, between **1** and **1000** inclusive.
14. Write a program to compute **1/2+2/3+3/4+...+n/n+1** with a given n input by console (n>0).
15. What is the output of the following code? 
      **nums = set([1,1,2,3,3,3,4,4])**
        print(len(nums))
16. What will be the output? 
      **d = {"john":40, "peter":45}
      print(list(d.keys()))**
17. A website requires a user to input username and password to register. Write a program to check the validity of password given by user. Following are the criteria for checking password:
       1. At least 1 letter between [a-z]
       2. At least 1 number between [0-9]
       1. At least 1 letter between [A-Z]
       3. At least 1 character from [$#@]
       4. Minimum length of transaction password: 6
       5. Maximum length of transaction password: 12**
18. Write a for loop that prints all elements of a list and their position in the list, **a = [4,7,3,2,5,9]**
19. How do you Count The Number Of Times Each Value Appears In An Array Of Integers?
    **[0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]**
    Answer should be array(**[4, 2, 1, 1, 3, 2, 0, 0, 0, 1]**) which means 0 comes 4 times, 1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so on.

20. Create a numpy array **[[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]** and filter the elements greater than 5.
21. Create a numpy array having NaN (Not a Number) and print it.
    **array([ nan, 1., 2., nan, 3., 4., 5.])**
     Print the same array omitting all elements which are nan
22. Create a 10x10 array with random values and find the minimum and maximum values.
23. Create a random vector of size 30 and find the mean value.
24. Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
25. Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column.
26. Create a four dimensions array get sum over the last two axis at once
27. Extract data from the given **SalaryGender CSV** file and store the data from each column in a separate NumPy array
     Find: 1. The number of men with a PhD 2. The number of women with a PhD
     Store the “Age” and “PhD” columns in one DataFrame and delete the data of all people who don’t have a PhD from SalaryGender CSV file.
     Calculate the total number of people who have a PhD degree from SalaryGender CSV file.

28.
 **Business challenge/requirement**
The University has data of Math, Physics and Data Structure score of sophomore students.
  This data is stored in different files. 
  The University has hired a data science company to do analysis of scores and find if there is 
  any correlation of score with age, ethnicity etc. Before the data is given to the company you have to do data wrangling.
**Key issues**
  Ensure students identify is not revealed to the agency and only relevant data is shared
**Data volume**
- In thousands, but only around 1800 records are shared in files MathScoreTerm1.csv DSScoreTerm1.csv, PhysicsScoreTerm1.csv
**Business benefits**
  University can get more students enrollment by improving its international ranking through personalized course/curriculum for students
**Approach to Solve**
    You have to use fundamentals of Numpy and Pandas covered in module 4.
    1. Read the three csv files which contains the score of same students in term1 for each Subject
    2. Remove the name and ethnicity column (to ensure confidentiality)
    3. Fill missing score data with zero
    4. Merge the three files
    5. Change Sex(M/F) Column to 1/2 for further analysis
    6. Store the data in new file – ScoreFinal.csv
**Enhancements for code**
    You can try these enhancements in code
        1. Convert ethnicity to numerical value
        2. Fill the missing score for a student to the average of the class



  

29. Analyse various school outcomes in Tennessee using pandas. Suppose you are a public school administrator. Some schools in your state of Tennessee are performing below average academically. Your superintendent, under pressure from frustrated parents and voters, approached you with the task of understanding why these schools are under-performing. To improve school performance, you need to learn more about these schools and their students, just as a business needs to understand its own strengths and weaknesses and its customers. Though you is eager to build an impressive explanatory model, you know the importance of conducting preliminary research to prevent possible pitfalls or blind spots. Thus, you engages in a thorough exploratory analysis, which includes: a lit review, data collection, descriptive and inferential statistics, and data visualization.
**Phase 1 - Data Collection**
Here is a data of every public school in middle Tennessee. The data also includes various demographic, school faculty, and income variables. You need to convert the data into useful information.
• Read the data in pandas data frame
• Describe the data to find more details
**Phase 2 - Group data by school ratings**
Chooses indicators that describe the student body (for example, reduced_lunch) or school administration (stu_teach_ratio) hoping they will explain school_rating. reduced_lunch is a variable measuring the average percentage of students per school enrolled in a federal program that provides lunches for students from lower-income households. In short, reduced_lunch is a good proxy for household income.
Isolates ‘reduced_lunch’ and groups the data by ‘school_rating’ using pandas groupby method and then uses describe on the re-shaped data
**Phase 3 – Correlation analysis**
Find the correlation between ‘reduced_lunch’ and ‘school_rating’. The values in the correlation matrix table will be between -1 and 1. A value of -1 indicates the strongest possible negative correlation, meaning as one variable decreases the other increases. And a value of 1 indicates the opposite.
**Phase 4 – Scatter Plot**
Find the relationship between school_rating and reduced_lunch, Plot a graph with the two variables on a scatter plot. Each dot represents a school. The placement of the dot represents that school's rating (Y-axis) and the percentage of its students on reduced lunch (x-axis). The downward trend line shows the negative correlation between school_rating and reduced_lunch (as one increases, the other decreases). The slope of the trend line indicates how much school_rating decreases as reduced_lunch increases. A steeper slope would indicate that a small change in reduced_lunch has a big impact on school_rating while a more horizontal slope would indicate that the same small change in reduced_lunch has a smaller impact on school_rating.
**Phase 5 – Correlation Matrix**
An efficient graph for assessing relationships is the correlation matrix, as seen below; its color-coded cells make it easier to interpret than the tabular correlation matrix above. Red cells indicate positive correlation; blue cells indicate negative correlation; white cells indicate no correlation. The darker the colors, the stronger the correlation (positive or negative) between those two variables. Draw a graph of correlation matrix having all important fields of data frame.
30. Create a random matrix and Compute a matrix rank
31. Create a random array and swap two rows of an array.
32. You are given a dataset, containing the number of hurricanes occurring in the United States along the coast of the Atlantic. Load the data from the dataset into your program and plot a Bar   Graph of the data, taking the Year as the x-axis and the number of hurricanes occurring as the Y-axis.
33. The dataset given, records data of city temperatures over the years 2014 and 2015. Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.
34. Plot a pie-chart of the number of models released by every manufacturer, recorded in the data provide. Also mention the name of the manufacture with the largest releases.
35. Enter the elements which needs to find in given list at position
36. Weather forecasting organization wants to show is it day or night. So, write a program for such organization to find whether is it dark outside or not.
37. Write a program to find distance between two locations when their latitude and longitudes are given.
38. Design a software for bank system. There should be options like cash withdraw, cash credit and change password. According to user input, the software should provide required output.

39. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
40. Write a program which can compute the factorial of a given numbers. Use recursion to find it.
Hint: Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

41. Write a program that calculates and prints the value according to the given formula:
**Q = Square root of [(2 * C * D)/H]**
Following are the fixed values of C and H: C is 50. H is 30.
D is the variable whose values should be input to your program in a comma- separated sequence.
Example:
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24

42. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: **i=0,1.., X-1; j=0,1,¡Y-1.**
Example:
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

43. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

44. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
**HELLO WORLD
PRACTICE MAKES PERFECT**
45. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
46. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
47. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
48. Give example of fsum and sum function of math library
49. A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps. Write a program to compute the distance current position after sequence of movements.
Hint: Use math module.
50. Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
**Data volume**
- Approx 500K records – file BigMartSalesData.csv

51. Let the x axis data points and y axis data points are
X = [1,2,3,4] y = [20, 21, 20.5, 20.8]
1: Draw a Simple plot
2: Configure the line and markers in simple plot
3: configure the axes
4: Give title of Graph & labels of x axis and y axis
5: Give error bar if y_error = [0.12, 0.13, 0.2, 0.1]
6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100
7: Give a font size of 14
8: Draw a scatter graph of any 50 random values of x and y axis
9: Create a dataframe from following data
'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]
Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
10: Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore with the size = 300 and the color determined by sex
52. CustomerEcom.py

    **Business challenge/requirement**
    GoodsKart—largest ecommerce company of Indonesia with revenue of $2B+ acquired another ecommerce company FairDeal. FairDeal has its own IT system to maintain records of customer, sales etc. For ease of maintenance and cost savings GoodsKart is integrating customer databases of both the organizations hence customer data of FairDeal has to be converted in GoodsKart Customer Format.
    **Key issues**
    GoodsKart customer data has more fields than in FairDeal customer data. Hence FairDeal data needs to be split and stored in GoodsKart Customer Object Oriented Data Structure
    **Considerations**
    System should convert the data at run time    
    **Business benefits**
      GoodsKart can eventually sunset IT systems of FairDeal and reduce IT cost by 20-30%
      **Approach to Solve**
      You have to use fundamentals of Python taught in module 3.
      1. Read FairDealCustomerData.csv
      2. Name field contains full name – use regular expression to separate title, first name, last name
      3. Store the data in Customer Class
      4. Create Custom Exception – CustomerNotAllowedException
      5. Pass a customer to function "createOrder" and throw CustomerNotAllowedException in case of blacklisted value is 1
      **Enhancements for code**
      You can try these enhancements in code
      1. Change function createOrder to take productname and product code as input
      2. Create Class Order
      Return object of type Order in case customer is eligible

53. GoogleSearch.py
Create a python script called googlesearch that provides a command line utility to
perform google search. It gives you the top links (search results) of whatever you want to
search on google.
54. Location.py
Create a script called location that return the location parameters of any location you want.
55. LoanEligibility.py

    **Business challenge/requirement**
    Bank of Portugal runs marketing campaign to offer loans to clients. Loan is offered to only clients with particular professions. List of successful campaigns (with client data) is given in  attached dataset. You have to come up with program which reads the file and builds a set of unique profession list and given input profession of client – system tells whether client is eligible to be approached for marketing campaign.
    **Key issues**
    Tele Caller can only make x number of cold calls in a day. Hence to increase her effectiveness only eligible customers should be called
    **Considerations**
    Current system does not differentiate clients based on age and profession
    **Data volume**
    447 records in bank-data.csv   
    **Business benefits**
    Company can achieve between 15% to 20% higher conversion by targeting right clients
    **Approach to Solve**
    You have to use fundamentals of Python taught in module 3
      1. Read file bank-data.csv
      2. Build a set of unique jobs
      3. Read the input from command line –profession
      4. Check if profession is in list
      5. Print whether client is eligible
      **Enhancements for code**
      You can try these enhancements in code
      1. Compute max and min age for loan eligibility based on data in csv file
      2. Store max and min age in dictionary
      3. Make the profession check case insensitive
      4. Currently program ends after the check. Take the input in while loop and end only if user types "END" for profession

  
  
