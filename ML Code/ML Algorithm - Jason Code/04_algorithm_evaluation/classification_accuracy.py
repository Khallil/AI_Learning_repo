# Example of calculating classification accuracy

# Calculate accuracy percentage between two lists
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / float(len(actual)) * 100.0

# Test accuracy
actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,0,1,0,0,1,1,1,1,1]
accuracy = accuracy_metric(actual, predicted)
print(accuracy)

'''
Accuracy is a good metric to use when you have a small number of class values, such as 2,
also called a binary classification problem. Accuracy starts to lose it’s meaning when you have
more class values and you may need to review a different perspective on the results, such as a
confusion matrix.
'''