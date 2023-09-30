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
                    sha1_hash = parts[0]
                    file_name = parts[1]
                    file_dict[sha1_hash] = file_name
                else:
                    warnings.warn(f"Warning: file with hash {parts[0]} has no file name associated with it", RuntimeWarning)
        return file_dict

    except FileNotFoundError:
        print(f"Could not find file: {file_path}")
        return None

# returns a list of the hashes in file_1 which aren't in file_2
def get_list_of_hashes_not_in_file(file_1, file_2):
    not_in_file = []

    for sha1_hash in file_1:
        if sha1_hash not in file_2:
            print (sha1_hash)
            not_in_file.append(sha1_hash)
    return not_in_file

# will create the OldNotInNew.txt and NewNotInOld.txt files. Will throw exception if either file exists already
def create_not_in_file(not_in_file_list, file_dict, file_name):

    with open(file_name, 'x') as f:
        for sha1_hash in not_in_file_list:
            f.write(file_dict[sha1_hash] + "\n")

if __name__ == "__main__":
    old_file = "Old.sha1.txt"
    new_file = "New.sha1.txt"

    old_values = format_file(old_file)
    new_values = format_file(new_file)

    print(f"Old files {old_values}")
    print(f"New files {new_values}")

    old_not_in_new_hash_list = get_list_of_hashes_not_in_file(old_values, new_values)
    new_not_in_old_hash_list = get_list_of_hashes_not_in_file(new_values, old_values)

    print(f"Old not in new{old_not_in_new_hash_list}")
    print(f"New not in old{new_not_in_old_hash_list}")

    create_not_in_file(old_not_in_new_hash_list, old_values, 'OldNotInNew.txt')
    create_not_in_file(new_not_in_old_hash_list, new_values, 'NewNotInOld.txt')