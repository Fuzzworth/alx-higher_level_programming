#!/usr/bin/python3
module_attributes = dir()

# Filter and print only the lines that don't start with "__"
filtered_attributes = [attr for attr in module_attributes if not attr.startswith('__')]
for attribute in filtered_attributes:
    print(attribute)
