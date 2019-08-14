# Softcite REST API

This is server exposing a REST API for the softcite Software Knowledge Base. 

The softcite Software Knowledge Base is built on top Wikidata existing resources. 

## Requirements

The client has been tested with Python 3.5. 

A MongoDB server version 3.* must be installed and started. 

## Install

> cd grobid/software-mention/python/

It is advised to setup first a virtual environment to avoid falling into one of these gloomy python dependency marshlands:

> virtualenv --system-site-packages -p python3 env

> source env/bin/activate

Install the dependencies, use:

> pip3 install -r requirements.txt

An instance of MongoDB version 3.* needs to be installed. 

### Configuration

In the configuration file `config.json`, the host, port and application db name of the MongoDB instance need to be provided. You can also set the port of the service. 

```json
{
    "service_port": "5000",
    "mongo_host": "localhost",
    "mongo_port": "27017",
    "mongo_db": "softcite"
}
```

## Usage and options

### Init the Knowledge Base

The Softcite Knowledge Base uses Wikidata for importing common knowlegde around software. Entities corresponding to software (except video games) are imported to seed the KB, together with some relevant entities in relation to software corresponding to persons, organizations and close concepts (programming language, OS, license). 

You will need first a recent full Wikidata json dump compressed with bz2 (which is more compact), which can be dowloaded [here](https://dumps.wikimedia.org/wikidatawiki/entities/). There is no need to uncompressed the json dump.

Then for launching this initialization:

> python3 kb_init.py path_to_the_wikidata_dump_with_extension_json.bz2


### Start the service

> python3 service.py 

The swagger documentation/console of the web services is then available at: http:// **service_host** : **service_port** /api/ui/, e.g, http://localhost:5000/api/ui/.


### Populate the database with extraction realized by the software-mention recognizer

This process need to be done by the software-mention recognizer client available at https://github.com/impactstory/software-mentions under `client/`, see the [documentation](https://github.com/impactstory/software-mentions/client/Readme.md). 

The client will further feed the Knowledge Base with new software mentions via the API, and create new software, document, person, and organization entities. The new entities have identifiers prefixed with letter `E` (in contrast to entities existing in Wikidata which remains prefixed by `Q`). Software citations found in documents are added to the software entities after disambiguation as additional statements. 

### Exporting the augemented KB in Wikidata json format

TBD

## License and contact

Distributed under [Apache 2.0 license](http://www.apache.org/licenses/LICENSE-2.0). The dependencies used in the project are either themselves also distributed under Apache 2.0 license or distributed under a compatible license. 

Main author and contact: Patrice Lopez (<patrice.lopez@science-miner.com>)


