package greeter

object DynamicWorkSheet {;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(86); 
  println("Welcome to the Scala worksheet");$skip(12); 
  val x = 5;System.out.println("""x  : Int = """ + $show(x ));$skip(34); 
  
  def increase(i: Int) = i + 1;System.out.println("""increase: (i: Int)Int""");$skip(17); val res$0 = 
  
  increase(x);System.out.println("""res0: Int = """ + $show(res$0))}
}

                                         