# SeekTruth.py : Classify text objects into two categories
#
# PLEASE PUT YOUR NAMES AND USER IDs HERE
#
# Based on skeleton code by D. Crandall, October 2021
#

import sys
import re
def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(parsed[1] if len(parsed)>1 else "")

    return {"objects": objects, "labels": labels, "classes": list(set(labels))}

# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to reviews
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each review
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the result
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!
#

def find_posterior_prob(freq_A, freq_B):
    res = freq_A/(freq_A + freq_B)
    return res


def classifier(train_data, test_data):
    # This is just dummy code -- put yours here!
    
    frequency_of_class = {}
    number_of_classes = len(train_data["classes"])

    for i in range(number_of_classes):
        frequency_of_class[train_data["classes"][i]] = 0

    distinct_words_freq = {}

    traformed_train_data = zip(train_data['objects'], train_data['labels'])
    
    for message, label in traformed_train_data:
        for word in re.split(',|_|-|!|\s+', message):
            if word in distinct_words_freq.keys():
                distinct_words_freq[word][label] += 1
            else:
                distinct_words_freq[word] = {train_data["classes"][0]:0, train_data["classes"][1]:0}
                distinct_words_freq[word][label] += 1
        frequency_of_class[label]+=1
    
    final_result = []
    spam = [ 'Hi', 'Hello', '?', 'lol', 'Oh', 'Dear', 'Thank', 'Regards', 'the', 'an', 'and', 'a']
    for message in test_data["objects"]:

        class_t_prob = find_posterior_prob(frequency_of_class[test_data["classes"][0]], frequency_of_class[test_data["classes"][1]])
        class_d_prob = find_posterior_prob(frequency_of_class[test_data["classes"][1]], frequency_of_class[test_data["classes"][0]])

        for word in re.split(',|_|-|!|\s+', message):
            if word in distinct_words_freq.keys() and word not in spam and(distinct_words_freq[word][test_data["classes"][0]] > 0) and (distinct_words_freq[word][test_data["classes"][1]] > 0):
                class_t_prob = class_t_prob * find_posterior_prob(distinct_words_freq[word][test_data["classes"][0]] , distinct_words_freq[word][test_data["classes"][1]])
                class_d_prob = class_d_prob * find_posterior_prob(distinct_words_freq[word][test_data["classes"][1]] , distinct_words_freq[word][test_data["classes"][0]])
        if class_t_prob > class_d_prob:
            final_result.append(test_data["classes"][0])
            #print(final_result, "In if ************")
        else:
            final_result.append(test_data["classes"][1])
            #print(final_result, "In else ************")
    
    #print(final_result)
    return final_result



if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)
    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"], "classes": test_data["classes"]}

    results = classifier(train_data, test_data_sanitized)

    #calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))
