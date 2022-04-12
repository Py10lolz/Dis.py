# Dis Interpreter in python
import sys
DIS_INSTR = '*^>|}{!_'

def op(a, b):
	result = 0
	for i in range(10):
		result += (((a//3**i)%3-(b//3**i)%3)%3)*3**i
	return result
def rotate(n): return n//3 + (n%3)*3**9
def initialize(txt):
	c = 0
	mem = []
	if txt > 3**10:
		raise Exception("Code size must be smaller than {3**10}")
	while c < len(txt):
		if txt[c].isspace():
			pass
		elif txt[c] in DIS_INSTR:
			mem.append(ord(txt[c]))
		elif txt[c] == "(":
			while txt[c] != ")":
				c += 1
		else:
			raise Exception("invalid char at {c}: {txt[c]}")
		c += 1
	return mem + [0] * (3**10 - len(mem))
def interpreter(mem):
	A = C = D = 0
	while 1:
		instr = chr(mem[C])
		if instr == "*":
			D = mem[D]
		elif instr == "^":
			C = mem[D]
		elif instr == ">":
			mem[D] = A = rotate(mem[D])
		elif instr == "|":
			mem[D] = A = op(A, mem[D])
		elif instr == "}":
			input = sys.stdin.read(1)
			A = ord(input) if input else 3**10 - 1
		elif instr == "{":
			if A = 3**10 - 1:
				return
			else:
				print(chr(A%256), end='')
		elif instr == "!":
			return
		C, D = (C+1)%(3**10), (D+1)%(3**10)
with open(argv[1], "r") as f:
	txt = f.read()
	interpreter(initialize(txt))