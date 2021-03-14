# Auto-NLP

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Auto-NLP is a stack of open source NLP tools for devs and SEs to integrate into their projects. 

  - Plug N Play approach
  - Customizable
  - Highly accurate

### Tech

Dillinger uses a number of open source projects to work properly:

* [NLTK] - Standard NLP library
* [Stanza] - Alternative to Stanford NLP
* [python] - Pretty simple python

### Installation and Usage

Install the dependencies first.

```sh
from auto-nlp.aspect import main
answer = main("The UX is great but the support is poor.")
print(answer)
```



