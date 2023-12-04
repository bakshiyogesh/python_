# with open('zen-of-python.txt','w') as f:
#     contents=f.writelines('Name is the file directory for saving world from demons like you.')
#     # saved_content=f.readlines()
#     f.writelines('Beautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.')
# f.close()

with open('zen-of-python.txt','r') as f:
    contents=f.readlines()
    # saved_content=f.readlines()
f.close()
print(contents)

#Example for reading text line by line
with open('zen-of-python.txt','r') as f:
    while True:
        line=f.readline()
        if not line:
            break
        print(line.strip())

# if you’re dealing with other languages such as Japanese, Chinese, and Korean, the text file is not a simple ASCII text file. And it’s likely a UTF-8 file that uses more than just the standard ASCII text characters.

# To open a UTF-8 text file, you need to pass the encoding='utf-8' to the open() function to instruct it to expect UTF-8 characters from the file.

#$$$$Example
# with open('quotes.txt', encoding='utf8') as f:
#     for line in f:
#         print(line.strip())
quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'

with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write(quote)

# 'x' – open a file for exclusive creation. If the file exists, the open() function raises an error (FileExistsError). Otherwise, it’ll create the text file.

# When processing files, you’ll often want to check if a file exists before doing something else with it such as reading from the file or writing to it.
# To do it, you can use the exists() function from the os.path module or is_file() method from the Path class in the pathlib module.

#First method 
from os.path import exists as file_exists
file_exists('readme.txt')

# Second Method to check
from pathlib import Path

path_to_file = 'readme.txt'
path = Path(path_to_file)

if path.is_file():
    print(f'The file {path_to_file} exists')
else:
    print(f'The file {path_to_file} does not exist')