% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/parameter.R
\name{parameter}
\alias{parameter}
\title{Assign parameter to the flow}
\usage{
parameter(
  flow,
  parameter,
  required = FALSE,
  help = NULL,
  separator = NULL,
  default = NULL,
  type = NULL,
  is_flag = FALSE
)
}
\arguments{
\item{flow}{metaflow object}

\item{parameter}{name of the parameter}

\item{required}{logical (defaults to FALSE) denoting if
parameter is required as an argument to \code{run} the flow}

\item{help}{optional help text}

\item{separator}{optional separator for string parameters.
Useful in defining an iterable as a delimited string inside a parameter}

\item{default}{optional default value of the parameter}

\item{type}{optional type of the parameter}

\item{is_flag}{optional logical (defaults to FALSE) flag to denote is_flag}
}
\description{
\code{parameter} assigns variables to the flow that are
automatically available in all the steps.
}
\section{Usage}{

\preformatted{
parameter("alpha", help = "learning rate", required = TRUE)
parameter("alpha", help = "learning rate", default = 0.05)
}
}

