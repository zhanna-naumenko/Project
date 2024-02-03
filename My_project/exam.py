from utils import unzip_with_7z


zip_file_path = 'congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 

# WRITE YOUR CODE BELOW
# ----------------------------------------

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for first_char in letters:
    for second_char in letters:
        secret_password = first_char + second_char + 'bcmpda'
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            break


