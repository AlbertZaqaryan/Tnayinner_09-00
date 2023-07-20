# def delete_sharps(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.readlines()
#         for i in res:
#             if i[0] == '#':
#                 res.remove(i)
#         s = ''
#         for i in res:
#             s += i
#         with open(filename, 'w') as file:
#             file.write(s)
#         return 'Good open file :)'
#     except FileNotFoundError:
#         return 'No file'
    
# filename = input('Enter filename: ')
# print(delete_sharps(filename))
# -------------------------------------------------------
# import random

# def generate_random_password(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#         res = res.split('\n')
#         while True:
#             s1 = random.choice(res)
#             s2 = random.choice(res)
#             if len(s1) < 3 or len(s2) < 3:
#                 continue
#             else:
#                 if 8 <= len(s1 + s2) <= 10:
#                     return f'{s1.title()}{s2.title()}'
#                 else:
#                     continue
#     except FileNotFoundError:
#         return 'No file'
    
# filename = input('Enter filename: ')
# print(generate_random_password(filename))        
# -------------------------------------------------------
# def find_max_word(filename):
#     try:
#         with open(filename, 'r') as file:
#             res = file.read()
#         res = res.split('\n')
#         res = ' '.join(res)
#         for i in res:
#             if i in '!@#$%^&*()_-+=:;"<,>.?/':
#                 res = res.replace(i, ' ')
#         res = res.split(' ')
#         mydict = {i:res.count(i) for i in res}
#         mydict.pop('')
#         return {i:mydict[i] for i in sorted(mydict, key=mydict.get, reverse=True)[:1]}
#     except FileNotFoundError:
#         return 'No file'
    
# filename = input('Enter filename: ')
# print(find_max_word(filename))
# -------------------------------------------------------
