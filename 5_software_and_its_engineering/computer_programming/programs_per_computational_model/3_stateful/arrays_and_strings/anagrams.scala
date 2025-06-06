def makeAnagrams(a: String, b: String, deletions: Int): Int =

    def checkLetter(letter: Char, subject: String, comp: String) =
        val subjectOccurrence = subject.count(_ == letter)
        val compOccurrence = comp.count(_ == letter)
        val deletions = math.abs(subjectOccurrence - compOccurrence)

        if (subjectOccurrence > compOccurrence) {
            (subject.diff(letter.toString * deletions), comp, deletions)
        } else if (subjectOccurrence < compOccurrence) {
            (subject, comp.diff(letter.toString * deletions), deletions)
        } else (subject, comp, deletions)

    def areAnagrams(a: String, b: String) = a.sorted == b.sorted

    if (areAnagrams(a, b)) deletions
    else {
        val stringAChanges = a.map { letter =>
            {
                val changed = checkLetter(letter, a, b)
                if (areAnagrams(changed._1, changed._2)) changed._3
                else changed._3
            }
        }
        val stringBChanges = b.map { letter =>
            {
                val changed = checkLetter(letter, b, a)
                if (areAnagrams(changed._1, changed._2)) changed._3
                else changed._3
            }
        }
        stringAChanges.sum + stringBChanges.sum
    }

@main def main() =
    val a = "bacdc"
    val b = "dcfezq"
    println(makeAnagrams(a, b, 0))
