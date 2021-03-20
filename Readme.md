# Auto-NLP

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://pypi.org/project/auto-nlp/)

Auto-NLP is a stack of open source NLP tools for devs and SEs to integrate into their projects. 

  - Plug N Play approach
  - Customizable
  - Highly accurate

# Installation
```sh
pip install auto-nlp==0.40
```

### Tech

auto-nlp uses a number of open source projects to work properly:

* [NLTK] - Standard NLP library
* [Stanza] - Alternative to Stanford NLP
* [python] - Pretty simple python
* [Tensorflow] - Google's AI Enginer
* [Transformers] - HuggingFace's original NLP library

### Installation and Usage

Install the dependencies first.

```sh
from auto-nlp.sen_analysis import sentiment
answer = sentiment("The UX is great but the support is poor.", "analyze using transformers")
print(answer)
```



