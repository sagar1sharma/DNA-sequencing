import csv
import sys


def main():

    # TODO: Check for command-line usage
    if(len(sys.argv) != 3):
        print("Please type only 2 file names, First for database file and second sequence file")
        return

    # TODO: Read database file into a variable
    data_filePath = sys.argv[1]
    data = []

    with open(data_filePath, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(dict(row))


    # TODO: Read DNA sequence file into a variable
    sequence_filePath = sys.argv[2]
    to_check_data = []

    with open(sequence_filePath , 'r') as file:
        to_check_data = file.read()


    # TODO: Find longest match of each STR in DNA sequence
    map = {}
    for strs in data[0]:
        map[strs] = longest_match(to_check_data, strs)

    # TODO: Check database for matching profiles
    for record in data:
        flag = True
        for col in record:
            if(col != 'name'):
                if(int(record[col]) != int(map[col])):
                    flag = False
                    break
        if(flag):
            print(record['name'])
            return

    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
