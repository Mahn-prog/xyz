speed = int(input("Give Speed: "))

if speed < 50:
    print(f"Speeding ticket is 0 euros")
elif speed >= 50 and speed <= 64:
    print(f"Speeding ticket is 150 euros")
elif speed >= 65 and speed <= 74:
    print(f"Speeding ticket is 300 euros")
elif speed >= 75 and speed <= 84:
    print(f"Speeding ticket is 500  euros")
elif speed >= 85 and speed <= 89:
    print(f"Speeding ticket is 800  euros")
elif speed >= 90:
    print(f"Speeding ticket is 1200 euros")

def opposites(numbers: list):
    for i in range(len(numbers)):
        numbers[i] = -numbers[i]

words_count = {}
while True:
    word = input("Give word: ")
    if word != "":
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    else:
        break

word = max(words_count, key=words_count.get)
print("Most frequent word: " + word)

def join_lists(list1: list, list2: list):
    list3 = list1 + list2
    list4 = list(set(list3))
    list4.sort()
    return list4


def copy_correct():
    original_lines = []
    with open('source.txt') as source_file:
        original_lines = source_file.readlines()

    correct_lines = []
    for line in original_lines:
        stripped_line = line.strip()
        if stripped_line[0].isupper() and stripped_line.endswith('.'):
            correct_lines.append(stripped_line)

    with open('target.txt', 'w') as target_file:
        for correct_line in correct_lines:
            target_file.write(correct_line + '\n')
