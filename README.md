### Review-Classification-using-Naive-Bayes-
###Classify reviews into faked or legitimate, for 20 hotels in Chicago


## Description:
The problem stated is a classification problem where we need to classify input in two classes - truthful and deceptive. We have implemented the Naïve Bayes Classifier to solve the problem. This classifier is used in sentiment analysis and spam filtering and hence it is the best suited one to solve this problem. This approach is a Naïve assumption to the bayes theorem. We split the events into independent parts – class ‘x’ and class ‘y’, 
#### P (x, y) = P(x)P(y)
Which gives us, 
#### P(y|x1,x2,…xn) = P(x1|y)P(x2|y)….P(xn|y)P(y)/(P(x1)P(x2)…P(xn))
Ignoring the denominator as it stays constant, 
#### P(y|x1,…..xn) = P(y) π P(xi|y) 	,where i = 1 to n 
Now, to create a classifier model, we find the probability of given set of inputs for all possible values of the class variable y and pick up the output with maximum probability. 
We have implemented the same concept in our classifier function.

### Training the data:
We split the messages(objects) based on some common delimiters, which gives us separate words. 
#### find_posterior_prob() function:
We calculate the total number of times the classes occur, in our case total number of ‘truthful’ and ‘deceptive’ labels. We also define a dictionary of distinct words. This dictionary is initialized as distinct_word_freq[word] = {truthful:0, deceptive:0}. This means that the distinct word has been categorised as truthful and deceptive zero number of times. We keep increasing the frequency of the classes as we traverse through the distinct words. Thus, we get the number of times one particular word was classified as truthful or deceptive from the training data.

### Classifying the test data:
#### classifier() function:
We have defined a spam word list. This list contains frequent words occurring in messages that do not have any semantic meaning. 
Now, for every message(object) we find the posterior probability of the two classes using the formula mentioned below, 
#### P(t) = P(t)/(P(t)+P(d))

Then, for every word in the message we check the following – \
a.	that the word exists in our distinct words dictionary\
b.	that the word does not exist in our spam list\
c.	that the frequency of the word being truthful and deceptive is greater than zero (basically eliminating the words that are not being classified as truthful or deceptive even once) 

We calculate the posterior probabilities of this filtered list of words for both classes and append the class with the greater posterior probability to our final classification list.\
Initially we came up with a plan to eliminated the words that have not been classified as truthful or deceptive more than a bunch of times. We kept increasing and decreasing the frequency value and ended up on zero as it gave the most accurate result approximately 83%. We then used a spam word list to eliminate any other semantically irrelevant words. This helped us increase our accuracy up to 85.25%. 

