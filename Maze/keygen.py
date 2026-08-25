from z3 import *
import re
import ctypes

set_param('sat.threads', 4)
set_param('smt.threads', 4)


inp_letters_cond = "GVRXJ7SD9ZYFUQHK2B8LMNWP36E54CAT"
limit = 0x0204081020408101

# print([ord(val) for val in inp_letters_cond])


def natural_sort_key(d):
    # Splits the name by numbers and converts numeric parts into actual integers
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', d.name())]


x0 = BitVec('x0', 64)
x1 = BitVec('x1', 64)
x2 = BitVec('x2', 64)
x3 = BitVec('x3', 64)
x4 = BitVec('x4', 64)
x5 = BitVec('x5', 64)
x6 = BitVec('x6', 64)
x7 = BitVec('x7', 64)
x8 = BitVec('x8', 64)
x9 = BitVec('x9', 64)
x10 = BitVec('x10', 64)
x11 = BitVec('x11', 64)
x12 = BitVec('x12', 64)
x13 = BitVec('x13', 64)
x14 = BitVec('x14', 64)
x15 = BitVec('x15', 64)
x16 = BitVec('x16', 64)
x17 = BitVec('x17', 64)
x18 = BitVec('x18', 64)
x19 = BitVec('x19', 64)
x20 = BitVec('x20', 64)
x21 = BitVec('x21', 64)
x22 = BitVec('x22', 64)
x23 = BitVec('x23', 64)
x24 = BitVec('x24', 64)
x25 = BitVec('x25', 64)
x26 = BitVec('x26', 64)
x27 = BitVec('x27', 64)
x28 = BitVec('x28', 64)
x29 = BitVec('x29', 64)
x30 = BitVec('x30', 64)

variables = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24, x25, x26, x27, x28, x29, x30]

key = 0x811C9DC5

key = ((x0 ^ key) << 0) + ((x0 ^ key) << 1) + ((x0 ^ key) << 4) + ((x0 ^ key) << 7) + ((x0 ^ key) << 8) + ((x0 ^ key) << 24)
key = ((x1 ^ key) << 0) + ((x1 ^ key) << 1) + ((x1 ^ key) << 4) + ((x1 ^ key) << 7) + ((x1 ^ key) << 8) + ((x1 ^ key) << 24)
key = ((x2 ^ key) << 0) + ((x2 ^ key) << 1) + ((x2 ^ key) << 4) + ((x2 ^ key) << 7) + ((x2 ^ key) << 8) + ((x2 ^ key) << 24)
key = ((x3 ^ key) << 0) + ((x3 ^ key) << 1) + ((x3 ^ key) << 4) + ((x3 ^ key) << 7) + ((x3 ^ key) << 8) + ((x3 ^ key) << 24)
key = ((x4 ^ key) << 0) + ((x4 ^ key) << 1) + ((x4 ^ key) << 4) + ((x4 ^ key) << 7) + ((x4 ^ key) << 8) + ((x4 ^ key) << 24)
key = ((x5 ^ key) << 0) + ((x5 ^ key) << 1) + ((x5 ^ key) << 4) + ((x5 ^ key) << 7) + ((x5 ^ key) << 8) + ((x5 ^ key) << 24)
key = ((x6 ^ key) << 0) + ((x6 ^ key) << 1) + ((x6 ^ key) << 4) + ((x6 ^ key) << 7) + ((x6 ^ key) << 8) + ((x6 ^ key) << 24)
key = ((x7 ^ key) << 0) + ((x7 ^ key) << 1) + ((x7 ^ key) << 4) + ((x7 ^ key) << 7) + ((x7 ^ key) << 8) + ((x7 ^ key) << 24)
key = ((x8 ^ key) << 0) + ((x8 ^ key) << 1) + ((x8 ^ key) << 4) + ((x8 ^ key) << 7) + ((x8 ^ key) << 8) + ((x8 ^ key) << 24)
key = ((x9 ^ key) << 0) + ((x9 ^ key) << 1) + ((x9 ^ key) << 4) + ((x9 ^ key) << 7) + ((x9 ^ key) << 8) + ((x9 ^ key) << 24)
key = ((x10 ^ key) << 0) + ((x10 ^ key) << 1) + ((x10 ^ key) << 4) + ((x10 ^ key) << 7) + ((x10 ^ key) << 8) + ((x10 ^ key) << 24)
key = ((x11 ^ key) << 0) + ((x11 ^ key) << 1) + ((x11 ^ key) << 4) + ((x11 ^ key) << 7) + ((x11 ^ key) << 8) + ((x11 ^ key) << 24)
key = ((x12 ^ key) << 0) + ((x12 ^ key) << 1) + ((x12 ^ key) << 4) + ((x12 ^ key) << 7) + ((x12 ^ key) << 8) + ((x12 ^ key) << 24)
key = ((x13 ^ key) << 0) + ((x13 ^ key) << 1) + ((x13 ^ key) << 4) + ((x13 ^ key) << 7) + ((x13 ^ key) << 8) + ((x13 ^ key) << 24)
key = ((x14 ^ key) << 0) + ((x14 ^ key) << 1) + ((x14 ^ key) << 4) + ((x14 ^ key) << 7) + ((x14 ^ key) << 8) + ((x14 ^ key) << 24)
key = ((x15 ^ key) << 0) + ((x15 ^ key) << 1) + ((x15 ^ key) << 4) + ((x15 ^ key) << 7) + ((x15 ^ key) << 8) + ((x15 ^ key) << 24)
key = ((x16 ^ key) << 0) + ((x16 ^ key) << 1) + ((x16 ^ key) << 4) + ((x16 ^ key) << 7) + ((x16 ^ key) << 8) + ((x16 ^ key) << 24)
key = ((x17 ^ key) << 0) + ((x17 ^ key) << 1) + ((x17 ^ key) << 4) + ((x17 ^ key) << 7) + ((x17 ^ key) << 8) + ((x17 ^ key) << 24)
key = ((x18 ^ key) << 0) + ((x18 ^ key) << 1) + ((x18 ^ key) << 4) + ((x18 ^ key) << 7) + ((x18 ^ key) << 8) + ((x18 ^ key) << 24)
key = ((x19 ^ key) << 0) + ((x19 ^ key) << 1) + ((x19 ^ key) << 4) + ((x19 ^ key) << 7) + ((x19 ^ key) << 8) + ((x19 ^ key) << 24)
key = ((x20 ^ key) << 0) + ((x20 ^ key) << 1) + ((x20 ^ key) << 4) + ((x20 ^ key) << 7) + ((x20 ^ key) << 8) + ((x20 ^ key) << 24)
key = ((x21 ^ key) << 0) + ((x21 ^ key) << 1) + ((x21 ^ key) << 4) + ((x21 ^ key) << 7) + ((x21 ^ key) << 8) + ((x21 ^ key) << 24)
key = ((x22 ^ key) << 0) + ((x22 ^ key) << 1) + ((x22 ^ key) << 4) + ((x22 ^ key) << 7) + ((x22 ^ key) << 8) + ((x22 ^ key) << 24)
key = ((x23 ^ key) << 0) + ((x23 ^ key) << 1) + ((x23 ^ key) << 4) + ((x23 ^ key) << 7) + ((x23 ^ key) << 8) + ((x23 ^ key) << 24)
key = ((x24 ^ key) << 0) + ((x24 ^ key) << 1) + ((x24 ^ key) << 4) + ((x24 ^ key) << 7) + ((x24 ^ key) << 8) + ((x24 ^ key) << 24)
key = ((x25 ^ key) << 0) + ((x25 ^ key) << 1) + ((x25 ^ key) << 4) + ((x25 ^ key) << 7) + ((x25 ^ key) << 8) + ((x25 ^ key) << 24)
key = ((x26 ^ key) << 0) + ((x26 ^ key) << 1) + ((x26 ^ key) << 4) + ((x26 ^ key) << 7) + ((x26 ^ key) << 8) + ((x26 ^ key) << 24)
key = ((x27 ^ key) << 0) + ((x27 ^ key) << 1) + ((x27 ^ key) << 4) + ((x27 ^ key) << 7) + ((x27 ^ key) << 8) + ((x27 ^ key) << 24)
key = ((x28 ^ key) << 0) + ((x28 ^ key) << 1) + ((x28 ^ key) << 4) + ((x28 ^ key) << 7) + ((x28 ^ key) << 8) + ((x28 ^ key) << 24)
key = ((x29 ^ key) << 0) + ((x29 ^ key) << 1) + ((x29 ^ key) << 4) + ((x29 ^ key) << 7) + ((x29 ^ key) << 8) + ((x29 ^ key) << 24)
key = ((x30 ^ key) << 0) + ((x30 ^ key) << 1) + ((x30 ^ key) << 4) + ((x30 ^ key) << 7) + ((x30 ^ key) << 8) + ((x30 ^ key) << 24)

key = key & 0xFFFFFFFF 


s = Solver()

key = (((key << 30) + (key << 24) + (key << 23) + (key << 22) + (key << 18) + (key << 17) + (key << 14) + (key << 11) + (key << 10) + (key << 9) + (key << 6) + (key << 5) + (key << 3) + (key << 2) + key) + 0x3039)
check1 = (( key >> 0x10) & 0xFF) ^ 0x67
s.add(check1 == 0x45)

key = (((key << 30) + (key << 24) + (key << 23) + (key << 22) + (key << 18) + (key << 17) + (key << 14) + (key << 11) + (key << 10) + (key << 9) + (key << 6) + (key << 5) + (key << 3) + (key << 2) + key) + 0x3039)
check2 = (( key >> 0x10) & 0xFF) ^ 0xD3
s.add(check2 == 0x5A)

key = (((key << 30) + (key << 24) + (key << 23) + (key << 22) + (key << 18) + (key << 17) + (key << 14) + (key << 11) + (key << 10) + (key << 9) + (key << 6) + (key << 5) + (key << 3) + (key << 2) + key) + 0x3039)
check3 = (( key >> 0x10) & 0xFF) ^ 0x9B
s.add(check3 == 0x41)

key = (((key << 30) + (key << 24) + (key << 23) + (key << 22) + (key << 18) + (key << 17) + (key << 14) + (key << 11) + (key << 10) + (key << 9) + (key << 6) + (key << 5) + (key << 3) + (key << 2) + key) + 0x3039)
check4 = (( key >> 0x10) & 0xFF) ^ 0x96
s.add(check4 == 0x4D)


for var in variables:
    s.add(Or([var == ord(val) for val in inp_letters_cond]))



if s.check() == sat:
    m = s.model()

    for d in sorted(m.decls(), key=natural_sort_key):
        print(chr(m[d].as_long()),end="")
    
    print()

 