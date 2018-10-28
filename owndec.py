#This is a exercise of writing a decision tree from scratch
#It is based on googles youtube video and code

#first must create the toy dataset;
# it is a list that contains the 1 label and two features


import numpy as np
from collections import Counter


training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]
training_data=np.array(training_data)

#first must create all help functions
#We also need the headers

header=['color','diam','Cat']

#first muust try to get distinct rows per coloum, own mod using numpy array
def unique_vals(rows,col):
     return set(rows[:,col])



#then class counts must be defined. This means the number of each classes it will return a dict with classes
#bit mod from example, this is the already defined verson


def countclass(rows):
    from collections import Counter
    return Counter(rows[:,2])


#Need function for is numeric:

def is_numeric(value):
    """Test if a value is numeric."""
    return isinstance(value, int) or isinstance(value, float)

class Question:
    """A Question is used to partition a dataset.
    This class just records a 'column number' (e.g., 0 for Color) and a
    'column value' (e.g., Green). The 'match' method is used to compare
    the feature value in an example to the feature value stored in the
    question. See the demo below.
    """

    def __init__(self, column,value):
        self.column=column
        self.value=value

    def match(self, example):
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        # This is just a helper method to print
        # the question in a readable format.
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            header[self.column], condition, str(self.value))



Question(1, 3)
# How about one for a categorical attribute
q = Question(0, 'Green')

print(q)
# Let's pick an example from the training set...
example = training_data[0]
# ... and see if it matches the question
q.match(example)
#######

def partition(rows, question):
    """Partitions a dataset.
    For each row in the dataset, check if it matches the question. If
    so, add it to 'true rows', otherwise, add it to 'false rows'.
    """

    true_rows,false_rows=np.empty([3,]),np.empty([3,])

    #


    for row in rows:
        if question.match(row):
           true_rows= np.vstack((true_rows,row))
        else:
           false_rows= np.vstack((false_rows,row))

    return true_rows[1:],false_rows[1:]

#calculate gini of split

def gini(rows):
    counts=countclass(rows)
    impurity=1
    for cat in counts:
        p=counts[cat]/float(len(rows))
        impurity -= p**2
    return impurity


#testcase
rows=np.array([['red',1,'Apple'],['green',3,'Grape']])
rows2=np.array([['red',1,'Apple'],['green',3,'Grape'],['green',3,'Grape'],['green',3,'Grape']])



#test for infogain formula
def info_gain(left, right, current_uncertainty):
    """Information Gain.
    The uncertainty of the starting node, minus the weighted impurity of
    two child nodes.
    """
    p = float(len(left)) / (len(left) + len(right))
    return current_uncertainty - p * gini(left) - (1 - p) * gini(right)

#test
true_rows, false_rows = partition(training_data, Question(0,'Red'))
testinfogain=info_gain(true_rows,false_rows,gini(training_data))

print(testinfogain)
