from rdflib import Graph
import os

def determine_format(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read(1024)

    if content.startswith('<?xml'):
        if '<rdf:RDF' in content or '<RDF' in content:
            return 'xml'
    elif '@prefix' in content or '@base' in content:
        return 'ttl'
    elif '{' in content and '@context' in content:
        return 'json-ld'
    elif content.startswith('<') and '>' in content:
        if content.count('<') == 1 and ' ' not in content:
            return 'nt'
        elif content.count('<') > 1:
            return 'nquads'
    elif '<TriX' in content:
        return 'trix'
    elif 'xmlns:rdfa' in content:
        return 'rdfa'
    elif content.startswith('#') or '@prefix' in content:
        return 'n3'
    elif '@prefix' in content and '{' in content:
        return 'trig'
    else:
        return None

formats = ["ttl", "xml", "json-ld", "nt", "nquads", "trix", "rdfa", "n3", "trig"]

file_path = input("Enter the file name: ")

if not os.path.exists(file_path):
    print("File not found.")
else:
    format = determine_format(file_path)
    if format not in formats:
        print("Invalid file format")
    else:
        try:
            g = Graph()
            g.parse(file_path, format=format)
            print("RDF file is valid.")
        except Exception as e:
            print(f"Error: {e}")
