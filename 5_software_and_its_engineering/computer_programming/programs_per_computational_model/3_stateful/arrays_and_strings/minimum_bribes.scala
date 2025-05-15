import Math.abs

/*
    tooChaotic = number cannot be in index greater thsn (the number - 2)

    isNumberInOriginalPosition? // index == number
      Yes, add 0 to bribes
      Else if tooChaotic, print too too chaotic
      Else, increment bribes by (the number - current position)

      1 2 3 4 5 6 7 8
      1 2 5 3 4 6 7 8
      1 2 5 3 7 8 4 6
      1 2 5 3 7 8 6 4

      5 3 4
      1 2 5 3 4 6 7 8

      7 6 4
      1 2 5 3 7 4 6 8

      8 6 4
      1 2 5 3 7 8 4 6

      6 4
      1 2 5 3 7 8 6 4

      5 - 3 = 2

      3 - 4 = -1

      7 - 5 = 2
      8 - 6 = 2

      6 - 7 = - 1


 */

// 2 2 8
def minimumBribes(q: Array[Int]) =
    calculateNumberOfBribes(q.toList.zipWithIndex, 0).getOrElse("Too chaotic")

    def calculateNumberOfBribes(q: List[(Int, Int)], total: Int): Option[Int] =
        q match {
            case head :: tail if (isNumberInIllegalPosition(head)) => None
            case head :: tail if (isNumberInOriginalPosition(head)) =>
                calculateNumberOfBribes(tail, total)
            case head :: tail if (!isNumberInOriginalPosition(head)) =>
                calculateNumberOfBribes(
                  tail,
                  total + calculateNumbersBribe(head)
                )
            case Nil => Some(total)
        }

    def isNumberInOriginalPosition(numberAndPosition: (Int, Int)) =
        numberAndPosition match {
            case (number, index) =>
                number == adjustArrayIndexToNaturalNumber(index)
        }

    def isNumberInIllegalPosition(numberAndPosition: (Int, Int)) =
        val maxBribes = 2
        val isIllegal = numberAndPosition match {
            case (number, index) =>
                number - adjustArrayIndexToNaturalNumber(index) > maxBribes
        }
        println(numberAndPosition._1 + " " + isIllegal)
        isIllegal

    def adjustArrayIndexToNaturalNumber(index: Int) = index + 1

    // NOT good enough for 6 - 7
    def calculateNumbersBribe(numberAndPosition: (Int, Int)) =
        val totalBribes = numberAndPosition match {
            case (number, index) =>
                number - adjustArrayIndexToNaturalNumber(index)
        }
        if (totalBribes < 0) 0
        else totalBribes

@main def main(): Unit =
    val q = Array(1, 2, 5, 3, 7, 8, 6, 4)

    // Array(2,1,5,3,4)
    println(minimumBribes(q))
