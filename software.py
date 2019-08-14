from datetime import datetime
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

SOFTWARE = {
    "Q8029" : {
        "id": "Q8029",
        "labels": {"en": {"language": "en", "value": "BibTeX"}}, 
        "descriptions": {"en": {"language": "en", "value": "reference management software for formatting lists of references"}},
        "aliases": [],
        "claims": {"P31": [{"datatype":"wikibase-item", "datavalue": {"value": "Q7397"}},      # instance of software 
                           {"datatype":"wikibase-item", "datavalue": {"value": "Q18616720"}}], # instance of bibliographic data format 
                   "P178": [{"datatype":"wikibase-item", "datavalue": {"value": "Q93068"}}],   # developer is Q93068 (Oren Patashnik) 
                   "P856": [{"datatype":"url", "datavalue": {"value": "https://www.ctan.org/pkg/bibtex"}}] # url 
                  }
        }
    }

CITATIONS = {
    "Q8029": {
        "id": "Q8029",
        "citations": [ {
            "document": { "doi": "https://doi.org/10.1093/pcp/pcg126", 
                          "url": "",
                          "sha1": ""},
            "mentions": [{
                "type": "software",
                "id": "Q8029",
                "conf": 0.9511,
                "software-name": {
                    "rawForm": "bibtex",
                    "offsetStart": 351,
                    "offsetEnd": 364,
                    "boundingBoxes": [{
                        "p": 8,
                        "x": 118.928,
                        "y": 461.363,
                        "w": 49.98600000000002,
                        "h": 7.749360000000024
                    }]
                },
                "creator": {
                    "rawForm": "O. Patashnik",
                    "offsetStart": 366,
                    "offsetEnd": 407,
                    "boundingBoxes": [{
                        "p": 8,
                        "x": 175.37953333333334,
                        "y": 461.363,
                        "w": 115.15626666666665,
                        "h": 7.749360000000024
                    }, {
                        "p": 8,
                        "x": 48.5996,
                        "y": 471.623,
                        "w": 21.192299999999996,
                        "h": 7.749360000000024
                    }]
                }
            }]
        }, 
        {
            "document": { "doi": "https://doi.org/10.1038/s41699-018-0076-0", 
                          "url": "",
                          "sha1": ""},
            "mentions": [{
                "type": "software",
                "id": "Q8029",
                "conf": 0.7719,
                "software-name": {
                "rawForm": "BibTeX",
                "offsetStart": 113,
                "offsetEnd": 135,
                "boundingBoxes": [{
                    "p": 8,
                    "x": 271.854,
                    "y": 363.347,
                    "w": 125.13299999999998,
                    "h": 13.283999999999992
                }]
            },
            }]
        }
        ]
    }
}

DOCUMENTS = {
    "Q8029": {
        "id": "Q8029",
        "documents": [ 
            {
                "document": { "doi": "https://doi.org/10.1093/pcp/pcg126", 
                              "url": "",
                              "sha1": ""},
                "relevance": 0.95
            }, 
            {
                "document": { "doi": "https://doi.org/10.1038/s41699-018-0076-0", 
                              "url": "",
                              "sha1": ""},
                "relevance": 0.89
            }
        ]
    }
}

SOFTWARE_RELATEDNESS = {
    "Q8029": {
        "id": "Q8029",
        "software": [
            {
                "id": "Q5310",
                "relatedness": 0.9761
            },
            {
                "id": "Q226915",
                "relatedness": 0.7130
            }
        ]
    }
}

def read_one(id):
    """
    This function responds to a request for /api/software/{id}
    with one matching id from all software entities
    :param id:   identifier of the software entity to find
    :return:       software entity matching the identifier
    """
    if id in SOFTWARE:
        soft = SOFTWARE.get(id)
        soft["date"] = get_timestamp()

    # otherwise nope
    else:
        abort(
            404, "Software entity with identifier {id} not found".format(id=id)
        )

    return soft

def read_citations(id):
    """
    This function responds to a request for /api/software/{id}/citations
    with one matching id from all software entities
    :param id:   identifier of the software entity to find
    :return:       all the citations to the software entity matching the identifier
    """
    if id in CITATIONS:
        soft = CITATIONS.get(id)
        soft["date"] = get_timestamp()

    # otherwise nope
    else:
        abort(
            404, "Software entity with identifier {id} not found".format(id=id)
        )

    return soft

def disambiguate(json_mention):
    response = {
                "id": "Q8029",
                "conf": 0.96
    }
    response["date"] = get_timestamp()

    return response


def nbest_documents(id):
    """
    This function responds to a request for /api/software/{id}/documents:
    with one matching id from all software entities
    :param id:   identifier of the software entity to find
    :return:       list of n-best documents related to the software entity matching the identifier
    """
    if id in DOCUMENTS:
        soft = DOCUMENTS.get(id)
        soft["date"] = get_timestamp()

    # otherwise nope
    else:
        abort(
            404, "Software entity with identifier {id} not found".format(id=id)
        )

    return soft

def nbest_software(id):
    """
    This function responds to a request for /api/software/{id}/related:
    with one matching id from all software entities
    :param id:   identifier of the software entity to find
    :return:       list of n-best software related to the software entity matching the identifier
    """
    if id in SOFTWARE_RELATEDNESS:
        soft = SOFTWARE_RELATEDNESS.get(id)
        soft["date"] = get_timestamp()

    # otherwise nope
    else:
        abort(
            404, "Software entity with identifier {id} not found".format(id=id)
        )

    return soft
    
def delete(json_object):
    """
    This function responds to a POST request for /api/document:
    :param json:    the json object as produced by the software mention recognizer when producing a full document  
    """
    response = {}
    response["date"] = get_timestamp()

    return response



'''
          example:  
            wikidata_identifier:
              value: Q8029
              summary: identifier for a software entity already in Wikidata
            non_wikidata_identifier:
              value: E280
              summary: identifier for a software entity not already in Wikidata

'''