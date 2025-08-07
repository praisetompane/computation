"""
  Source: https://www.hackerrank.com/challenges/birthday-cake-candles/copy-from/71884152
"""
def count_largest_object_occurrence(ar: Array[Int]): Int =
    val max_height = if (ar.length == 0) 0 else ar.reduceLeft(_ max _)
    ar.count(x => x == max_height)

@main
def main(): Unit =
    assert(count_largest_object_occurrence(Array(3, 2, 1, 3)) == 2)

    assert(
      count_largest_object_occurrence(
        Array(3, 2, 1, 3, 7, 7, 7, 1, 2, 5, 3, 3, 5, 2, 1)
      ) == 3
    )

    assert(
      count_largest_object_occurrence(Array(3, 2, 1)) == 1
    )

    assert(count_largest_object_occurrence(Array()) == 0)
    assert(count_largest_object_occurrence(Array(1)) == 1)
    assert(count_largest_object_occurrence(Array(1, 2)) == 1)

    println("completed successfully")
