def run_assembly_simulation(code_text: str):
    # 1. Initialize 32 MIPS registers (R0 to R31) with value 0
    registers = {f"R{i}": 0 for i in range(32)}
    memory = {}  # for sw

    # Split assembly code into lines and initialize Program Counter (PC)
    lines = code_text.strip().split("\n")
    pc = 0

    # Instruction execution loop
    while pc < len(lines):
        line = lines[pc].strip()
        pc += 1  # Increment PC to point to the next line by default

        # Skip empty lines or comments
        if not line or line.startswith("#"):
            continue

        # Clean line commas and split into instruction parts
        parts = line.replace(",", "").split()
        if not parts:
            continue

        opcode = parts[0].upper()

        # 1. R-TYPE INSTRUCTIONS (Register-to-Register)
        if opcode in ["ADD", "SUB", "AND", "OR", "XOR", "SLT"]:
            rd, rs, rt = parts[1], parts[2], parts[3]
            val_rs = registers.get(rs, 0)
            val_rt = registers.get(rt, 0)

            if opcode == "ADD":
                registers[rd] = val_rs + val_rt
            elif opcode == "SUB":
                registers[rd] = val_rs - val_rt
            elif opcode == "AND":
                registers[rd] = val_rs & val_rt
            elif opcode == "OR":
                registers[rd] = val_rs | val_rt
            elif opcode == "XOR":
                registers[rd] = val_rs ^ val_rt
            elif opcode == "SLT":  # Set on Less Than (1 if rs < rt, else 0)
                registers[rd] = 1 if val_rs < val_rt else 0

        # 2. I-TYPE INSTRUCTIONS (Immediate & Memory)
        elif opcode in ["ADDI", "ANDI", "ORI", "LW", "SW", "BEQ"]:
            if opcode == "ADDI":
                rd, rs, imm = parts[1], parts[2], int(parts[3])
                registers[rd] = registers.get(rs, 0) + imm

            elif opcode == "ANDI":
                rd, rs, imm = parts[1], parts[2], int(parts[3])
                registers[rd] = registers.get(rs, 0) & imm

            elif opcode == "ORI":
                rd, rs, imm = parts[1], parts[2], int(parts[3])
                registers[rd] = registers.get(rs, 0) | imm

            elif opcode == "SW":  # Store Word: e.g., SW R1, 100(R0)
                rt = parts[1]
                offset_and_rs = parts[2].split("(")
                offset = int(offset_and_rs[0])
                rs = offset_and_rs[1].replace(")", "")

                address = registers.get(rs, 0) + offset
                memory[str(address)] = registers.get(rt, 0)

            elif opcode == "LW":  # Load Word: e.g., LW R1, 100(R0)
                rt = parts[1]
                offset_and_rs = parts[2].split("(")
                offset = int(offset_and_rs[0])
                rs = offset_and_rs[1].replace(")", "")

                address = registers.get(rs, 0) + offset
                registers[rt] = memory.get(str(address), 0)

            elif opcode == "BEQ":  # Branch if Equal: e.g., BEQ R1, R2, target_line
                rs, rt, target_line = parts[1], parts[2], int(parts[3])
                if registers.get(rs, 0) == registers.get(rt, 0):
                    pc = target_line  # Jump to target line


        # 3. J-TYPE INSTRUCTIONS (Jump)
        elif opcode == "J":  # Unconditional Jump: e.g., J target_line
            target_line = int(parts[1])
            pc = target_line  # Jump directly to target line

    # Filter registers to return only non-zero registers for cleaner response
    non_zero_registers = {k: v for k, v in registers.items() if v != 0}

    return {
        "status": "Simulation completed successfully",
        "registers": non_zero_registers,
        "memory": memory,
    }