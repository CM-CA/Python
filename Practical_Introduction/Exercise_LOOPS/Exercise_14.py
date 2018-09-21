

side = int(input("Please input side length of diamond: "))

for x in list(range(side)) + list(reversed(range(side-1))):
    print('{: <{w1}}{:*<{w2}}'.format('', '', w1=side-x-1, w2=x*2+1))


# So how does it work?
#
# First we need a counter that counts up to side and then back down again. There is nothing stopping you from
# appending two range lists together so:
#
# list(range(3)) + list(reversed(range(3-1))
# This gives you a list [0, 1, 2, 1, 0]
#
# From here we need to work out the correct number of spaces and asterisks needed for each line:
#
#   *        needs 2 spaces 1 asterix
#  ***       needs 1 space  3 asterisks
# *****      needs 0 spaces 5 asterisks
# So two formulas are needed, e.g. for side=3:
#
# x   3-x-1   x*2+1
# 0   2       1
# 1   1       3
# 2   0       5
# Using Python's string formatting, it is possible to
# specify both a fill character and padding width. This avoids having to use string concatenation.