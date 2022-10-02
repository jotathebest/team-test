# About the Setup

## Requirements

- python 3.8 or greater (may be installed following instructions at [python downloads](https://www.python.org/downloads/))

# About how to run the application

## Python package

The class `DataCapture` may be imported from the `datacapture` script. A functional example may be found in 
the `example.py` script

## Unit tests

To trigger the unit tests, go to the root folder and run

```bash
python -m unittest tests/test*.py
```

# About the Algorithm

## DataCapture

Any new number added will be stored inside a dictionary, where the key will be the number and the value
will be the times the number has been added. For example, if you add the number two three times and
number five once, a dictionary as follows will be stored:

```
{2: 3, 5: 1}
```

A new zeros array of length equals to the higher inserted number to represent the counter of any _n_ positive
is also created. Each position _k_ will be filled with the sum of counters less than the position.
For the example above, we would have as max the number 5 and the following counters array:

```
[0, 3, 3, 3, 4]
```

This may be mapped to the _n_ positive numbers found as follows

| 0   | 3   | 3   | 3   | 4   |
|-----|-----|-----|-----|-----|
| 1   | 2   | 3   | 4   | 5   | 

we may build this map as follows:

1. Number 1 is not stored, so we fill the first position with a zero
2. Number 2 is stored, so we fill the stored counter plus the value of the previous one: `counter = 3 + 0`
3. Number 3 is not stored, so we fill with the previous counter
4. Number 4 is not stored, so we fill with the previous counter
5. Number 5 is stored, so we fill the stored counter plus the value of the previous one: `counter = 1 + 3`

The pseudocode may be inferred as follows:

```
if number is stored then fill with the sum of the previous value and the stored counter
else fill with the previous counter value
```

## Stats

The algorithm will be explained using as input the following counter array:

| 0   | 3   | 3   | 3   | 4   |
|-----|-----|-----|-----|-----|
| 1   | 2   | 3   | 4   | 5   | 

### less

As the counter is also a sorted array, if we need to find the sum of inserted numbers before a certain value,
we just need to move an index before the value asked. This means if we need to find the counter for value 3,
we just need to return the stored index for value 2, which is 3.

| 0   | 3     | 3   | 3   | 4   |
|-----|-------|-----|-----|-----|
| 1   | 2     | 3   | 4   | 5   |
|     | **↑** |     |     |     |

### between

For a reference example, get the sum of numbers stored between 3 and 4.

| 0   | 3   | 3     | 3     | 4   |
|-----|-----|-------|-------|-----|
| 1   | 2   | 3     | 4     | 5   |
|     |     | **↑** | **↑** |     |

The way to calculate the result may be referenced in the pseudocode below:

```
1. Get the times the lower limit is stored, which is the result of the counter in the lower index less the counter
of the previous index. For the example, it will be array[3] - array[2] = 0 (The user never inserted a 3)
2. Get a remaining. This will the result of the upper limit counter less the lower limit counter. 
For the example, it will be array[4] - array[3] = 0 (The user never inserted a 4)
3. The result will be the sum of times obtained from (1) and remaining from (2). For the example, it will be 0 
```

### greater

For a reference example, get the sum of numbers greater than 3.

| 0   | 3   | 3     | 3   | 4   |
|-----|-----|-------|-----|-----|
| 1   | 2   | 3     | 4   | 5   |
|     |     | **↑** |     |     |

The result will be the remainder between the max value (the last one in the counter array) and the counter
of the index number. For the example, it will be `array[5] - array[3] = 1`