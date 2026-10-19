[5, 2, 1]

# get a recursion that does (5 - 2) - 1 instead of 5 - (2 - 1)

# current version (I know this looks horrendous but it's just visual)

left_side = 5
right_side = "find_expression"
find_expression_left_side = 2
find_expression_right_side = "find_find_expression_right_side"
find_find_expression_right_side = 1
find_expression = find_expression_left_side - find_find_expression_right_side
side = left_side - find_expression
print(side)

# what we need to get
left_side = 5
right_side = 2
left_side = left_side - right_side
right_side = "find_right_side"
find_right_side_left = 1
find_right_side_right = "nothing here since it's the end, we now return"
left_side = left_side - right_side
"return"

# will this break if we have multiple of this? As in, how will we handle addition? Multiplication?
# we need to remodel our tree and logic

# 5 - 2 - 1 = 
# 5
# - 2
# - 1

# 5 - 2 x 2 = 
# 5
# - 2 x 2

# which I guess could also be
# 5
# - 2
#   x 2

# and then 5 - 2 x 2 - 1 would be
# 5 
# - 2
#   x 2
# - 1

# maybe?
# do we just, instead of recursion, just endlessly add from left to right
# then when multiplication or division come up we just pause the addition and subtraction until we meed a minus or addition?
# could work