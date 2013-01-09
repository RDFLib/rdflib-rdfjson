This parser/serialiser will 

* read in an RDF/JSON formatted document and create an RDF graph 
* serialize an RDF graph to RDF/JSON formatted output 

See:
  http://docs.api.talis.com/platform-api/output-types/rdf-json

It was originally written by Rob Sanderson as a plugin for RDFLib 2.x.
This version modifies the import paths for compatibility with RDFLib 3.x
and changes its name to RdfJsonParser due to the large number of
other JSON serialisations of RDF.

See:
  http://code.google.com/p/rdflib/issues/detail?id=76

[![Build Status](https://travis-ci.org/RDFLib/rdflib-rdfjson.png?branch=master)](https://travis-ci.org/RDFLib/rdflib-rdfjson)

