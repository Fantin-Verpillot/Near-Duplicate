def create_shingles(content, size):
    shingles = set()
    split_content = content.split()

    if len(split_content) < size:
        shingles.add(content)
        return shingles

    for i, token in enumerate(split_content):
        final_token = token
        if (i + size - 1) < len(split_content):
            for j in range(1, size):
                final_token += " " + split_content[i + j]
            shingles.add(final_token)
    return shingles


def generate_matrix(shingles):
    matrix = []
    for i in range(0, len(shingles)):
        matrix.append([])

    for i, set1 in enumerate(shingles):
        for set2 in shingles:
            matrix[i].append(dup(set1, set2))
    return matrix


def dup(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / float(union)
