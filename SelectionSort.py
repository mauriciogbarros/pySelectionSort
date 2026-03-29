def selection_sort(numbers):
	length = len(numbers)
	for i in range(length - 1):
		min_i = i
		for j in range(i + 1, length):
			if numbers[j] < numbers[min_i]:
				min_i = j

		if min_i != i:
			numbers[i], numbers[min_i] = numbers[min_i], numbers[i]

	return numbers

print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))