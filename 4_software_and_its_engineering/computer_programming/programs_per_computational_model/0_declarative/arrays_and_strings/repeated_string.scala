import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

/*
Source: https://www.hackerrank.com/challenges/repeated-string/
*/

object Solution {
    def repeatedString(s: String, n: Long): Long = {
        if (s == "a") n
        else {
            val length = s.length
            val letter_a_occurrence_in_base_patten = s.count(l => l == 'a')
            val projected_whole_base_pattern_occurrence = n / length
            val letter_a_occurrence_in_remaining_string =
                s.substring(0, (n % length).toInt).count(l => l == 'a')
            projected_whole_base_pattern_occurrence * letter_a_occurrence_in_base_patten + letter_a_occurrence_in_remaining_string
        }
    }
}
