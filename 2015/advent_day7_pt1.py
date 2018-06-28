import re
import sys

def get_wire(input_value):
    try:
        int(input_value)
        return int(input_value)
    except ValueError:
        if callable(wires[input_value]):
            wires[input_value] = wires[input_value]()
        return wires[input_value]

class Gate:
    def __init__(self, first_input, operator, shift_bits, second_input):
        #check if first input is constant or wire ID
        self.first_input = first_input
        self.operator = operator
        self.shift_bits = shift_bits
        self.second_input = second_input
        if operator:
            self.output = getattr(self, 'logic_{}'.format(operator))
        else:
            try:
                int(first_input)
                self.output = self.logic_CONST
            except ValueError:
                self.output = self.logic_JOIN

    def logic_AND(self):
        print(self.first_input, 'AND', self.second_input)
        return get_wire(self.first_input) & get_wire(self.second_input)

    def logic_OR(self):
        print(self.first_input, 'OR', self.second_input)
        return get_wire(self.first_input) | get_wire(self.second_input)

    def logic_NOT(self):
        #0xFFFF used to mask the higher bits
        print('NOT', self.second_input)
        return (~get_wire(self.second_input)) & 0xFFFF

    def logic_RSHIFT(self):
        print('RSHIFT', self.first_input, 'by', self.shift_bits, 'bits')
        return (get_wire(self.first_input) >> int(self.shift_bits)) & 0xFFFF

    def logic_LSHIFT(self):
        print('LSHIFT', self.first_input, 'by', self.shift_bits, 'bits')
        return (get_wire(self.first_input) << int(self.shift_bits)) & 0xFFFF

    def logic_JOIN(self):
        print('Getting signal of wire',self.first_input)
        return wires[self.first_input]()

    def logic_CONST(self):
        print('Consant signal', self.first_input)
        return int(self.first_input)

wires = {}

def get_signal(wire_id):
    return wires[wire_id]()

'''
Group 1: first input to gate (wire id OR constant)
Group 2: operator, if given
Group 3: SHIFT gate bits, if given
Group 4: second input to gate (wire id OR constant), if given
Group 5: output wire id of gate
'''
instruction_pattern = re.compile(r'([a-z]+|[0-9]+)? ?([A-Z]+)? ?([0-9]+)? ?([a-z]+|[0-9]+)? -> ([a-z]+)')

for instruction in sys.stdin:
    result = re.match(instruction_pattern, instruction)
    
    first_input = result.group(1)
    operator = result.group(2)
    shift_bits = result.group(3)
    second_input = result.group(4)
    output = result.group(5)

    wires[output] = Gate(first_input, operator, shift_bits, second_input).output

print(get_signal('a'))