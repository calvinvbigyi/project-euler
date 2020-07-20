#Given an input "bit pattern" which is a string containing only the characters '0', '1' and '?'
# output a list of all "bit strings" which match the pattern where '?' acts as a wild card.
#For example: "?01?" -> ["0010", "0011", "1010", "1011"]

#test_str = '?01?'
#test_output = ['0010', '0011', '1010', '1011']
import itertools
#javier's solution
def replace(string):
    if string == '':
        return ['']
    if string[0] != '?':
        return [string[0] + rest for rest in replace(string[1:])]
    return [x + rest for rest in replace(string[1:]) for x in ['0', '1']]

print(replace('?01?'))

#joey's solution
def replace_joey(x):
	if x == '':
		return ['']
	else:
		result_arr = []
		for s in replace(x[1:]):
			if x[0] == '?':
				result_arr.append(['0' + s, '1' + s])
			else:
				result_arr.append([x[0] + s])

		return [item for sublist in result_arr for item in sublist]

print(replace_joey('?01?'))

#erin's solution
def replace_erin(string):
    return [string.replace('?','{}').format(*p) for p in itertools.product([0,1], repeat=string.count('?'))]

print(replace_erin('?01?'))
# 1. start from simple solution and want to expand it to the general case in the question
# 2. successfully implmented part of the question "?" -> "1"
# 3. he had questions/issues with expanding the solution with two "?"s and he seems that he 
# could debug his own codes.
# 4. guiding questions: how to go back to the original list
# 5. he's thinking about while loop or for loop, but never occurred to him that he could use
# recursion
# 6. he wants to go back to the original str_li.
# 7. he's stuck on the 
# Loop through before doing any join. 
