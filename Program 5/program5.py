# Program 5: Implementation of Find-S Algorithm for Concept Learning
#
# Concept: Concept Learning as Search
# Find-S finds the most specific hypothesis that is consistent
# with all positive examples. Negative examples are ignored.


def find_s(training_data):
    # Initialize hypothesis as None
    hypothesis = None

    # Find the first positive example
    for row in training_data:
        if row[-1] == "Yes":
            hypothesis = row[:-1].copy()
            break

    # If there are no positive examples
    if hypothesis is None:
        return "No positive instances found."

    # Compare all remaining positive examples
    for row in training_data:
        if row[-1] == "Yes":

            for i in range(len(hypothesis)):
                # If attributes are different, generalize to '?'
                if row[i] != hypothesis[i]:
                    hypothesis[i] = "?"

    return hypothesis


# Example Usage
if __name__ == "__main__":

    # Columns:
    # Sky, Temp, Humidity, Wind, Water, Forecast, EnjoySport

    dataset = [
        ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
        ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
        ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
        ["Sunny", "Warm", "High", "Strong", "Cool", "Change", "Yes"]
    ]

    # Apply Find-S algorithm
    most_specific_hypothesis = find_s(dataset)

    # Display the result
    print("Most Specific Hypothesis found by Find-S:")
    print(most_specific_hypothesis)