lazy val root = (project in file(".")).
    settings(
        inThisBuild(List(
            organization := "com.praise",
            scalaVersion := "2.13.6"
        )),
        name := "learn-scala"
    )

libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.9" % Test
