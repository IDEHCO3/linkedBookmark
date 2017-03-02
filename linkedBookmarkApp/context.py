
def addContextInHeader(url, response):
    link = ' <'+url+'>; rel=\"http://www.w3.org/ns/json-ld#context\"; type=\"application/ld+json\"'
    if "Link" not in response:
        response['Link'] = link
    else:
        response['Link'] += ", " + link
    return response

LinkedBookmarkResourceContext = {
    "@context": {
        "name": {
            "@id": "http://schema.org/name",
            "@type": "http://schema.org/text"
        },
        "description": {
            "@id": "http://schema.org/description",
            "@type": "http://schema.org/text"
        }
    }
}

LinkedBookmarkItemResourceContext = {
    "@context": {
        "name": {
            "@id": "http://schema.org/name",
            "@type": "http://schema.org/text"
        },
        "description": {
            "@id": "http://schema.org/description",
            "@type": "http://schema.org/text"
        },
        "iri": {
            "@id": "http://schema.org/url",
            "@type": "@id"
        }
    }
}