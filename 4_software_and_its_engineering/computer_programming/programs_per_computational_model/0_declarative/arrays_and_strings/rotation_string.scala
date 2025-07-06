import io.Source.stdin
import scala.annotation.tailrec

/*
    Objective:
        given a string, return all possible rotations

    Constraints:
        0 <= T <= 10
        0 <= n <= 10^2
    Performance:
        Time:
            T = number of test cases
            n = length of each string
            O(T * n)

    Source: https://www.hackerrank.com/challenges/rotate-string/copy-from/324543244
 */

def rotate(input: String): String =
    @tailrec
    def _rotate(rotations: Int, rotated: String, output: String): String =
        if (rotations <= 0) output
        else {
            val _rotated = rotated.appended(rotated(0)).drop(1)
            _rotate(rotations - 1, _rotated, output ++ _rotated ++ " ")
        }
    _rotate(input.length(), input, "").trim()

@main def main(): Unit =
    println(rotate("abc"))
    assert(rotate("abc").==("bca cab abc"))
