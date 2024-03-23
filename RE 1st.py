import re

def main():
   
    text = "The quick brown fox jumps over the lazy dog."


    pattern = r'fox'

    match = re.search(pattern, text)
    if match:
        print("Pattern found:", match.group())
    else:
        print("Pattern not found")

    matches = re.findall(pattern, text)
    print("All occurrences of the pattern:")
    for match in matches:
        print(match)

    new_text = re.sub(pattern, 'wolf', text)
    print("Text after replacement:", new_text)

if __name__ == "__main__":
    main()
