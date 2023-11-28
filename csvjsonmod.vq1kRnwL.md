List of common methods for working with CSV and JSON in Python:

### CSV (using `csv` module):

1. **`csv.reader(file, dialect='excel', **kwargs)`:**
   - Purpose: Creates a CSV reader object that reads rows from the specified file.

2. **`csv.writer(file, dialect='excel', **kwargs)`:**
   - Purpose: Creates a CSV writer object that writes rows to the specified file.

3. **`csv.reader.__next__()` or `next(csv.reader)`:**
   - Purpose: Advances the CSV reader to the next row and returns it.

4. **`csv.writer.writerows(rows)`:**
   - Purpose: Writes multiple rows to the CSV file.

5. **`csv.writer.writerow(row)`:**
   - Purpose: Writes a single row to the CSV file.

6. **`csv.fieldnames`:**
   - Purpose: A list containing the field names of the CSV file.

7. **`csv.Dialect`:**
   - Purpose: An object that defines various properties of the CSV format, such as delimiter and quoting behavior.

8. **`csv.register_dialect(name, dialect=None, **fmtparams)`:**
   - Purpose: Registers a new CSV dialect.

### JSON (using `json` module):

1. **`json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`**:
   - Purpose: Serialize obj to a JSON formatted str.

2. **`json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`**:
   - Purpose: Serialize obj as a JSON formatted stream to a file-like object.

3. **`json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`**:
   - Purpose: Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.

4. **`json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`**:
   - Purpose: Deserialize fp (a .read()-supporting text file or binary file containing a JSON document) to a Python object.

5. **`json.JSONEncoder.default(o)`**:
   - Purpose: Override this method in a custom JSONEncoder subclass to implement custom serialization.

6. **`json.JSONDecoder.object_hook(d)`**:
   - Purpose: Override this method in a custom JSONDecoder subclass to implement custom deserialization.

7. **`json.JSONEncoder.encode(o)`**:
   - Purpose: Implement this method in a custom JSONEncoder subclass to convert obj to a JSON-serializable form.

8. **`json.JSONDecoder.decode(s)`**:
   - Purpose: Deserialize s (a str, bytes or bytearray instance containing a JSON document) to a Python object.

9. **`json.JSONEncoder.default(o)`**:
   - Purpose: Override this method in a custom JSONEncoder subclass to implement custom serialization.



### Advanced CSV Features:

1. **Custom Dialects:**
   - **Method: `csv.register_dialect(name, dialect=None, **fmtparams)`:**
   - **Purpose:**
     - Register a new CSV dialect with custom parameters like delimiter, quote character, etc.

2. **Reading into Dicts:**
   - **Method: `csv.DictReader(file, fieldnames=None, restkey=None, restval=None, dialect='excel', **kwargs)`:**
   - **Purpose:**
     - Reads a CSV file into a list of dictionaries where each row is represented as a dictionary.

3. **Writing from Dicts:**
   - **Method: `csv.DictWriter(file, fieldnames, restval='', extrasaction='raise', dialect='excel', **kwargs)`:**
   - **Purpose:**
     - Writes dictionaries into a CSV file. Each dictionary is a row, and keys are used as column headers.

### Advanced JSON Features:

1. **Custom Serialization:**
   - **Method: `json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`**:
   - **Purpose:**
     - Use the `default` parameter to specify a custom serialization function for non-serializable objects.

2. **Custom Deserialization:**
   - **Method: `json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)`**:
   - **Purpose:**
     - Use the `object_hook` parameter to specify a custom deserialization function for decoding JSON objects.

3. **JSON Pretty Printing:**
   - **Method: `json.dumps(obj, indent=4, sort_keys=True)`:**
   - **Purpose:**
     - Use the `indent` parameter to specify the number of spaces for indentation, making the JSON output more human-readable.
