- CRAN

Metadata
--------

https://cran.r-project.org/web/packages/knitr/
(other tools/API listed below)

downloads
---------

https://cranlogs.r-pkg.org/
for example: https://cranlogs.r-pkg.org/downloads/daily/1900-01-01:2020-01-01/knitr

the download database:
https://github.com/r-hub/cranlogs.app

- MetaCRAN

https://github.com/cran
https://www.r-pkg.org/services

API: https://www.r-pkg.org/services#api

Dependencies
------------

"reverse" dependencies
https://cran.r-project.org/web/packages/knitr/

for other dependencies:

- Google BigQuery's GitHub Archive
https://bigquery.cloud.google.com/table/githubarchive:github.timeline

- build yourself a dependency graph by parsing pachage information
extracted lines that included the words "library" or "requires" from files that end in R and R/Sweave/knitr filename extensions...
see https://github.com/ourresearch/depsy/blob/master/models/github_repo.py

Other links

General commercial tools to track dependencies:

- free (API requests are subject to a 60/request/minute rate limit based on the api_key)
https://libraries.io/
warning: the tool itself is AGPL

- commercial
https://www.versioneye.com/

https://mran.revolutionanalytics.com/packages

Also:

software-heritage preserves open source repositories, and offer an API to browse the archive with versioning and some metadata information
https://archive.softwareheritage.org/api/
(at this stage, it does not track dependencies)
warning: the tool itself is AGPL

see also:
https://librestats.com/2012/05/17/visualizing-the-cran-graphing-package-dependencies/
https://www.r-bloggers.com/2015/08/differences-in-the-network-structure-of-cran-and-bioconductor/


