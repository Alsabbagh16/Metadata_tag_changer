import json
import os

def replace_metadata_name(json_file, new_name):
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Assuming the metadata name is under the "name" key, adjust as needed
    data['name'] = new_name

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)

def main():
    json_folder = "D:\Projects\Metadata_tag_changer\json"  # Replace with the actual path to your NFT JSON files
    names_file = "D:\Projects\Metadata_tag_changer\\names.txt"  # Replace with the actual path to your names text file

    with open(names_file, 'r') as names_file:
        new_names = [line.strip() for line in names_file.readlines()]

    # Ensure the number of names matches the number of JSON files
    if len(new_names) != 10:
        print("Error: The number of names does not match the number of JSON files.")
        return

    for i, json_file in enumerate(os.listdir(json_folder)):
        if json_file.endswith(".json"):
            json_path = os.path.join(json_folder, json_file)
            replace_metadata_name(json_path, new_names[i])
            print(f"Replaced name in {json_file} with: {new_names[i]}")

if __name__ == "__main__":
    main()
