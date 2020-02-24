# BalancedCodesKnuth

This project is an inplementation of Knuth's algorithm for balanced codes, given in "Efficient Balanced Codes", IEEE Transactions on Information Theory, vol. 32,
no. 1, pp. 51–53, Jan. 1986. 

Our implementation supports various input lengths and alphabet size of upto 10 symbols.
We also added some improvements for the algorithm, making it better for various cases.

A documented details can be seen in *description.pdf* file.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project requires Python 3 for running it. It does not use any special libraries.

### Installing

Install python3 and download the git repository. 
After downloading, you can import from "knuth.py" and use the functions: encode_knuth, decode_knuth.

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
001000110112111221220222002
001000110
```

## Running the tests

The tests for this project can be found in *test.py* file.
Simply run the file and watch the test run. If a test fail you will be notified by the output.
### Some Important tests

#### test_encode_knuth
This test checks some basic vectors and see that they are encoded correctly.

#### test_decode_knuth
This test checks that vectors are decoded correctly by the decoding function

#### test_stress
This test generated random vectors and checks that they are encoded correctly and also decoded correctly. Additionally, there is a check that assures that the result of the encoding is balanced.

## Authors

* **Noa Marelly**
* **Ohad Goudsmid**

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
