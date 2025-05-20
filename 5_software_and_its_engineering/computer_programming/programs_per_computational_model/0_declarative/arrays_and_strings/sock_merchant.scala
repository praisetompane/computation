import java.io._
import java.math._
import java.security._
import java.text._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

object Solution {

    //numberGroup = group the same number
    /*
        if numberGroup is even, add numberGroup/2 to pairs
        else
            val evenCount= find highest even number of elements
            add eventCount/2 to pairs
    */

    def sockMerchant(n: Int, ar: Array[Int]): Int = {
        val numberGroups = ar.groupBy(a => a)
        countPairs(0, numberGroups.toList)
    }

    private def countPairs(pairs: Int, 
                           numberGroups: List[(Int, Array[Int])]): Int = 
    numberGroups match {
        case n if n.isEmpty => pairs
        case head :: tail if isEven(head._2.length) => 
            countPairs(pairs + head._2.length/2, tail)
        case head :: tail if !isEven(head._2.length) =>
            countPairs(pairs + findClosestEvenNumber(head._2.length)/2, tail)
    }

    private def findClosestEvenNumber(number: Int): Int = {
      if(number % 2 == 0) number
      else findClosestEvenNumber(number - 1)
    }

    private def isEven(number: Int) = number%2 == 0
    
    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))

        val n = stdin.readLine.trim.toInt

        val ar = stdin.readLine.split(" ").map(_.trim.toInt)
        val result = sockMerchant(n, ar)

        printWriter.println(result)

        printWriter.close()
    }
}
