import os

# Specify the directory
directory = '/New folder'

# List all files and directories in the specified directory
contents = os.listdir(directory)

# Print the contents
for item in contents:
    print(item)
