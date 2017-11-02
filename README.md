# Lexical-Analysis-Training-Set
Methods for training artificial intelligence to identify language patterns (Python).

# Methods
• groupTwo:
  Takes an array of strings and pairs each string with its right most partner. Returns an array of these pairs.

• matrixComp:
  Takes two matrices and compares each of their values with the value sharing the same index in the opposing array. If all        values match it returns true, otherwise it returns false.

• factorial:
  Pairs every value in an array with every other value in the array once, returns the result of matrixComp upon creating every    pair.
  
# Usage

````python
trainingSet = ['noun','verb','verb','adjective','noun']

//pair each word with it's right-most neighbor

pairs = venn.groupTwo(TrainingSet)

// pair each pair created by groupTwo with every other pair once; for every time this
// done return true if the pairs are identical, otherwise return false

venn.factorialpvenn.factorial(pairs)
````
