###[[6/18/2014] Challenge #167 [Intermediate] Final Grades](http://www.reddit.com/r/dailyprogrammer/comments/28gq9b/6182014_challenge_167_intermediate_final_grades/)

It is that time of year again. The Intro to Computer Science 101 class has ended at Greendale community college and the professor has to submit the final grades. The school requires grades to be submitted with a letter grade. In addition the grades should be submitted from the "best" student first. The individual scores should be be listed from "worse" to "best".

######Input:

You will be given class roster in the form of:

    (first name) , (last name) (score 1) (score 2) (score 3) (score 4) (score 5)

######Data Crunch:

Each student has 5 scores from 1 to 100. So a total of 500 points for the class.
Based on this you must determine what grade they get on a percentile 1-100. 

The letter Grades are assigned based on the following

* 90-100 A
* 80-89 B
* 70-79 C
* 60-69 D
* 59 and below F

Those scoring in the top 3 percent of the rank get a "+" added. Those scoring in the lower 3 percent of the rank get a "-". However there is no "+" for an A and there are no "+" or "-" for an F grade.

    student scoring 82% would be a B-
    student scoring 79% would be a C+


Note: Final Grades are rounded to the nearest whole number. So 89.5 is 90 and 89.4 is 89.

######Output:

The output should be ranked from the "best" student who had the best grade to the "worse" student who had the lowest grade. The 5 scores should also be arranged from the "lowest" to "highest".


The output should take on this form:

    (Last Name) (First Name) (Final percentage) (Final Grade) : (Scores 1-5 from low to high)

######Example:

Input:

    Valerie,	Vetter 79	81	78	83	80
    Richie,	Rich	88	90	87	91	86

Output:

    Rich,    Richie  (88%) (B+): 86 87 88 90 91
    Valerie, Vetter (80%) (B-): 78 79 80 81 83 
