# RDF Format Detector and Validator

This script detects the format of an RDF file and validates its syntax using the `rdflib` library.

## 📄 Description

The script reads a small portion of an RDF file to determine its format based on common patterns. It supports various RDF serialization formats including:

- Turtle (`ttl`)
- RDF/XML (`xml`)
- JSON-LD (`json-ld`)
- N-Triples (`nt`)
- N-Quads (`nquads`)
- TriX (`trix`)
- RDFa (`rdfa`)
- Notation3 (`n3`)
- TriG (`trig`)

Once the format is detected, it uses `rdflib.Graph` to parse and validate the file.

## ✅ Features

- Automatically detects RDF serialization format based on content.
- Validates the RDF file using `rdflib`.
- Provides informative error messages if validation fails.

## 📦 Requirements

- Python 3.6+
- `rdflib`

Install the required library using pip:

```bash
pip install rdflib
```

## 🚀 Usage

1. Save the script as `rdf_validator.py`.
2. Run the script:

```bash
python rdf_validator.py
```

3. Enter the file path when prompted:

```
Enter the file name: example.ttl
```

If the file is valid and the format is supported, you will see:

```
RDF file is valid.
```

Otherwise, an error message will be shown.

## 🔍 Format Detection Logic

The script checks the file content for common indicators like:
- `<?xml` and `<rdf:RDF>` for RDF/XML
- `@prefix` for Turtle, N3, and TriG
- `<` and `>` for N-Triples and N-Quads
- `@context` and `{}` for JSON-LD
- `<TriX` for TriX
- `xmlns:rdfa` for RDFa

## ⚠️ Limitations

- Format detection is heuristic and may not cover all edge cases.
- Only the first 1024 characters of the file are analyzed to determine the format.

## 🧑‍💻 Author

Amir Sadrnia
