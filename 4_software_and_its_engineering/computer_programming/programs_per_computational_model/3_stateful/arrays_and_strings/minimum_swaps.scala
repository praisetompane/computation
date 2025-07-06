import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

object Solution {

    /*
        Objective:
            Return minimum bribes
                to generate current queue state
            Or "Too chaotic" if it's not possible

        Constraints:
            MaxBribes = 2
            People at the back bribe ones infront
                No backwards bribing
            Initial array was 1,2...

        Input:
            final state of the array

        Algo:
            bribes = 0
            for each value
                bribesUsed = abs(value - currentIndex)
                if(bribesUsed > MaxBribes) println("too chaotic")
                else bribes += bribesUsed
    */

    def minimumBribes(finalQueue: Array[Int]): Unit = {
        val MaxBribes = 2
        val finalIndex = finalQueue.length - 1
        var bribes = 0
        var swapped = true
        val zeroIndexOffset = 1

        def swap(indexA: Int, indexB: Int) = {
            val tempB = finalQueue(indexB)
            finalQueue(indexB) = finalQueue(indexA)
            finalQueue(indexA) = tempB
        }

        while(swapped) {
            swapped = false
            finalQueue.zipWithIndex.foreach {
                case(value: Int, index: Int) => 
                    val nextIndex = index + 1
                    val distanceFromOriginalPosition = math.abs(value - (index + zeroIndexOffset))

                    if(value > index && distanceFromOriginalPosition > MaxBribes) {
                        println("Too chaotic")
                        return
                    }

                    if(index != finalIndex && value > finalQueue(nextIndex)) {
                        swapped = true
                        bribes += 1
                        swap(index, nextIndex)
                    }
            }
        }

        println(bribes)
    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val t = stdin.readLine.trim.toInt

        for (tItr <- 1 to t) {
            val n = stdin.readLine.trim.toInt

            val q = stdin.readLine.split(" ").map(_.trim.toInt)
            minimumBribes(q)
        }
    }
}
