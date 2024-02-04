# Structify-take-home-test
# Chord Intersection Counter

## Description
This program counts the number of intersections between chords in a circle. An intersection occurs when two chords cross each other within the circle.

## Algorithm
The algorithm sorts the chords by their starting radians and then iterates through each pair of chords to check for intersections. An intersection is found if one chord starts between the start and end radians of another chord, but its end radian does not lie between the other chord's start and end radians.

## Complexity Analysis
The algorithm consists of two major parts:
1. Sorting the chords by their starting radians: If we use a comparison-based sorting algorithm like quicksort or mergesort, this step has a time complexity of O(n log n), where n is the number of chords.

2. Checking for intersections: This part involves a nested loop where each chord is compared with every other chord to check for intersections. Since each chord must be compared with every other chord once, the time complexity for this part is O(n^2).

Therefore, the overall time complexity of the algorithm is dominated by the second part, which is O(n^2).

