def main():
    nums = input("Please enter an unsorted list of numbers seperated by commas (ex: 12.2, -5.4, 81.12, 2000.0002, 1010101.0, 6.4, 22.12, -10.01): \n")
    nums = nums.split(", ")
    nums_floats = []
    try:
        for num in nums:
            nums_floats.append(float(num))
    except Exception:
        print("Error! List of numbers is invalid")
    else:
        median = sort_and_find_median(nums_floats)
        print("The median is: " + str(median))

def sort_and_find_median(numbers: list[int]):
    numbers = sort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        return numbers[n//2]

def sort(numbers: list[int]):
    # The below sorting algorithm is merge sort

    if len(numbers) > 2:
        # Split the list into two halves
        left = numbers[:len(numbers)//2]
        right = numbers[len(numbers)//2:]

        # Recursively call sort on the two halves
        left = sort(left)
        right = sort(right)

        sorted_numbers = []

        # Merge the two halves
        left_index = 0
        right_index = 0
        for _ in range(len(numbers)):

            # if the right half is out of numbers then all that remains is the left half which have to be larger
            if right_index == len(right):
                sorted_numbers.append(left[left_index])
                left_index += 1

            # if the left half is out of numbers then all that remains is the right half which have to be larger
            elif left_index == len(left):
                sorted_numbers.append(right[right_index])
                right_index += 1

            # if neither side is out of numbers, then take the lowest between the two
            elif left[left_index] > right[right_index]:
                sorted_numbers.append(right[right_index])
                right_index += 1
            else:
                sorted_numbers.append(left[left_index])
                left_index += 1

        return sorted_numbers
    # If the list only has 2 elements we can simply check if they are out of order and fix them
    elif len(numbers) == 2:
        if numbers[0] > numbers[1]:
            return [numbers[1], numbers[0]]
    # If the list has less then 2 elements or has 2 but they are already in the correct order, we can simply return the list as it is already sorted
    return numbers

main()