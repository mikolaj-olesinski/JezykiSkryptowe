def odwr(zdanie):
    slowa = zdanie.split()
    slowa_odwrocone = slowa[::-1]
    return " ".join(slowa_odwrocone)



def most_common_element(lst):
    
    counted = {elem: ["x" for x in lst if  x == elem] for elem in lst}
    return sorted(counted, key=lambda x: len(counted[x]), reverse=True)[0] if counted else None


def pierwiastek(x, epsilon=0.1):

    def pierw_recursive(x, y, epsilon):
        next_y = (y + x / y) / 2
        return y if abs(y**2 - x) < epsilon else pierw_recursive(x, next_y, epsilon)

    return 0 if x == 0 else None if x < 0 else pierw_recursive(x, x/2, epsilon)


def make_alpha_dict(sentence):
    splited_sentence = sentence.split()

    unique_chars = [char for word in splited_sentence for char in word if char.isalpha()]
    unique_chars = set(unique_chars)
    alpha_dict = {char: [word for word in splited_sentence if char in word] for char in unique_chars}

    return alpha_dict



def flatten(lst):
    match lst:
        case []:
            return []
        case [head, *tail]:
            return flatten(head) + flatten(tail)
        case _:
            return [lst]

def flatten_v2(lst):
    return [elem for list_ in lst for elem in (flatten(list_) if isinstance(list_, list) else [list_])]


print('odwr("To jest przykladowe zdanie"): ', odwr("To jest przykladowe zdanie"))
print('odwr(""): ', odwr(""))
print('odwr("AAAA"): ', odwr("AAAA"))

print()
print('most_common_element([1, 1, 19, 2, 3, 4, 4, 5, 1]): ', most_common_element([1, 1, 19, 2, 3, 4, 4, 5, 1]))
print('most_common_element([1, 1, 1, 1, 1, 1, 1, 1, 1]): ', most_common_element([1, 1, 1, 1, 1, 1, 1, 1, 1]))
print('most_common_element([1, 2, 3, 4, 5, 6, 7, 8, 9]): ', most_common_element([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print('most_common_element([]): ', most_common_element([]))

print()
print('pierwiastek(3, 0.1): ', pierwiastek(3, 0.1))
print('pierwiastek(-5, 0.1): ',pierwiastek(-5, 0.1))
print('pierwiastek(0, 0.1): ',pierwiastek(0, 0.1))
print('pierwiastek(4, 0.1): ',pierwiastek(4, 0.1))

print()
print('make_alpha_dict("on i ona"): ', make_alpha_dict("on i ona"))
print('make_alpha_dict(""): ', make_alpha_dict(""))
print('make_alpha_dict("a b c d"): ', make_alpha_dict("a b c d"))

print()
print('flatten([1, [2, 3], [[4, 5], 6]]): ', flatten(flatten([1, [2, 3], [[4, 5], 6]])))
print('flatten([1, 2, 3, 4, 5, 6]): ', flatten([1, 2, 3, 4, 5, 6]))
print('flatten([]): ', flatten([]))

