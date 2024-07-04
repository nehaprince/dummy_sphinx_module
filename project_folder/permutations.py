import itertools

def generate_string_permutations(data):
    """
    Generate all permutations of a string.
    
    :param data: String to permute.
    :return: List of permutations as strings.
    """
    return [''.join(p) for p in itertools.permutations(data)]

# Example usage
data_string = input('Enter your name:')

permutations = generate_string_permutations(data_string)
print(permutations)