# Ona Challenge Question
Ona Challenge Question

### How to install
Simple Python script.  Ideally run from within a Virtual environment, with the libraries in requirements.txt installed

### How to run
Call the function calculate from ona.py with the argument url="https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

### How to run tests
`python tests.py`

### Results

Returns a dictionary, with the following items:

* number_functional - an integer representing number of functional water points

* number_water_points - a list of tuples, with all communities and the number of water points in each.  Each tuple contains the name of the comunity and the number of water points that it has

* community_ranking - a list of tuples which represents the communities sorted in order ranging from the community with the most non functional water points to the one with the least.  Each tuple includes the name of the community and the percentage of non functional water points that the community has
