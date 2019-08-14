import concurrent.futures
import requests
import pymongo
import sys
import os
import bz2
import itertools
import codecs
import argparse
import json

class KB_initializer(object):
    """
    This script will intialize the Knowledge Base:
    - create mongoDB database and collection
    - import relevant Wikidata entities (software, persons and organizations) into the KB

    A recent Wikidata dump is necessary.
    """

    def __init__(self, config_path='./config.json'):
        self.config = None
        self._load_config(config_path)
        self.mongo_db = None

        self._check_mongo()

        # list of valid entities (we might want to use a LMDB map)
        self.entities = []
        with open("resources/software.entities", "rt") as fp:
            for line in fp:
                self.entities.append(line.rstrip())

    def _check_mongo(self):
        # check if mongo is up and running
        try:
            if self.mongo_db is None:
                mongo_client = pymongo.MongoClient(self.config["mongo_host"], int(self.config["mongo_port"]))
                mongo_client.server_info() # force connection on a request 
                self.mongo_db = mongo_client[self.config["mongo_db"]]

                # create required collections if not available
                self.documents = self.mongo_db.documents
                self.organizations = self.mongo_db.organizations
                self.person = self.mongo_db.persons
                self.software = self.mongo_db.software

        except pymongo.errors.ServerSelectionTimeoutError as err:
            print("a mongo db instance does not appear to be available")
            print(err)

    def _load_config(self, path='./config.json'):
        """
        Load the json configuration 
        """
        config_json = open(path).read()
        self.config = json.loads(config_json)

    def import_wikidata(self, jsonWikidataDumpPath):
        if self.mongo_db is None:
            self._check_mongo()

        # read compressed dump line by line
        print(jsonWikidataDumpPath)
        with bz2.open(jsonWikidataDumpPath, "rt") as bzinput:
            bzinput.read(2) # skip first 2 bytes 
            for i, line in enumerate(bzinput):
                #if i == 1000: break
                entityJson = json.loads(line.rstrip(',\n'))
                if self._valid_entity(entityJson):
                    entityJson = self._simplify(entityJson)
                    #print(entityJson)
                    # store entity in mongo
                    inserted_id = self.mongo_db.software.insert_one(entityJson).inserted_id


    def _valid_entity(self, jsonEntity):
        """
        Filter out json wikidata entries not relevant to software. For this we use an external
        list of entities produced by entity-fishing, which has a full KB representation for 
        exploiting hierarchy of P31 and P279 properties. Wikidata identifiers are stable. 
        """
        if jsonEntity["id"] in self.entities:
            return True
        else:
            return False 

    def _simplify(self, jsonEntity):
        """
        As we process only English for the moment, we don't need other language labels 
        """
        _replace_element(jsonEntity, "labels", "en")
        _replace_element(jsonEntity, "descriptions", "en")
        _replace_element(jsonEntity, "aliases", "en")

        if 'sitelinks' in jsonEntity:
            del jsonEntity['sitelinks']

        return jsonEntity


def _replace_element(jsonEntity, element, lang):
    if element in jsonEntity:
        if lang in jsonEntity[element]:
            en_lab_val = jsonEntity[element][lang]
            en_lab = {}
            en_lab[lang] = en_lab_val
            jsonEntity[element] = en_lab
    return jsonEntity


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Intialize the Softcite Knowledge Base with relevant Wikidata entities")
    parser.add_argument("WikidataDumpPath", default=None, help="path to a complete Wikidata JSON dump file in bz2 format") 
    parser.add_argument("--config", default="./config.json", help="path to the config file, default is ./config.json") 

    args = parser.parse_args()
    config = args.config

    if args.WikidataDumpPath is not None:
        kb_initializer = KB_initializer(config)
        kb_initializer.import_wikidata(args.WikidataDumpPath)
    else:
        print("No Wikidata JSON dump file path indicated")