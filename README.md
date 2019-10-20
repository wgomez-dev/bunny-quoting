# User Managment Api
This python script performs one lineal extrapolation using a dataset provided by a csv file.

The extrapolation formula used is:

![alt text](https://wikimedia.org/api/rest_v1/media/math/render/svg/6ada3c06653e948a1b0535afdec94e6c91c9d8ca)

## Assumptions
Based on the test description I made these assumptions

1. Each record belongs to one contractor.
2. It takes as an input that record and performs the analysis over those values.
3. The expected output is one value calculated using only that record values.
4. The propsed model is one implementation using the extrapolation formula described previously.

## How to run it
```bash
python3 extrapolation.py [contractorId] [number of units]
```
Example
For contractor user with id 76, we want to know the estimated value of 6500 units.

```bash
python3 extrapolation.py 76 6500
```
Output

```bash
For contractor with id  76  and current quoting values  {5: 10.98, 50: 21.96, 500: 153.74, 5000: 439.26, 50000: 2745.38}
The value of  6500.0  units is: 
516.13
```

## Algorithm Steps

1. Ask for the contractor id
2. Ask for the number of units to quote. 
3. Extract the contractor base dataset to perform the estimation, using the csv file as a source.
4. Detect to what range of units belongs the input value.
5. Perform the extrapolation formula.
6. Show the result to the user.

## Considerations
This script uses as an input one csv file as a source, the source could be updated externally and the script works since it reads it every time it runs.

