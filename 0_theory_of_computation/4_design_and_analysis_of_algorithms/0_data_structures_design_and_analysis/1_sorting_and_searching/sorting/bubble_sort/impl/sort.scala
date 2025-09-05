def sort(list: List[Int]): List[Int] = {
    def sort(
        highest_numbers: List[Int],
        sorted: List[Int]
    ): List[Int] =
        if (highest_numbers.isEmpty) sorted
        else bubble(highest_numbers, Nil, sorted)

    def bubble(
        highest_numbers: List[Int],
        unsorted: List[Int],
        sorted: List[Int]
    ): List[Int] = highest_numbers match {
        case first_num :: second_num :: remaining_list =>
            if (first_num > second_num)
                bubble(
                  first_num :: remaining_list,
                  second_num :: unsorted,
                  sorted
                )
            else
                bubble(
                  second_num :: remaining_list,
                  first_num :: unsorted,
                  sorted
                )
        case first_num :: Nil => sort(unsorted, first_num :: sorted)
        case Nil              => Nil
    }
    sort(list, Nil)
}

@main def main(): Unit =
    assert(sort(List(4, 2, 3, 1, 5)) == List(1, 2, 3, 4, 5))
    assert(sort(List(1, 2, 3, 4, 5)) == List(1, 2, 3, 4, 5))
    assert(sort(List(5, 4, 3, 2, 1)) == List(1, 2, 3, 4, 5))
    assert(sort(List()) == List())
