
def output_hex(inp):
    return hex(inp)


entry_point = 0x51B69
raw_entry_point = 0x51B69 - 0x1000 + 0x600

virtual_byte_code_offset = 0x50050

pe_dict = {}


byte_code_offset = raw_entry_point - (entry_point - virtual_byte_code_offset)
ip = 0

mem = [0] * 0x14
base_addr = 0x0000000140000000

opcode_count = {}

tmp_count = 0

with open("C:\\<<PATH>>\\LvHaMaze.exe", "rb") as file:

    while True:

        file.seek(byte_code_offset + ip)
        opcode = int.from_bytes(file.read(0x1), byteorder="little")

        if opcode == 0xcc:
            file.seek(byte_code_offset + ip + 1)
            mem_idx = int.from_bytes(file.read(0x1), byteorder="little")
            file.seek(byte_code_offset + ip + 2)

            _bytes = file.read(0x8)

            val = int.from_bytes(_bytes, byteorder="little")

            _bytes_out = "".join(f"{b:02x}" for b in _bytes)
            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx:02x}", _bytes_out), end="\t\t")
            print("mov qword ptr ss:[{}], {}".format(hex(mem_idx), hex(val)))

            mem[mem_idx] = val

            ip = ip + 0xA
            
        elif opcode == 0x19:
            file.seek(byte_code_offset + ip + 1)
            mem_idx1 = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            mem_idx2 = int.from_bytes(file.read(0x1), byteorder="little")

            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx1:02x}", f"{mem_idx2:02x}"), end="\t\t\t")
            print("mov qword ptr ss:[{}], qword ptr ss:[{}]".format(hex(mem_idx1), hex(mem_idx2)), end="\t\t")
            print("// qword ptr ss:[{}] values is {}".format(hex(mem_idx2), hex(mem[mem_idx2])))

            mem[mem_idx1] = mem[mem_idx2]

            ip = ip + 0x3
        
        elif opcode == 0x27:
            file.seek(byte_code_offset + ip + 1)
            mem_idx1 = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            mem_idx2 = int.from_bytes(file.read(0x1), byteorder="little")

            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx1:02x}", f"{mem_idx2:02x}"), end="\t\t\t")
            print("sub qword ptr ss:[{}], qword ptr ss:[{}]".format(hex(mem_idx1), hex(mem_idx2)), end="\t\t")
            print("// qword ptr ss:[{}] values is {}, qword ptr ss:[{}] values is {}".format(hex(mem_idx1), hex(mem[mem_idx1]), hex(mem_idx2), hex(mem[mem_idx2])))

            mem[mem_idx1] = mem[mem_idx1] - mem[mem_idx2]

            ip = ip + 3
        
        elif opcode == 0x93:
            file.seek(byte_code_offset + ip + 1)
            mem_idx1 = int.from_bytes(file.read(0x1), byteorder="little")

            print(hex(opcode))

            print("cmp qword ptr ss:[{}], 0x0".format(hex(mem_idx1)))
            if mem[mem_idx1] == 0x0:
                file.seek(byte_code_offset + ip + 2)
                mem_idx2 = int.from_bytes(file.read(0x2), byteorder="little", signed=True)

                ip = ip + mem_idx2

                print("ip inc to {}. since res is true".format(hex(mem_idx2)))
            else:
                ip = ip + 4
                print("ip inc to 4. since res is false")
            

        elif opcode == 0xC8:
            file.seek(byte_code_offset + ip + 1)
            mem_idx = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            _bytes = file.read(0x4)
            operand = int.from_bytes(_bytes, byteorder="little")

            _bytes_out = "".join(f"{b:02x}" for b in _bytes)

            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx:02x}", _bytes_out), end="\t\t\t")
            print("imul qword ptr ss:[{}], {}".format(hex(mem_idx), hex(operand)), end="\t\t\t\t")
            print("// qword ptr ss:[{}] values is {}".format(hex(mem_idx1), hex(mem[mem_idx1])))


            mem[mem_idx] = operand * mem[mem_idx]

            ip = ip + 6
        elif opcode == 0xF5:
            file.seek(byte_code_offset + ip + 1)
            mem_idx1 = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            mem_idx2 = int.from_bytes(file.read(0x1), byteorder="little")


            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx1:02x}", f"{mem_idx2:02x}"), end="\t\t\t")
            print("add qword ptr ss:[{}], qword ptr ss:[{}]".format(hex(mem_idx1), hex(mem_idx2)), end="\t\t")
            print("// qword ptr ss:[{}] values is {}, qword ptr ss:[{}] values is {}".format(hex(mem_idx1), hex(mem[mem_idx1]), hex(mem_idx2), hex(mem[mem_idx2])))


            mem[mem_idx1] = mem[mem_idx1] + mem[mem_idx2]

            ip = ip + 3

        elif opcode == 0x44:
            file.seek(byte_code_offset + ip + 1)
            mem_idx1 = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            mem_idx2 = int.from_bytes(file.read(0x1), byteorder="little")


            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx1:02x}", f"{mem_idx2:02x}"), end="\t\t\t")

            print("mov rax, {}".format(hex(base_addr)))

            print("\t\t\t\t\t\tadd rax, qword ptr ss:[{}]".format(hex(mem_idx2)), end="\t\t\t\t")
            print("// qword ptr ss:[{}] value is {}".format(hex(mem_idx2), hex(mem[mem_idx2])))

            file.seek(raw_entry_point - (entry_point - mem[mem_idx2]))
            val = int.from_bytes(file.read(0x1), byteorder="little")
            print("\t\t\t\t\t\tmovzx eax, byte ptr ds:[rax]", end="\t\t\t\t")
            print("// byte ptr ds:[rax] value is {}".format(hex(val)))

            print("\t\t\t\t\t\tmov qword ptr ss:[{}], rax".format(hex(mem_idx1)))

            mem[mem_idx1] = val

            ip = ip + 3


        elif opcode == 0x17:
            file.seek(byte_code_offset + ip + 1)
            mem_idx = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            _bytes = file.read(0x4)
            operand = int.from_bytes(_bytes, byteorder="little")

            _bytes_out = "".join(f"{b:02x}" for b in _bytes)


            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx:02x}", _bytes_out), end="\t\t\t")
            print("add qword ptr ss:[{}], {}".format(hex(mem_idx), hex(operand)), end="\t\t\t\t")
            print("// qword ptr ss:[{}] values is {}".format(hex(mem_idx), hex(mem[mem_idx])))


            mem[mem_idx] = mem[mem_idx] + operand

            ip = ip + 6

        elif opcode == 0xA1:

            file.seek(byte_code_offset + ip + 1)
            mem_idx1 = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            mem_idx2 = int.from_bytes(file.read(0x1), byteorder="little")

            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx1:02x}", f"{mem_idx2:02x}"), end="\t\t\t")
            print("xor qword ptr ss:[{}], qword ptr ss:[{}]".format(hex(mem_idx1), hex(mem_idx2)), end="\t\t")
            print("// qword ptr ss:[{}] values is {}, qword ptr ss:[{}] values is {}".format(hex(mem_idx1), hex(mem[mem_idx1]), hex(mem_idx2), hex(mem[mem_idx2])))

            mem[mem_idx1] = mem[mem_idx1] ^ mem[mem_idx2]

            ip = ip + 0x3
        
        elif opcode == 0x7B:
            file.seek(byte_code_offset + ip + 1)
            mem_idx = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            _bytes = file.read(0x4)
            operand = int.from_bytes(_bytes, byteorder="little")

            _bytes_out = "".join(f"{b:02x}" for b in _bytes)


            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx:02x}", _bytes_out), end="\t\t\t")
            print("and qword ptr ss:[{}], {}".format(hex(mem_idx), hex(operand)), end="\t\t\t\t")
            print("// qword ptr ss:[{}] values is {}".format(hex(mem_idx), hex(mem[mem_idx])))


            mem[mem_idx] = mem[mem_idx] & operand

            ip = ip + 6
        elif opcode == 0xB7:

            file.seek(byte_code_offset + ip + 1)
            mem_idx = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            operand = int.from_bytes(file.read(0x1), byteorder="little")

            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx1:02x}", f"{operand:02x}"), end="\t\t\t")
            print("rol qword ptr ss:[{}], {}".format(hex(mem_idx), hex(operand)), end="\t\t\t\t")
            print("// qword ptr ss:[{}] value is {}".format(hex(mem_idx), hex(mem[mem_idx])))

            # (x >> (8 - n)) | ((x << n) & 0xFF)
            mem[mem_idx] = (mem[mem_idx] >> (8 - operand)) | ((mem[mem_idx] << operand) & 0xFF)

            ip = ip + 3
        elif opcode == 0xE4:
            file.seek(byte_code_offset + ip + 1)
            mem_idx1 = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            mem_idx2 = int.from_bytes(file.read(0x1), byteorder="little")

            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx1:02x}", f"{mem_idx2:02x}"), end="\t\t\t")
            
            print("mov rcx, qword ptr ss:[{}]".format(hex(mem_idx1)), end="\t\t\t\t")
            print("// qword ptr ss:[{}] value is {}".format(hex(mem_idx1), hex(mem[mem_idx1])))

            print("\t\t\t\t\t\tmov rax, qword ptr ss:[{}]".format(hex(mem_idx2)), end="\t\t\t\t")
            print("// qword ptr ss:[{}] value is {}".format(hex(mem_idx2), hex(mem[mem_idx2])))
            
            print("\t\t\t\t\t\tadd rax, {}".format(hex(base_addr)))
            
            print("\t\t\t\t\t\tmov byte ptr ds:[rax], cl")

            pe_dict[base_addr + mem[mem_idx2]] = mem[mem_idx1]

            ip = ip + 3


        elif opcode == 0x52:
            file.seek(byte_code_offset + ip + 1)
            mem_idx1 = int.from_bytes(file.read(0x1), byteorder="little")

            file.seek(byte_code_offset + ip + 2)
            mem_idx2 = int.from_bytes(file.read(0x1), byteorder="little")

            print("{}\t\t{} {} {}".format(hex(ip), f"{opcode:02x}", f"{mem_idx1:02x}", f"{mem_idx2:02x}"), end="\t\t\t")
            print("imul qword ptr ss:[{}], qword ptr ss:[{}]".format(hex(mem_idx1), hex(mem_idx2)), end="\t\t")
            print("// qword ptr ss:[{}] values is {}, qword ptr ss:[{}] values is {}".format(hex(mem_idx1), hex(mem[mem_idx1]), hex(mem_idx2), hex(mem[mem_idx2])))

            mem[mem_idx1] = mem[mem_idx1] * mem[mem_idx2]

            ip = ip + 0x3

        elif opcode == 0x3B:
            file.seek(byte_code_offset + ip + 1)
            val = int.from_bytes(file.read(0x2), byteorder="little", signed=True)

            print("{}\t\t{} {}".format(hex(ip), f"{opcode:02x}", f"{val:04x}"), end="\t\t\t\t")
            print("jmp [rip + {}] ".format(hex(val)))

            print(ip)
            ip = ip + val
            break
        else:
            print(hex(opcode))

            for i in range(len(mem)):

                if i % 8 == 0:
                    print()

                print(f"0x{mem[i]:08x}", end=" ")

            break
        
        print()


    print("test")



    ## rdx is rip