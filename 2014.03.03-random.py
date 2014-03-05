import random

def make_entries(length, bits):
	entries = []

	for i in range(0, random.randint(0, length)):
		entries.append(random.randint(0, bits))

	return entries

def test(entries):
	table = []
	faults = 0

	for i in entries:
		if i not in table:
			faults += 1

			if len(table) >= size:
				table.pop(random.randrange(0,len(table)))
			table.append(i)

	return faults

size = 4
max_length = 15
values = 15

samples = []

for l in range(0,100000):
	entries = make_entries(max_length, values)
	faults = test(entries)

	samples.append(faults)

print sum(samples) / float(len(samples))