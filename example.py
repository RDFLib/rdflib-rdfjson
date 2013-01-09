from rdflib import Graph, plugin, Namespace
from rdflib.parser import Parser
from rdflib.serializer import Serializer

plugin.register("rdf-json", Parser,
   "rdflib_rdfjson.rdfjson_parser", "RdfJsonParser")

plugin.register("rdf-json", Serializer,
    "rdflib_rdfjson.rdfjson_serializer", "RdfJsonSerializer")

plugin.register("rdf-json-pretty", Serializer,
    "rdflib_rdfjson.rdfjson_serializer", "PrettyRdfJsonSerializer")


testrdfjson = '''{
  "http://example.org/about" :
    {
       "http://purl.org/dc/elements/1.1/title": [
            { "type" : "literal" , "value" : "Anna's Homepage." }
        ]
    }
}'''

g = Graph()
g.bind("dc", "http://purl.org/dc/elements/1.1/")
g.parse(data=testrdfjson, format="rdf-json")
rdfxml = g.serialize(format="xml")
assert '''Anna's Homepage''' in rdfxml

print(rdfxml)
print("""<?xml version="1.0" encoding="UTF-8"?>
<rdf:RDF
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
>
  <rdf:Description rdf:about="http://example.org/about">
    <dc:title>Anna's Homepage.</dc:title>
  </rdf:Description>
</rdf:RDF>""")

testrdfn3 = '''
<http://example.org/about>
    <http://purl.org/dc/elements/1.1/title>
   "Anna's Homepage" .'''

g = Graph()
g.bind("dc", "http://purl.org/dc/elements/1.1/")
g.bind("rdf", "http://www.w3.org/1999/02/22-rdf-syntax-ns#")
g.parse(data=testrdfn3, format="n3")
rdfjson = g.serialize(None, format="rdf-json")
assert '''"Anna's Homepage"''' in rdfjson
print(rdfjson)
print("""{
  "http://example.org/about": {
    "http://purl.org/dc/elements/1.1/title": [
      {
        "type": "literal",
        "value": "Anna's Homepage"
      }
    ]
  }
}""")

prettyrdfjson = g.serialize(None, format="rdf-json-pretty")
assert '''"Anna's Homepage"''' in prettyrdfjson
print(prettyrdfjson)
print("""{
  "xmlns$rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
  "http://example.org/about": {
    "dc$title": [
      {
        "type": "literal",
        "value": "Anna's Homepage"
      }
    ]
  },
  "xmlns$dc": "http://purl.org/dc/elements/1.1/"
}""")
