# NumRs Tutorial
An exploration of high performance Python Modules built in Rust by creating a basic NumPy clone.

## Setup
0. Make sure you have installed [Rust](https://www.rust-lang.org/tools/install) and [Python](https://www.python.org/downloads/) before installing further dependencies.
1. Create a [virtual environment](https://docs.python.org/3/library/venv.html)
2. Inside the virtual environment, install Python dependencies: `pip install -r requirements.txt`
3. Create a dev build of NumRs: `maturin develop`
4. Try it out using the Python REPL by importing the `numrs` library.

## Tests
All library tests are written in Python and located in the `tests` folder. The `pytest` terminal command will run all tests.

