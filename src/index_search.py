def create_indexed_list(l: list, n):
	indexed_l = []
	slot_size = n // 10
	i = 0

	indexed_l.append(i)

	while i <= n:
		i += slot_size
		indexed_l.append(i - 1)

	return indexed_l

def index_search(l: list, value):
	begin = 0
	end = len(l) - 1
	indexed_l = create_indexed_list(l, len(l))
	counter = 0

	for i in indexed_l:
		if value > l[i]:
			begin = i
		elif value < l[i]:
			end = i
			break
		else:
			begin = i
			end = i
			break

	
	for i in range(begin, end):
		counter += 1
		if value == l[i]:
			print('{} was found at {}'.format(value, i))
			return counter

	print('{} wasnt found'.format(value))
	return counter
