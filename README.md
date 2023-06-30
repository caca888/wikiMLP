[![Makefile CI](https://github.com/caca888/MLportfolio/actions/workflows/makefile.yml/badge.svg)](https://github.com/caca888/MLportfolio/actions/workflows/makefile.yml)

## Portfolio Content
The repo is aim to indicate my personal understanding about DevOps, DataOps, and MLOps. All included contents are used for study purpose. 

The application includes the following user interfaces:
* Command Line Tool 
* Web Services
* Docker Container
according to the figure shown in the CI environment.

In particular, the following functionalities are available via the above user interfaces
* Wikipedia Searching: wikipedia summary about the searching term, ref to. [wikipedia library](https://pypi.org/project/wikipedia/)
* Key Word Extraction: key words extracted from the wikipedia summary, ref to. [text_blob library](https://textblob.readthedocs.io/en/dev/)
* Sentimental Analysis: sentimental analysis of the wikipedia summary, step 1 to limit summary content about the term, ref. to [text summary based on model facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) and in step 2 the summarized text will be analyzed by [sentimental analysis model cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)


## CI Environment

The app is aim to deploy CI pipeline in the Github Actions for the following functionalities, e.g.:
* Unit Test
* Lint Score
* Unified formatting of Code
* Setup Command Line Tool
* Installation of Dependencies
* Automatic Code Bulding
  
  
![CI Environment](/img/CI.PNG)
