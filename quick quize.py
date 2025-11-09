#  Define an array of electronic components
components = ["Resistor", "Capacitor", "Inductor", "Diode", "Transistor"]

# Display the original array
print("Original List of Components:")
print(components)

# Append "LED" without using built-in function
new_component = "LED"
components_length = len(components)

# Increase the size of the array and add the new component
components = components + [None]  # Extend array by one space
components[components_length] = new_component  # Assign the new component to the last index

# Display the updated array
print("\nUpdated List of Components:")
print(components)

# Create an array of electronic components
electronic_components = ["Resistor", "Capacitor", "Inductor", "Diode", "Transistor"]

# Display the array items
print("Array of electronic components:")
for component in electronic_components:
    print(component)

# Access individual components through indices
print("\nAccessing individual components:")
for index in range(len(electronic_components)):
    print(f"Component at index {index}: {electronic_components[index]}")

# Example: Access specific components directly
print("\nExample access:")
print(f"The first component is: {electronic_components[0]}")
print(f"The last component is: {electronic_components[-1]}")