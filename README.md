# Selection Sort
This algorithm works by repeatedly finding the smallest element from the unsorted portion of the list and swapping it with the first unsorted element. It begins by selecting the minimum value in the entire list and swapping it with the first element. Then it moves to the second position, and swaps it with the second element. This process continues, moving throught list one element at a time, until the entire list is sorted.

Selection sort results in a quadratic time complexity in the best, average, and worst case scenarios. The space complexity will be constant `O(1)` because the sorting is done in place and a constant amount of memory is being used regardless of the size of the list.

## User Stories:
1. You should define a function named `selection_sort`.
2. Your `selection_sort` function should have one parameter that represents the list of items.
3. Your `selection_sort` function should take a list and sort the items in place from smallest to largest.
4. Your `selection_sort` function should modify the input list in-place, and return it once it's sorted.
5. Your `selection_sort` function should follow the selection sort algorithm, swapping the smallest element from the unsorted porition of the list with the first unsorted element.
6. Your `selection_sort` function should not perform unnecessary swaps when the smallest element is already in the correct position.
7. Your `selection_sort` function should not use either the built-int `sort()` method or `sorted()` function.
