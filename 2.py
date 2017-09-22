import string
import re

'''
Return true iff input is a special character
'''
def findSpecial(token):
    dots = re.match("(\.)+", token)
    star = token == "*"
    return (dots or star)


def parse_path(path):
	tokens = path.split('\\')
	short_tokens = []
	i = len(tokens) - 1
	while(i >= 0):
		if findSpecial(tokens[i]):
			if(tokens[i] == '*'):
				break
			else:
				skipped = len(tokens[i]) - 1
				print skipped
				i -= skipped
		short_tokens = [tokens[i]] + short_tokens
		i -= 1
	return string.join(short_tokens, '\\')

def read_input():
	f = open('test.txt', 'r')
	for path in f:
		print path
		short_path = parse_path(path)
		print short_path


if __name__ == '__main__':
	read_input()