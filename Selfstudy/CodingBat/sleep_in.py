def count_code(str):
    i = 0
    count = 0
    while i < len(str) - 2:
        if str[i] == "o" and str[i - 1] == "c" and str[i + 2] == "e":
            count += count
        i += 1

    return count


print(count_code("codexxcode"))
