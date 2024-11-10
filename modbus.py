COMMANDS = [
    "mask_write_register",
    "read_coils",
    "read_discrete_inputs",
    "read_holding_registers",
    "read_input_registers",
    "readwrite_registers",
    "write_multiple_coils",
    "write_multiple_registers",
    "write_single_coil",
    "write_single_register",
]


class ModbusEmulator:
    def __init__(self):
        self.coils = [False] * 100  # Simulated coils (0-99)
        self.discrete_inputs = [True] * 100  # Simulated discrete inputs (0-99)
        self.holding_registers = [0] * 100  # Simulated holding registers (0-99)
        self.input_registers = [1] * 100  # Simulated input registers (0-99)

    def read_coils(self, address, count):
        return self.coils[address : address + count]

    def read_discrete_inputs(self, address, count):
        return self.discrete_inputs[address : address + count]

    def read_holding_registers(self, address, count):
        return self.holding_registers[address : address + count]

    def read_input_registers(self, address, count):
        return self.input_registers[address : address + count]

    def write_single_coil(self, address, value):
        if 0 <= address < len(self.coils):
            self.coils[address] = value
            return True
        return False

    def write_single_register(self, address, value):
        if 0 <= address < len(self.holding_registers):
            self.holding_registers[address] = value
            return True
        return False

    def write_multiple_coils(self, address, values):
        if 0 <= address < len(self.coils) and (address + len(values)) <= len(
            self.coils
        ):
            self.coils[address : address + len(values)] = values
            return True
        return False

    def write_multiple_registers(self, address, values):
        if 0 <= address < len(self.holding_registers) and (
            address + len(values)
        ) <= len(self.holding_registers):
            self.holding_registers[address : address + len(values)] = values
            return True
        return False

    def mask_write_register(self, address, and_mask, or_mask):
        if 0 <= address < len(self.holding_registers):
            original_value = self.holding_registers[address]
            new_value = (original_value & and_mask) | (or_mask & ~and_mask)
            self.holding_registers[address] = new_value
            return new_value
        return None

    def readwrite_registers(
        self, read_address, read_count, write_address, write_values
    ):
        read_values = self.read_holding_registers(read_address, read_count)
        write_result = self.write_multiple_registers(write_address, write_values)
        return read_values if write_result else None


# # Testing the Modbus Emulator
emulator = ModbusEmulator()

COMMAND_DICT = output_dict = {
    "read_coils": f"Read Coils: {emulator.read_coils(0, 5)}",
    "read_discrete_inputs": f"Read Discrete Inputs: {emulator.read_discrete_inputs(10, 5)}",
    "read_holding_registers": f"Read Holding Registers: {emulator.read_holding_registers(20, 3)}",
    "read_input_registers": f"Read Input Registers: {emulator.read_input_registers(30, 2)}",
    "write_single_coil": f"Write Single Coil Result: {emulator.write_single_coil(5, True)}",
    "write_single_register": f"Write Single Register Result: {emulator.write_single_register(15, 123)}",
    "write_multiple_coils": f"Write Multiple Coils Result: {emulator.write_multiple_coils(10, [True, False, True])}",
    "write_multiple_registers": f"Write Multiple Registers Result: {emulator.write_multiple_registers(25, [456, 789])}",
    "mask_write_register": f"Mask Write Register Result: {emulator.mask_write_register(5, 0xF0F0, 0x0F0F)}",
    "readwrite_registers": f"Read/Write Multiple Registers Result: {emulator.readwrite_registers(40, 2, 50, [111, 222])}",
}

# # Example usage:
# print("Read Coils:", emulator.read_coils(0, 5))
# print("Read Discrete Inputs:", emulator.read_discrete_inputs(10, 5))
# print("Read Holding Registers:", emulator.read_holding_registers(20, 3))
# print("Read Input Registers:", emulator.read_input_registers(30, 2))
# print("Write Single Coil Result:", emulator.write_single_coil(5, True))
# print("Write Single Register Result:", emulator.write_single_register(15, 123))
# print(
#     "Write Multiple Coils Result:",
#     emulator.write_multiple_coils(10, [True, False, True]),
# )
# print(
#     "Write Multiple Registers Result:",
#     emulator.write_multiple_registers(25, [456, 789]),
# )
# print("Mask Write Register Result:", emulator.mask_write_register(5, 0xF0F0, 0x0F0F))
# print(
#     "Read/Write Multiple Registers Result:",
#     emulator.readwrite_registers(40, 2, 50, [111, 222]),
# )
