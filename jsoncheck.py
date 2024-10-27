import json
import sys

def load_json(file):
    with open(file, "r") as f:
        return json.load(f)

def save_json(data, file):
    with open(file, "w") as f:
        json.dump(data, f, indent=1)

def jsonchecker(inputf, outputf):
    try:
        json_data = load_json(inputf)
        save_json(json_data, outputf)
        print("JSON has been successfully fixed & saved as", outputf)
    except json.JSONDecodeError as e:
        print("Error while loading JSON:", e)
    except Exception as e:
        print("Random Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python jsoncheck.py <your_json_file> fixed.json")
    else:
        jsonchecker(sys.argv[1], sys.argv[2])
