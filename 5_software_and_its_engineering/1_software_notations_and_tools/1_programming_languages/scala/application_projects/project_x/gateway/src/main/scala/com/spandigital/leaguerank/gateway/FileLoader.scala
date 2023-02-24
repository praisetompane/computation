package com.praisecapital.project_x.gateway

import com.praisecapital.project_x.model.{ModelA, ModelB}
import scala.util.{Try, Success, Failure}
import scala.io.Source
import scala.util.Using

object FileLoader {
  def loadFile(filename: String): List[String] =
    Using(Source.fromFile(filename)) { reader =>
      reader.getLines().toList
    } match {
      case Success(result) => result
      case Failure(e) =>
        println(
          s"An error occured loading file $filename."
        )
        throw e
    }
}
