from rdflib import plugin
from rdflib import serializer
from rdflib import parser
import sys # sop to Hudson
sys.path.insert(0, '/var/lib/tomcat6/webapps/hudson/jobs/rdfextras')

plugin.register(
        'rdfa-json', serializer.Serializer,
        'rdflib_rdfjson.serializer', 'RdfJsonSerializer')

plugin.register(
        'rdfa-json', parser.Parser,
        'rdflib_rdfjson.parser', 'RdfJsonParser')

