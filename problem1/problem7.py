def separate_number(q,string):

	for j in range(q):
		inp = string[j]
		if inp[0] == '0':
			print("NO")
			continue
		result = False
		for i in range(1,len(inp)+1):
			t = ""
			cur = int(inp[:i])
			check = 0
			while len(t) < len(inp):
				t += str(cur)
				cur += 1
				check += 1
			if check > 1 and t == inp:
				print("YES"), inp[:i]
				result = True
				break
		if not result:
			print("NO")



q=int(input('Enter the number of queries'))
s=[]
for x in range(q):
	print('Enter string', x + 1, ' ')
	temp=input()
	s.append(temp)
separate_number(q,s)