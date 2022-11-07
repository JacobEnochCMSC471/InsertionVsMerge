# InsertionVsMerge
Implementation and comparison of recursive Merge Sort and Insertion Sort in Python. Implementation is based off of CLRS pseudocode, found in the Divide and Conquer section of the textbook. MatPlotLib is used to plot the sorting times of these algorithms, given differently sized and randomly populated arrays. 

As shown by the plots of array length vs time, merge sort is in almost every case faster than selection sort due to it's runtime of Θ(nlogn). Note that this definition of Θ indicates that the upper and lower bounds for merge sort are O(nlogn) and Ω(nlogn) respectively. 

Created as part of a homework assignment for an algorithms class taken at UMBC. 

![Alt text]([https://github.com/JacobEnochCMSC471/InsertionVsMerge/Insertion_Sort_Times.jpg?raw=true] "Title")
