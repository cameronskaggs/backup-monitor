import sys
import warnings

# organizes the backup file into a dict where each key is a hash and their values are the file names
def format_file(file_path):
    file_dict = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(" ", 1)
                if len(parts) == 2:
                    sha1 = parts[0]
                    file_name = parts[1]
                    file_dict[sha1] = file_name
                else:
                    warnings.warn(f"Warning: file with hash {parts[0]} has no file name associated with it", RuntimeWarning)
        return file_dict

    except FileNotFoundError:
        print(f"Could not find file: {file_path}")
        return None

if __name__ == "__main__":
    old_file = "Old.sha1.txt"
    new_file = "New.sha1.txt"

    old_values = format_file(old_file)
    new_values = format_file(new_file)

    print(f"Old files {old_values}")
    print(f"New files {new_values}")