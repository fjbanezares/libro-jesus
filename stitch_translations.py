
import sys

path = "/Users/fjbanezares/libro sobre mi amigo Jesucristo/output/html/00_introduccion.html"

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

spanish_content = read_file("spanish_intro.txt")
english_content = read_file("english_intro.txt")
french_content = read_file("french_intro.txt")
italian_content = read_file("italian_intro.txt")
arabic_content = read_file("arabic_intro.txt")
russian_content = read_file("russian_intro.txt")

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line numbers (1-indexed)
# Spanish: 545-662
# French: 665-689 (current messy block)
# Italian: 691-716 (current messy block)
# Chinese: 718-754 (keep this one as is, it's correct)
# Arabic: 756-781 (current messy block)
# Russian: 783-808 (current messy block)
# English: 810-924

# Indices (0-indexed)
spanish_start = 545 - 1
spanish_end = 662 - 1
french_start = 665 - 1
french_end = 689 - 1
italian_start = 691 - 1
italian_end = 716 - 1
chinese_start = 718 - 1
chinese_end = 754 - 1
arabic_start = 756 - 1
arabic_end = 781 - 1
russian_start = 783 - 1
russian_end = 808 - 1
english_start = 810 - 1
english_end = 924 - 1

new_lines = (
    lines[:spanish_start] + 
    [spanish_content + "\\n"] + 
    lines[spanish_end+1:french_start] + 
    [french_content + "\\n"] + 
    lines[french_end+1:italian_start] + 
    [italian_content + "\\n"] + 
    lines[italian_end+1:chinese_start] + 
    lines[chinese_start:chinese_end+1] + 
    lines[chinese_end+1:arabic_start] + 
    [arabic_content + "\\n"] + 
    lines[arabic_end+1:russian_start] + 
    [russian_content + "\\n"] + 
    lines[russian_end+1:english_start] + 
    [english_content + "\\n"] + 
    lines[english_end+1:]
)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Replacement complete.")
