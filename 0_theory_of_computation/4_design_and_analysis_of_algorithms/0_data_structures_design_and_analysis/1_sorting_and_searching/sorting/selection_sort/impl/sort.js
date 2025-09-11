const sort = (arr) => {
    last_index = arr.length - 1;
    sorted = false
    min_so_far_index = 0;
    unsorted_start_index = 0;
    swaps = 0;
    while (!sorted) {
        sorted = true;
        for (i = unsorted_start_index; i < last_index; i++) {
            if (arr[min_so_far_index] > arr[i + 1]) {
                min_so_far_index = i + 1;
                sorted = false;
            }
        }
        if (min_so_far_index != unsorted_start_index) {
            temp = arr[unsorted_start_index];
            arr[unsorted_start_index] = arr[min_so_far_index];
            arr[min_so_far_index] = temp;
            swaps++;
        }
        unsorted_start_index++;
    }
    console.log(swaps)
    return arr;
}