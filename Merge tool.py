def merge_the_tools(string, k):
    # your code goes here
    new_str = ''
    seen = 0

    for char in string:
        if char not in new_str:
            new_str += char
        seen += 1

        if seen == k:
            seen = 0
            print(new_str)
            new_str = ''


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)