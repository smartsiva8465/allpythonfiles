'''string='siva'
def fun(string):
  return string[::-1]
print(fun(string))
#word count
st='good evening siva prasad'
wordcount=1
for i in st:
    if i ==' ':
        wordcount=wordcount+1
print(wordcount)
#space count
spacecount=0
for i in st:
    if i ==' ':
        spacecount=spacecount+1
print(spacecount)
#
num=input('enter the number :')
def fun(num):
    return num[::-1]
print(fun(num))
#reverse numbers
num=int(input('enter the number :'))
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print(rev)'''
import struct

# Simulated memory (represents a small portion of RAM)
memory = bytearray(1024)  # 1 KB of memory

# Simulated disk (represents a bootable disk with a simple program)
disk = bytearray([
    0xB8, 0x00, 0x00,  # MOV AX, 0x0000
    0xBB, 0x00, 0x00,  # MOV BX, 0x0000
    0x01, 0xD8,        # ADD AX, BX
    0xF4,              # HLT (halt)
])

def load_bootloader():
    """Simulate loading a bootloader from disk into memory."""
    print("Loading bootloader from disk...")
    # Copy the first 512 bytes (simulated boot sector) from disk to memory
    memory[0:512] = disk[0:512]
    print("Bootloader loaded into memory.")

def execute_bootloader():
    """Simulate executing the bootloader."""
    print("Executing bootloader...")
    # Simulate CPU execution by interpreting the instructions in memory
    ip = 0  # Instruction pointer
    ax = 0  # Simulated CPU register AX
    bx = 0  # Simulated CPU register BX

    while ip < len(memory):
        opcode = memory[ip]
        if opcode == 0xB8:  # MOV AX, imm16
            ax = struct.unpack('<H', memory[ip+1:ip+3])[0]
            ip += 3
        elif opcode == 0xBB:  # MOV BX, imm16
            bx = struct.unpack('<H', memory[ip+1:ip+3])[0]
            ip += 3
        elif opcode == 0x01:  # ADD AX, BX
            ax = (ax + bx) & 0xFFFF  # Simulate 16-bit overflow
            ip += 2
        elif opcode == 0xF4:  # HLT
            print("CPU halted.")
            break
        else:
            print(f"Unknown opcode: {opcode:02X}")
            break

    print(f"Final AX register value: {ax:04X}")

def main():
    """Main function to simulate boot process."""
    load_bootloader()
    execute_bootloader()


if __name__ == "__main__":
    main()


