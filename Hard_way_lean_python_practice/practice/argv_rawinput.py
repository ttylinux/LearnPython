from sys import argv

script, user_name = argv
prompt = ':'

print('Hi, %s, I\'m the %s script.'%(user_name,script))
print('I\'d like to ask you a few questions.')
print('Do you like me %s?'%user_name)
likes = input(prompt)

