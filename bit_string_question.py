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


#berkay's solution
def replace_berkay(x):
	if x == '':
		yield ''
	else:
		for s in replace_berkay(x[1:]):
			if x[0] == '?':
				yield '0' + s
				yield '1' + s
			else:
				yield x[0] + s

print(replace_erin('?01?'))

#brett's solution
def match_bits(pattern):
    vals = [""]
    for m in pattern:
        if m == "?":
            vals = [v + "0" for v in vals] +  [v + "1" for v in vals]
        else:
            vals = [v + m for v in vals]
    return vals
    
print(match_bits('?01?'))