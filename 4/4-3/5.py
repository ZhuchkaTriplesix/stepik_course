def pack_similar_chars(text):
    chars = text.split()

    if not chars:
        return []

    packed_list = []
    current_pack = [chars[0]]

    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            current_pack.append(chars[i])
        else:
            packed_list.append(current_pack)
            current_pack = [chars[i]]

    packed_list.append(current_pack)

    return packed_list


input_text = input()
result = pack_similar_chars(input_text)
print(result)
