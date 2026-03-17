from typing import TypedDict

##
# * Type Safety -we definded explicitly what the data structute are, reducing runtimes erros.
# * Enhanced Readability - Makes debugging easier and make code more understandable.

original_dict = {"name": "Yes Dir", "year": 2009}

# Defining the dictionary hints
class Movie(TypedDict):
    name: str
    year: int

my_movie = Movie(name="Yes Sir", year=2008)

print(f"original dict{original_dict} -> typedDict {my_movie}")

