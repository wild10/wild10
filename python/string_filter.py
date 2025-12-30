
def my_foo(s):
    alpha = "abcdefghijklmnñopqrstwxyzABCDEFIHIJKLMNÑOPQRSTUVWXYZ"
    re_s = ""
    for c in s:
        if c in alpha:
            re_s = re_s + c.lower()

    return re_s[::-1]

if __name__ == '__main__':
    s = "ABC13df"
    r = my_foo(s)
    print(r)

    re2 = ''.join([c.lower() for c in s if c.isalpha()])[::-1]
    print(re2)
