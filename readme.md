**WARNING**: 
- This is a vulernable & buggy code repo. 
- Primary use of this code is for testing the secrets detection tool & vulnerable open-source deps detection tool. 


It's a very simple code that fetches top 10a joke via the `https://sv443.net/jokeapi/v2/` API and displays it in a flask webserver along with timestamp. It also logs the details in a SQL-lite database. 

There is not much UI or any other fancy stuff involved here.

It uses pipenv for package management. (RealPython has a good getting started guide for pipenv)

Check the pipfile for specific versionof libraries used. 

Known vulnerabilities:
- Requests library 2.1: https://www.cvedetails.com/vulnerability-list/vendor_id-10210/product_id-29258/Python-Requests.html
- Flask library 1.1.4: https://snyk.io/vuln/pip:flask


To run the dockerfile, `docker build -t sample_py_proj:1 -f Dockerfile .`





