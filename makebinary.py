# Create a binary file with some random data
import os

def create_binary_file(filename, size):
    with open(filename, 'wb') as file:
        file.write(os.urandom(size))
    print("Binary file '{}' created with {} bytes.".format(filename, size))

# Usage example:
create_binary_file('test_binary_file.bin', 1024)  # Creates a binary file with 1 KB of random data