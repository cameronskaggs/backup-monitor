import sys
import warnings
import argparse

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
            not_in_file.append(sha1_hash)
    return not_in_file

# will create the OldNotInNew.txt and NewNotInOld.txt files. Will throw exception if either file exists already
def create_not_in_file(not_in_file_list, file_dict, file_name):

    with open(file_name, 'x') as f:
        for sha1_hash in not_in_file_list:
            f.write(file_dict[sha1_hash] + "\r\n")

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--oldfile', nargs='?', default="Old.sha1.txt")
    parser.add_argument('-n', '--newfile', nargs='?', default="New.sha1.txt" )
    parser.add_argument('-or', '--oldresultfile', nargs='?', default="OldNotInNew.txt" )
    parser.add_argument('-nr', '--newresultfile', nargs='?', default="NewNotInOld.txt" )
    
    args = parser.parse_args()

    old_values = format_file(args.oldfile)
    new_values = format_file(args.newfile)

    old_not_in_new_hash_list = get_list_of_hashes_not_in_file(old_values, new_values)
    new_not_in_old_hash_list = get_list_of_hashes_not_in_file(new_values, old_values)

    create_not_in_file(old_not_in_new_hash_list, old_values, args.oldresultfile)
    create_not_in_file(new_not_in_old_hash_list, new_values, args.newresultfile)