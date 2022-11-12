#Solution to binary sequence problem of hackerEarth
#https://www.hackerearth.com/practice/python/getting-started/numbers/practice-problems/algorithm/binary-sequence-dbaf9d61/


def case_builder(string):
        string = [k for k in string]
        cases = []
        for j in range(len(string)):
            ind = string.index('p')
            string[j] = 'p'
            string[ind] = '0'
            result = ''.join(string)
            cases.append(result)

        return cases

def finder(case, a, b):
	a_s = 0
	b_s = 0

	for l, m in enumerate([z for z in case]):
		if m == '0':
			nstring = case[l:]
			counter = nstring.count('1')
			a_s += counter

		else:
			nstring = case[l:]
			counter = nstring.count('0')
			b_s += counter

	return (a_s, b_s)

#for no. of taste cases add for loop here.
bin_str = input()
x, y, a, b = bin_str.split(' ')
sample_string = '0'*int(x) + 'p'
ones = "1"*int(y)
cases = case_builder(sample_string)
final = [j.replace('p', ones) for j in cases]

target = []
for case in final:
    result = finder(case, a, b)
    if result[0] == int(a) and result[1]==int(b):
        target.append(True)

    else:
        target.append(False)

if True in target:
    ind_req = target.index(True)
    resultant = final[ind_req]
    print(resultant, 'Yes')

else:
    print('No')







            
