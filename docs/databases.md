# Identifying existing curated resources on software

We can distinguish:
* Collaborative development platform (e.g. GitHub, GitLab, Bitbucket, ...), this is mostly where the actual software publication and development work takes place today
* Distribution/package systems (CPAN, CRAN, CTAN, PyPI, Maven Central, NPM, ...)
* Aggregator for software information (swMath, ASCL service, Papers with code, SciCrunch)
* Aggregator for software code and package (SoftwareHeritage, libraries.io, versioneye)
* Archive supporting software deposit (Zenodo, SoftwareHeritage)
* Tools supporing the collaborative development ecosystem: build/continuous integration service (travis, circleci, Jenkins, etc.), test coverage (coverall, codecov, etc.), image system (DockerHub), documentation (readthedoc), etc.
* Cloud-based computing infrastructure via Jupyter or Jupyter-style Notebooks environment: Google Colab, Azure Notebooks, Kaggle, Amazon Sagemaker, CoCalc, ...

which will be connected somehow to main scholarly services, e.g. for Open Access ones: 
* Scholar article repository (arXiv, bioRxiv, HAL, ...)
* Scholar article metadata aggregator/resolver (CrossRef, MAG)
* Data sharing repository (Zenodo, Dryad, figshare, etc. hundred others...)
* Discovery tools (Google Scholar, Semantic Scholar, Primo, Summons, ...)

- FDI Lab SciCrunch: scicrunch.org
curated research resources, including software, for identification and citation purposes

- https://libraries.io/
aggregator of software package objects
free API requests are subject to a 60/request/minute rate limit based on the api_key
data is CC-BY-SA
the tool itself is AGPL

- rOpenSci package manager
curated scientific R packages for maintenance, delivery, documentation, etc.
A must :)

API:
https://dev.ropensci.org/packages e
https://dev.ropensci.org/packages/magick/2.5.0.9000
https://dev.ropensci.org/stats/maintainers
https://dev.ropensci.org/stats/revdeps e
https://dev.ropensci.org/stats/sysdeps e
 
https://dev.ropensci.org/stats/checks
https://r-universe.dev/
Build, logs, registry are managed with GitHub Actions
via git submodules:
https://github.com/r-universe/ropensci
https://github.com/r-universe/hrbrmstr_gitlab.com

- swMath service for software in Mathematics with more than 30.000 curated entries

- ASCL service for software in Astrophysics with over 2.000 curated entries 

- Papers with code initiative in Machine Learning, with over 34.000 entries

- TAPoR 3 contains a list of 1500 curated software/tools in Digital Humanities, 
http://tapor.ca
see https://lehkost.github.io/tools-dh-proceedings/index.html 

- BioTools, tools in biomedicine, including databases, services, etc. https://bio.tools/
https://github.com/bio-tools
note: on covid-19 tools, https://bio.tools/t?domain=covid-19
(might be much more relevant around, Biocontainers, Bioconda, OpenEBench, Debian Med, BIII.eu, etc...)
(it uses keyphrase lookup to find tool mentions in PMC, see https://github.com/bio-tools/pub2tools)

- Zenodo lists some 44.000 software deposits (will be preserved in mirror at some point automatically at SoftwareHeritage)
They come from the Zenodo/GitHub integration
* but some appears to be data/dataset generated or used by by software
https://zenodo.org/record/4148730
* can be documentation on a software: https://zenodo.org/record/4053076
which leads to think that there is no curation. Many GitHub repo correspond to data or documentation, which might impact the Zenodo/GitHub integration.

In Zenodo, each version have an independent entry/deposit, but these entries are grouped when related to the same software, e.g.
https://zenodo.org/search?page=1&size=20&q=conceptrecid:4070073&all_versions&sort=-version
(note: by default the versions are conflated apparently in search result display)
it means -> 44.000 software and 101.000 versions, given that software and versions have each a distinct DOIs, we are in the range of 150.000 DOIs

REST API 
https://developers.zenodo.org/#rest-api
+ OAI-PMH service for harvesting
https://developers.zenodo.org/#oai-pmh

Zenodo metadata is CC-0 license

Lot's of orcid ID and some actual paper citation in the markdown description of the deposit.

- metadata/interoperability
https://codemeta.github.io/

This project provides a schema for describing software metadata and mapping for metadata available in WikiData, DataCite, 
some package format (maven, debian, npm, R, ruby gems), and GitHub

- list of programming languages

https://foldoc.org/source.html

Bill Kinnersley computer language list (2500)
https://web.archive.org/web/20160506170543/http://people.ku.edu/~nkinners/LangList/Extras/langlist.htm

https://hopl.info/ 
(Do not copy, do not reproduce!)

- Open Source Sofware licenses

https://libraries.io/licenses


