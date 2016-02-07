'''
Day 27: Testing Part II!

Problem Statement

A Discrete Mathematics professor has a class of N students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than K students are present when class starts. Given the arrival time of each student, determine if the class is canceled.

Input Format

The first line of input contains T, the number of test cases.

Each test case spans two lines. The first has two space-separated integers, N (students in the class) and K (the cancelation threshold). The second contains N space-separated integers (a1,…,aN) describing the students' arrival times.

Note: Non-positive arrival times (ai=0) indicate the student arrived early or on time; positive arrival times (ai>0) indicate the student arrived ai minutes late. If a student arrives exactly on time (ai=0), the student is considered to have entered before the class started.

Output Format

For each test case, print the word YES if the class is canceled or NO if it is not, on a new line.

Example

When properly solved, this input:

2
4 3
-1 -3 4 2
4 2
0 -1 2 1
Should produce this output:

YES
NO
For the first test case, K=3. The professor wants at least 3 students in attendance, but only 2 arrive on time (-3 and -1). Thus, the class is canceled.

For the second test case, K=2. The professor wants at least 2 students in attendance, and 2 do arrive on time (0 and -1). Thus, the class is not canceled.

Your Task

Create and print one or more test cases for the problem above that meet the following criterion: 
T=5 
1=N=200 
1=K=N 
-1000=ai=1000,where i?[1,N] 
The value of N should be distinct across all the test cases. 
Array a must have at least one zero, one positive integer, and one negative integer.

You must create five test cases to earn the maximum possible score.

The output for your test case (were it to run against a correct solution to the problem above) should be:

YES
NO
YES
NO
YES
Print your test cases as output the same way the solution would expect to read them as input. For example:

print('1')
print('4 3')
print('-1 -3 4 2')
print('5 2')
print('0 -1 2 1 4')
Scoring

If you submit x correct test cases, your score will be 20.0×x. If you submit more than 5 test cases, only the first 5 test cases will be evaluated.

'''

print "5"
print "4 3" 
print "-1 4 5 0"
print "3 2"
print "-1 5 0"
print "5 4"
print "-1 4 5 0 7"
print "6 1"
print "-1 4 5 0 3 3"
print "7 6"
print "-1 4 5 0 9 9 9"