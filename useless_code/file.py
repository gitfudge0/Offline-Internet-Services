#!/usr/bin/python3

def main():
	out = ''
	f = open('output.txt')
	for line in f:
		out += line
	print(out)


if __name__ == '__main__':
	main()
