# Prompt Optimization

## Overview

This project implements an optimization algorithm for prompts based on the paper "Automatic Prompt Optimization with Gradient Descent and Beam Search." The core idea is to iteratively refine prompts using natural language "gradients" that point out prompt weaknesses, followed by edits in the opposite semantic direction. This approach mimics gradient descent but operates within the discrete space of textual prompts.

The goal of this project is to adapt this optimization algorithm specifically for code generation tasks. It utilizes the **HumanEval** dataset for batch evaluations and fine-tunes the **CodeT5** transformer model using the **APPS** dataset to improve generated code quality.

## Features

- **Automatic Prompt Optimization**: Iteratively refines prompts using textual feedback.
- **Code Generation-Specific Adaptation**: Tailored for optimizing prompts related to programming tasks.
- **Evaluation on HumanEval**: Uses benchmark coding problems for assessing prompt effectiveness.
- **Fine-Tuning with APPS Dataset**: Enhances CodeT5 performance by training on additional programming problems.

## Architecture
![image](https://github.com/user-attachments/assets/27c776f7-da15-4073-a759-f96c817f8768)
- **Initial Prompts:** Start with natural language prompts for code generation tasks.
- **Optimization Engine:** Iteratively refines prompts using feedback to improve code generation quality.
- **CodeT5 Model:** Utilizes an already optimized CodeT5 model for generating error messages.
- **Evaluation:** Prompts are evaluated using the HumanEval dataset.
- **Iterative Feedback Loop:** Selects the best-performing prompt based on evaluation results.
## Installation (For Development)

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Pip
- Jupyter Notebook (optional, for interactive testing)

### Setup

Clone the repository:

```bash
git clone https://github.com/your-repo/prompt-optimization.git
cd prompt-optimization
```

Install dependencies:

```bash
pip install -r requirements.txt
```


### **Usage (For Testing and Development)**

1. Navigate to the `ProTeGi/HumanEval` directory:

   ```bash
   cd ProTeGi/HumanEval
   ```
   
2. Launch Jupyter Notebook to run  `main.ipynb`:
   ```
    jupyter notebook
    ```
## Examples (Conceptual)

**Before Optimization:**

```
Write a Python function to calculate the factorial of a number.
```

**After Optimization:**

```
Write a Python function that computes the factorial of a given positive integer. The function should use recursion and include a base case for 0! = 1.
```

## License

This project is licensed under the MIT License.

## Status

🚧 This project is a work in progress. Expect frequent changes and improvements. 🚧

## Contact

For any inquiries or collaboration, reach out via sulavpokharel7@gmail.com.



