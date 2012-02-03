from setuptools import setup

# Requires simplejson if Python version < 2.6

setup(
    name = 'rdflib-rdfjson',
    version = '0.1',
    description = "rdflib extension adding RDF/JSON parser and serializer",
    author = "Graham Higgins",
    author_email = "gjhiggins@gmail.com",
    url = "http://github.com/RDFLib/rdflib-rdfjson",
    py_modules = ["rdflib_rdfjson"],
    test_suite = "test",
    install_requires = ["rdflib>=3.0", "rdfextras>=0.1"],
    entry_points = {
        'rdf.plugins.parser': [
            'rdf-json = rdflib_rdfjson.rdfjson-parser:RdfJsonParser',
        ],
        'rdf.plugins.serializer': [
            'rdf-json = rdflib_rdfjson.rdfjson-serializer:RdfJsonSerializer',
        ],
    }

)
