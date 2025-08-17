import scala.io.StdIn
import scala.collection.mutable.ListBuffer

trait Queue {
    def put(value: Int): Unit

    def pop(): Unit
}

class QueueImpl extends Queue {
    private val data = ListBuffer[Int]()

    def put(value: Int): Unit = data.append(value)

    def pop: Unit = data.remove(0)

    def peek: Int = data(0)

}

object QueryType {
    val Enqueue = "1"
    val Dequeue = "2"
    val PrintFrontElement = "3"
}

object Solution {

    def main(arg: Array[String]): Unit =
        val numberOfQueries = StdIn.readLine.trim.toInt
        val queue = new QueueImpl()
        val queries = { 1 to numberOfQueries }.toList

        queries.foreach { x =>
            val queryString = StdIn.readLine.split(" ")
            val query = queryString(0)
            val enqueueValue =
                if (queryString.length > 1) queryString(1).toInt
                else 0 // be careful here

            if (query == QueryType.Enqueue) queue.put(enqueueValue)
            else if (query == QueryType.Dequeue) queue.pop()
            else println(queue.peek)
        }
}
