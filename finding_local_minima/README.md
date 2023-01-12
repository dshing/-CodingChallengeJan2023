# Finding local minima of a dataset

You are free to use any programming language you prefer. Please comment all your steps and solution methods either directly in the code or separately in a
text document. lease put the main emphasis on the solution
approach. If you do not provide any code for a certain task, please write down how you would try to
solve it.

Should there be anything ambiguous, please comment the issue. Write down the problem you a
struggling with and point out, what information you are missing. However, please try to include the
most obvious solution.

### Description
Please use the file [data.json](data.json) for this task.

Please consider only the values **close** and **time** for this task.
The format used above is json, you are free to convert the list into any other format of you choice.
Try to find local minima, use two methods to do so (A and B) and
output the detected Minima in a list (**close** and **time**).

#### Method A
Definition of a minimum:
```
f(t-1) > f(t) < f(t+1)
```
 Check the data and use the above condition to detect a local minimum,
 `f(t)`being a **close** value at a certain **time t**.
 
 #### Method B
 Definition of a minimum for a consecutive amount of numbers
 ```
e(t) = f(t)-f(t-1)
```

Detect a signchange from - to + (`e<0 to e>0`).

Check the data and use the above condition to detect a local minimum,
 `f(t)`being a **close** value at a certain **time t**.