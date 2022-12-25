import json

# Dictionary of states and capitals
states_and_capitals = {
  "Andhra Pradesh": "Amaravati",
  "Telangana": "Hyderabad",
  "Bihar": "Patna",
  "Goa": "Panaji",
  "Gujarat": "Gandhinagar",
  "Kerala": "Thiruvananthapuram",
  "Haryana": "Chandigarh"
  
}

# Open a file for writing
with open("indianStates.json", "w") as f:
  # Write the dictionary to the file in JSON format
  json.dump(states_and_capitals, f)
