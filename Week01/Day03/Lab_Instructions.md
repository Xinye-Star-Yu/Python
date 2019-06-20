# Lab 1: Recursion and Testing

 ## Part 0
1.  Review the code in `location.py`. Note that there is a class definition for
    a `Location` class, and an associated `__init__` method. In addition, there
    is code to create Location objects and print information associated with
    those objects.

     ```python
    class Location:
        def __init__(self, name, lat, long):
            self.name = name    # string for name of location
            self.lat = lat      # latitude in degrees (-90 to 90)
            self.long = long    # longitude in degrees (-180 to 180)
    ```

 2.  Without modifying the code, run `location.py` in whatever environment you
    wish (again, reference the "Installing Python 3" document if you need help
    in doing this).

 3.  Note the information that is printed out for each Location object - you
    should see something like this:

         Location 1: <__main__.Location object at 0x000001F6A2E0C7B8>

 4.  Since we haven't provided any specific method to provide a representation
    for the class, Python uses a default method. What do you notice about the
    information for Locations 1 and 4?

 5.  Also note the result of the equality comparisons between the locations, in
    particular `loc1 == loc3` and `loc1 == loc4`. Make sure you understand why
    the results are what they are.

 6.  Now modify the `location.py` code, adding in the methods `__eq__()` and
    `__repr__()`. See the `location_tests.py` to figure out what the repr method
    should look like.

 7.  Run the `location.py` code with the modifications made above.

 8.  Now review the information printed out for each location. The `__repr__`
    method of Location is now being used when printing the object.

 9.  Examine the results of the equal comparisons. How are they different from
    before the `__eq__` method is added?


 ## Part 1
1.  In the `lab1.py` file, complete the iterative function to find the maximum
    integer in a list of integers.

     ```python
    def max_list_iter(int_list):  # must use iteration not recursion
       """finds the max of a list of numbers and returns the value (not the index)
       If int_list is empty, returns None. If list is None, raises ValueError"""
    ```

 2.  In the `lab1.py` file, complete the recursive function to reverse a list of
    integers:

     ```python
    def reverse_rec(int_list):   # must use recursion
       """recursively reverses a list of numbers and returns the reversed list
       If list is None, raises ValueError"""
    ```

 3.  In the `lab1.py` file, complete the recursive function to search a list of
    integers using binary search along with test cases. If the target of the
    search is in the list, the function returns its index.

     ```python
    def bin_search(target, low, high, int_list):  # must use recursion
       """searches for target in int_list[low..high] and returns index if found
       If target is not found returns None. If list is None, raises ValueError """
    ```

 ## Test Cases
Many people tend to focus on writing code as the singular activity of a
programmer, but testing is one of the most important tasks that one can perform
while programming. Writing high quality test cases can greatly simplify the
tasks of both finding and fixing bugs and, as such, will save you time during
development. That said, testing does not guarantee that your program is correct.

 For this part of the lab you will practice writing some simple test cases to
gain experience with the `unittest` framework. I recommend watching the first
20 minutes or so of the following video if you need more guidance on testing in
Python. <https://www.youtube.com/watch?v=6tNS--WetLI>

 Using your editor/IDE of choice, open the `lab1_test_cases.py` file. This file
defines, using code that we will treat as a boilerplate for now, a testing class
with a single testing function. In the `test_expressions` function you will see
some test cases already provided. You must add additional test cases to verify
that your functions (`max_list_iter`, `reverse_rec`, `bin_search`) are correct.


 ## Submission and Grading
Ensure that the following files have been pushed to GitHub by the due date:

 -   `lab1.py`
    -   Correct and well documented iterative `max_list_iter`, recursive
        `reverse_rec`, and `recursive bin_search` functions based on the
        template provided  **(5 points)**

 -   `lab1_test_cases.py`
    -   A complete set of test cases for the functions above. **(5 points)**

         Your test cases should test boundary conditions and other possible
        errors based on the structure of your program. For each test provide a
        comment (docstring) that explains what it is testing. Your tests cases
        will be tested with known incorrect (buggy) versions of the functions
        in `lab1.py` and will also be tested for 100% code coverage. 
