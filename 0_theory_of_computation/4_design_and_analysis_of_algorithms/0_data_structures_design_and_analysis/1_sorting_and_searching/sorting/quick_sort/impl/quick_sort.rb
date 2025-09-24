class SortableArray
    attr_reader :array

    def initialize(array)
        @array = array
    end

    #numbers less than pivot to the left of the pivot
    #numbers greater than pivot to the right of the pivot
    def partition!(left_pointer, right_pointer)
        pivot_position = right_pointer
        pivot = @array[pivot_position]

        right_pointer -= 1

        while true do
            while @array[left_pointer] < pivot do
                left_pointer += 1
            end
            while @array[right_pointer] > pivot do
                right_pointer -= 1
            end
            if left_pointer >= right_pointer
                break
            end
            swap(left_pointer, right_pointer)
        end
        swap(left_pointer, pivot_position)
        return left_pointer
    end

    private def swap(pointer_1, pointer_2)
        temp = @array[pointer_1]
        @array[pointer_1] = @array[pointer_2]
        @array[pointer_2] = temp
    end

    #works because the partition method always puts the pivot in the correct sorted place
    #we just keep placing the pivot in the right place in the sub arrays
    #brilliant!!!
    def quicksort!(left_index, right_index)
        if right_index - left_index <= 0
            return
        end

        pivot_position = partition!(left_index, right_index)
        quicksort!(left_index, pivot_position - 1)
        quicksort!(pivot_position + 1, right_index)
    end

    def quickselect!(index, left_index, right_index)
        if right_index - left_index <= 0
            return @array[index]
        end

        pivot_position = partition!(left_index, right_index)
        if index < pivot_position
            quickselect!(index, left_index, pivot_position - 1)
        else
            quickselect!(index, pivot_position + 1, right_index)
        end
    end
end

array = [1, 2, 17, 16, 11, 15]
sortable_array = SortableArray.new(array)
sortable_array.quicksort!(0, array.length - 1)
puts "quick selected value #{sortable_array.quickselect!(2, 0, array.length - 1)}"
puts sortable_array.array
