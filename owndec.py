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

headers=['color','diam','Cat']

#first muust try to get distinct rows per coloum, own mod using numpy array
def unique_vals(rows,col):
     return set(rows[:,col])



#then class counts must be defined. This means the number of each classes it will return a dict with classes
#bit mod from example, this is the already defined verson


def countclass(rows):
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

    def __init__(self, coloumn,value):
        self.coloumn=coloumn
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
