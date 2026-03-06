'''
EXERCISE: while loops

We need to use a while loop, in conjunction with an if statement to assess whether our user is: underweight, perfect weight, overweight or obese, according too the Body Mass Index.

To do this, create two variables:

Height - which should be equal to 178

Weight - which should be equal to 50

Then, use a while loop to a maximum weight of 200, incrementing the weight by 1 on each iteration of the loop.

The conditions you will need in order to assess someones weight is:

Under 60 = underweight

Between greater than or equal to 60 and less than 79 = perfect

Greater than or equal to 79 and less than 95 overweight

95 or greater = obese

You can find the solution to this in the next article
'''

# Solution:
height = 178
weight = 50
 
while weight < 200:
    if weight <60:
        print('you are underweight')
    elif weight >= 60 and weight <79:
        print('you are perfect')
    elif weight >=79 and weight <95:
        print('you are overweight')
    else:
        print('you are obese')
        
    weight = weight + 1


'''
EXERCISE: for loops

Create a for loop to iterate over the below list.

For each item in the list, assess whether it is too far to walk. If it's greater than 10 miles, it's too far, otherwise you can walk. Print your decision for each to the screen.

miles = [30, 10, 2, 1, 7.5, 90]
'''

# Solution:
miles = [30, 10, 2, 1, 7.5, 90]
 
for mile in miles:
    if mile > 10:
        print('too far to walk')
    else:
        print('you can walk')