

# function that calculates minimum edit distance between two strings based on a dynamic programming
# memoization table
def min_edit_dist(word1, word2):
    # create DP memoization matrix to store number of operations required to transform string word1 into word2
    table = [[0 for x in range(len(word1)+1)] for y in range(len(word2)+1)]
    # assign zero to top-left-most corner cell of table, which corresponds to the case
    # when we have no char to either replace, delete or insert in none of the strings
    table[0][0] = 0
    # if we are on the first row of table, just copy previous count to current count added to one,
    # since all we're doing is adding next char of first string to it, for there is
    # no corresponding character of string 2 to compare to
    for j in range(1, len(word1)+1):
        table[0][j] = table[0][j-1] + 1
    # conversely, if we are at the left-most column of table, we take the count from the cell right above current one,
    # add one to it and paste the result on the current cell, for we don't need to perform any operation
    # on second string but solely add its next character to it,
    # since we're trying to match chars of string 2 against a blank
    # char of string 1 (0 on very top of table column)
    for i in range(1, len(word2)+1):
        table[i][0] = table[i-1][0] + 1
    for i in range(1, len(word2)+1):
        for j in range(1, len(word1)+1):
            if word2[i - 1] == word1[j - 1]:
                # if chars match in both strings,
                # just copy number of operations from cell diagonally left above from table,
                # since we do not need to perform any operation on strings when characters are the same
                table[i][j] = table[i - 1][j - 1]
            else:
                # otherwise take minimum among left cell, top cell or diagonal cell above current one;
                # no need to implement own minimum function here, since we're always comparing only 3 items
                # at a time cost O(1)
                table[i][j] = min(table[i][j - 1], table[i - 1][j], table[i - 1][j - 1]) + 1
    return table[len(table)-1][len(table[0])-1]


n, m = (int(x) for x in input().split())

dictionary = ['' for x in range(n)]
words = ['' for x in range(m)]

for x in range(n):
    dictionary[x] = input()

for x in range(m):
    words[x] = input()

for word in words:
    output_string = ""
    for dictionary_word in dictionary:
        # add word to output only if edit distance to dictionary entry less than 3
        if min_edit_dist(dictionary_word, word) < 3:
            output_string += dictionary_word + " "
    print(output_string[:-1])
















