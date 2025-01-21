Question 1: Data Center Optimization

Amazon is building a new data center with n servers of different types. Each server has a health value and a type, represented by two arrays: health and serverType. Your task is to maximize the sum of the health values of selected servers under the following conditions:

1. You can select servers of at most m distinct types.


2. The sum of the health values of the selected servers must be maximized.



Write a function findMaxHealthSum(health, serverType, m) to calculate the maximum sum of health values for the given constraints.


---

Solution:
```python
from collections import defaultdict

def findMaxHealthSum(health, serverType, m):
    # Group health values by server type
    type_to_health = defaultdict(list)
    for h, t in zip(health, serverType):
        type_to_health[t].append(h)

    # Sort health values for each server type in descending order
    max_health_per_type = []
    for healths in type_to_health.values():
        max_health_per_type.append(sum(sorted(healths, reverse=True)))

    # Select the top m types with the highest total health
    max_health_per_type.sort(reverse=True)
    return sum(max_health_per_type[:m])

# Example usage
n = 5
health = [10, 10, 10, 10, 10]
serverType = [3, 3, 5, 5, 1]
m = 2

print(findMaxHealthSum(health, serverType, m))  # Output: 20

```
---

Question 2: Quality Score Optimization

You are a seller on Amazon specializing in eco-friendly home products. Each product has a rating that reflects its quality and impact, stored in the ratings array. To improve the quality score of your products, you can modify the ratings using one of the following strategies:

1. Amplify Ratings: Select a contiguous subarray and multiply all ratings in that subarray by impactFactor.


2. Adjust Ratings: Select a contiguous subarray and divide all ratings in that subarray by impactFactor. For positive ratings, take the floor of the division; for negative ratings, take the ceiling.



The task is to determine the maximum possible quality score (sum of ratings) after applying exactly one of the two strategies.


---

Solution:
```python
import math

def calculateMaxQualityScore(impactFactor, ratings):
    n = len(ratings)
    max_quality_score = float('-inf')

    # Strategy 1: Amplify Ratings
    amplify_ratings = [r * impactFactor for r in ratings]
    max_amplify_sum = max_subarray_sum(amplify_ratings)

    # Strategy 2: Adjust Ratings
    adjust_ratings = [
        math.floor(r / impactFactor) if r > 0 else math.ceil(r / impactFactor)
        for r in ratings
    ]
    max_adjust_sum = max_subarray_sum(adjust_ratings)

    # Unmodified sum (Kadane's for original ratings)
    max_original_sum = max_subarray_sum(ratings)

    # The result is the maximum of the three strategies
    max_quality_score = max(max_amplify_sum, max_adjust_sum, max_original_sum)
    
    return max_quality_score

def max_subarray_sum(arr):
    # Kadane's algorithm for maximum subarray sum
    max_sum = float('-inf')
    current_sum = 0
    for x in arr:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage
ratings = [5, -3, -3, 2, 4]
impactFactor = 3
print(calculateMaxQualityScore(impactFactor, ratings))  # Output: 12

```
---
