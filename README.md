# Suffix Array Burrows-Wheeler-Transform

This JupyterLab notebook contains Python solutions for the following three problems:

1. Suffix Array Construction Problem
2. Burrows-Wheeler Transform Construction Problem
3. Inverse Burrows-Wheeler Transform Problem

## Installation

To run this notebook, you will need to install the following Python packages:

- numpy
- pandas

## Usage

1. Download the JupyterLab notebook (.ipynb file) and open it in JupyterLab.
2. Run each cell in the notebook to see the solutions for each problem.


## Suffix Array Construction Problem

The suffix array problem uses the memory-efficient algorithm presented by Manber and Myers as an alternative to suffix trees. Sort all of the suffixes in the text in lexicographical order. This will give us a list of starting positions for the sorted suffixes.

## Burrows-Wheeler Transform Construction Problem

The Burrows-Wheeler Transform presents a different method for converting the repeats of a string to runs. The text is broken down into each cyclic rotation, meaning the suffix of a tree is chopped and appended to the end of the string; this forms a matrix known as the Burrows-Wheeler matrix. The last column of the matrix makes up the Burrows-Wheeler transform.

## Inverse Burrows-Wheeler Transform Problem

The inverse Burrows-Wheeler transform reconstructs a string from the Burrows-Wheeler transform
