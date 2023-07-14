"""Question 2"""
def str_to_int(s):
    return int(s.encode().hex(), 16)

key = str_to_int("attack at dawn") ^ 0x09e1c5f70a65ac519458e7e53f36
print("Q2:")
print("  one time pad encryption = ",hex(str_to_int("attack at dusk") ^ key))