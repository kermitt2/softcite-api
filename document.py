from datetime import datetime
from flask import make_response, abort
import json

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

DOCUMENTS_MENTIONS = {
    "10.1002/blabla": {
        "id": "10.1002/blabla",
        "mentions": [
            {
                "type": "software",
                "software-name": {
                    "rawForm": "ImagePro Plus",
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
                    "rawForm": "Media Cybernetics, Silver Spring, \nU.S.A.",
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
            }
        ],
        "pages": [ {"page_height":842.0, "page_width":595.0}, {"page_height":842.0, "page_width":595.0} ]
    }
}

DOCUMENTS_SOFTWARE = {
    "10.1002/blabla": {
        "id": "10.1002/blabla",
        "software": [
            {
                "id": "E280",
                "conf": 0.9761
            },
            {
                "id": "Q8029",
                "conf": 0.7130
            }
        ]
    }
}

SOFTWARE_RELATEDNESS = {
    "10.1002/blabla": {
        "id": "10.1002/blabla",
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

def read_one_mentions(id):
    """
    This function responds to a request for /api/document/{id}/mentions
    with one matching id from all documents
    :param id:   identifier of the document to find
    :return:       software mentions occurring in the document
    """
    print('id', id)
    if id in DOCUMENTS_MENTIONS:
        doc = DOCUMENTS_MENTIONS.get(id)
        print(doc)
        doc["date"] = get_timestamp()
        r = json.dumps(doc)
        print(r)
    # otherwise nope
    else:
        abort(
            404, "Document with identifier {id} not found".format(id=id)
        )

    return doc


def read_one_software(id):
    """
    This function responds to a request for /api/document/{id}/software
    with one matching id from all documents
    :param id:   identifier of the document to find
    :return:       software entity occurring in the document
    """
    if id in DOCUMENTS_SOFTWARE:
        doc = DOCUMENTS_SOFTWARE.get(id)
        doc["date"] = get_timestamp()

    # otherwise nope
    else:
        abort(
            404, "Document with identifier {id} not found".format(id=id)
        )

    return doc

def nbest_software(id):
    """
    This function responds to a request for /api/document/{id}/software/related:
    with one matching id from all documents
    :param id:   identifier of the document to find
    :return:       list of n-best software related to the document matching the identifier but NOT mentioned in the document
    """
    if id in SOFTWARE_RELATEDNESS:
        doc = SOFTWARE_RELATEDNESS.get(id)
        doc["date"] = get_timestamp()

    # otherwise nope
    else:
        abort(
            404, "Software entity with identifier {id} not found".format(id=id)
        )

    return doc

def disambiguate(json_document_metadata):
    """
    This function responds to a POST request for /api/document/disambiguate:
    :param json_document_metadata:   the json metadata object of the document to be disambiguated
    :return:       the disambiguated identifier for the document, associated to a confidence score 
    """
    response = {
                "id": "10.1002/blabla",
                "conf": 0.96
    }
    response["date"] = get_timestamp()

    return response

def add(json_object):
    """
    This function responds to a POST request for /api/document:
    :param json:    the json object as produced by the software mention recognizer when producing a full document  
    """
    response = {}
    response["date"] = get_timestamp()

    return response

    
def delete(json_object):
    """
    This function responds to a POST request for /api/document:
    :param json:    the json object as produced by the software mention recognizer when producing a full document  
    """
    response = {}
    response["date"] = get_timestamp()

    return response
    