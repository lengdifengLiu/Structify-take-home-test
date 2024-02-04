#!/usr/bin/env python
# coding: utf-8

# In[2]:


def count_intersections(radians, identifiers):
    # Create a dictionary to store the start and end radians for each chord
    chords = {}
    for i, iden in enumerate(identifiers):
        # Extract the number from the identifier to map starts and ends together
        num = ''.join(filter(str.isdigit, iden))
        if 's' in iden:
            chords[num] = {'start': radians[i]}
        else:
            chords[num]['end'] = radians[i]

    # Create a list of chords with start and end radians
    chords_list = [(chord['start'], chord['end']) for chord in chords.values()]

    # Sort chords by their start radians
    chords_list.sort(key=lambda x: x[0])

    # Function to check if two chords intersect
    def do_intersect(c1, c2):
        start1, end1 = c1
        start2, end2 = c2
        # Two chords intersect if one of them starts between the start and end of the other,
        # but does not end between the start and end of the other
        return (start1 < start2 < end1 and not start1 < end2 < end1) or \
               (start2 < start1 < end2 and not start2 < end1 < end2)

    # Count the number of intersecting chords
    intersection_count = 0
    for i in range(len(chords_list)):
        for j in range(i + 1, len(chords_list)):
            if do_intersect(chords_list[i], chords_list[j]):
                intersection_count += 1

    return intersection_count

# Test the function with the provided example inputs
example_input_1 = ([0.78, 1.47, 1.77, 3.92], ["s_1", "s_2", "e_1", "e_2"])
example_input_2 = ([0.9, 1.3, 1.70, 2.92], ["s1", "e1", "s2", "e2"])

# Count intersections for both examples
intersections_1 = count_intersections(*example_input_1)
intersections_2 = count_intersections(*example_input_2)

(intersections_1, intersections_2)


# In[ ]:




