//only works for positive integers
const has_duplicates_linear = (arr) => {
    number_exists = []

    for (i = 0; i < arr.length; i++) {
        if (number_exists[arr[i]] == undefined) {
            number_exists[arr[i]] = 1
        }
        else {
            return true;
        }
    }
    return false;
}

console.log(has_duplicates_linear([1, 2, 3, 4, 5, 7, 8]))


const has_duplicates_polynomial = (arr) => {
    for (i = 0; i < arr.length; i++) {
        for (j = 0; j < arr.length; j++) {
            if (i != j && arr[i] == arr[j]) {
                return true;
            }
        }
    }
    return false;
}

console.log(has_duplicates_polynomial([1, 2, 3, 4, 5, 7, 8]))