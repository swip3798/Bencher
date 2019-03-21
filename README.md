# Bencher
Benchmarking system for python 3

## Description
This is a little Benchmarking module for Python 3. It provides a easy to use Benchmarking class and a statistics class for further analysis.
It can save the measured benchmarks into a centralized folder in the home/user directory. This works crossplatform, I currently tested it on Windows and Debian, but it should work on most linux distributions and on OSX as well.

## Install

`python setup.py install` 


## Usage
```python
from bencher import Bencher
benchmark = Bencher("benchmarkcase")
benchmark.start()
# Productive coding
######
#
benchmark.stop()

# To get the measured time
time_needed = benchmark.get_time()

# To print a benchmark hint
print(benchmark)

# Save current benchmark for later analysing via the bencher.Statter class
benchmark.save()

# Reset benchmark
benchmark.reset()
```

## Usage statter

```python
from bencher import Statter

statter = Statter("benchmarkcase")

# Get sum
statter.sum()

# Get average
statter.avg()

# Get count
statter.count()
```

I will add more features, when I need them or someone requests them.
