# LeetCode Problem Solving Repository

Welcome to my LeetCode Problem Solving Repository! This repository contains my solutions to various coding problems on LeetCode. It's a comprehensive collection of algorithms and data structure problems solved in multiple programming languages. The primary goal of this repository is to enhance my problem-solving skills, prepare for technical interviews, and provide a valuable resource for other developers.

## Features

- **Diverse Problem Set**: Solutions to problems across different categories such as arrays, strings, linked lists, trees, graphs, dynamic programming, and more.
- **Multiple Programming Languages**: Solutions are implemented in various programming languages including Python, JavaScript, Java, and C++.
- **Optimized Code**: Focus on writing clean, efficient, and optimized code with proper documentation and comments.
- **Algorithmic Techniques**: Implementation of various algorithmic techniques such as recursion, backtracking, greedy algorithms, divide and conquer, and dynamic programming.
- **Unit Tests**: Comprehensive test cases included for each solution to ensure correctness and robustness.

## Example Code

Below is an example of a Python solution with a copy button:

<div style="position: relative;">
  <pre><code id="code1">
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
  </code></pre>
  <button onclick="copyToClipboard('#code1')" style="position: absolute; top: 0; right: 0;">Copy</button>
</div>

## Contribution

Contributions are welcome! If you have a better solution or optimization, feel free to open a pull request. Please ensure that your code is well-documented and includes test cases.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to contact me via [email](mailto:your.email@example.com) or through GitHub issues.

## Scripts

<script>
function copyToClipboard(selector) {
  const element = document.querySelector(selector);
  const text = element.innerText;
  navigator.clipboard.writeText(text).then(function() {
    alert('Code copied to clipboard');
  }, function(err) {
    alert('Failed to copy text: ', err);
  });
}
</script>
