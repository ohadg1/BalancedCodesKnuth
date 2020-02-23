# BalancedCodesKnuth

This project is an inplementation of Knuth's algorithm for balanced codes, given in "Efficient Balanced Codes", IEEE Transactions on Information Theory, vol. 32,
no. 1, pp. 51–53, Jan. 1986. 

Our implementation supports various input lengths and alphabet size of upto 10 symbols.
We also added some improvements for the algorithm, making it better for various cases.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project requires Python 3 for running it. It does not use any special libraries.

### Installing

Install python3 and download the git repository. 
After downloading, you can import from "knuth.py" and use the functions: encode_knuth, decode_knuth

```
from knuth import *

to_encode = "001000110"

encoded = encode_knuth("001000110", 3) # encode into a 3-base balanced code
print(encoded)

decoded = decode_knuth(encoded, 3, 9) #decode for a vector of length 9
print(decoded)
```

The output suould be:
```
221200110110000221111002222
001000110
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Authors

* **Noa Marelly**
* **Ohad Goudsmid**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
