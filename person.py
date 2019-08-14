from datetime import datetime
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

DOCUMENTS_SOFTWARE = {
    "Q93068": {
        "id": "Q93068",
        "software": [
            {
                "id": "E280",
                "documents": [
                    {
                        "document": { "doi": "https://doi.org/10.1093/pcp/pcg126", 
                                      "url": "",
                                      "sha1": ""}
                    }, 
                    {
                        "document": { "doi": "https://doi.org/10.1038/s41699-018-0076-0", 
                                      "url": "",
                                      "sha1": ""}
                    }
                ]
            },
            {
                "id": "Q8029",
                "documents": [
                    {
                        "document": { "doi": "https://doi.org/10.1038/s41699-018-0076-0", 
                                      "url": "",
                                      "sha1": ""}
                    }
                ]
            }
        ]
    }
}

def disambiguate(json_person_name):
    response = {
                "id": "Q93068",
                "conf": 0.96
    }
    response["date"] = get_timestamp()

    return response

def software(id):
    """
    This function responds to a request for /api/person/{id}/software
    with one matching id from all persons
    :param id:   identifier of the person to find
    :return:       lists the software entities having the person as author or co-author, 
                   and for each software the citing documents supporting the authorship
    """
    if id in SOFTWARE:
        soft = SOFTWARE.get(id)
        soft["date"] = get_timestamp()

    # otherwise nope
    else:
        abort(
            404, "Document with identifier {id} not found".format(id=id)
        )

    return soft

