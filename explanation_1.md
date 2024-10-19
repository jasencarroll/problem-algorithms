# Square Root Finder

This project implements an efficient algorithm to find the floored square root of an integer without using any external libraries or functions. The primary objective is to solve the problem with optimal time complexity, meeting the requirement of \(O(\log(n))\).

## Reasoning Behind the Approach

The algorithm uses **binary search** to solve the problem. Binary search is an excellent fit here because the square root function is **monotonic**—it either increases or remains constant as we progress from smaller to larger numbers. This allows us to systematically reduce the search space by half in each iteration, making binary search an ideal candidate for achieving logarithmic time complexity.

### Why Binary Search?
- **Efficient Search Space Reduction**: Instead of linearly searching for the square root (which would result in a time complexity of \(O(n)\)), binary search allows us to divide the problem space into halves, ensuring a much faster solution.
- **Monotonic Property**: The square of any number increases as the number increases. This property ensures that binary search can be applied since we can easily decide whether to move to the left or right half based on the current midpoint's square.

### Handling Edge Cases
The algorithm handles edge cases where the number is 0 or 1, returning the number itself as the square root, because the square root of these values is trivial.

## Time and Space Complexity

- **Time Complexity**: The time complexity of this algorithm is \(O(\log(n))\), where \(n\) is the input number. This is because the search space is halved with each iteration of the binary search. Given that binary search compares the midpoint's square to the input number, the search continues until it converges on the correct floored value.

- **Space Complexity**: The space complexity is \(O(1)\), meaning that the algorithm uses a constant amount of additional memory, regardless of the input size. This is due to the fact that only a few variables are used (such as `low`, `high`, `mid`, and `result`), and no additional data structures are needed.

## Conclusion
The chosen approach strikes a balance between simplicity and efficiency. Binary search ensures that the algorithm runs in logarithmic time, which is optimal for this problem. Additionally, by only using a constant amount of extra space, the algorithm remains lightweight, making it suitable for large input numbers without excessive memory overhead.