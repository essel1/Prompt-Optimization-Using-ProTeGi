import cohere

# Initialize Cohere client with your API key
cohere_api_key = '7DNoxjgNM7h9ffV8WGcQYPnsggQUUhq2UYywfk3Z'
co = cohere.Client(cohere_api_key)

# Make an API call to generate text
response = co.generate(
    model='command-r-plus',  # You can choose a different model size
    prompt='''
   from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    ''',
    max_tokens=100,
    temperature=0.7
)

# Output the generated text
print(response.generations[0].text)
