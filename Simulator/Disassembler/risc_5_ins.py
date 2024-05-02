type_R_dict = {             # No immediate number
    '0110011': {
        '010': {
            '0000000': 'SLT'
        },
        '001': {
            '0000000': 'SLL'
        },
        '101': {
            '0000000': 'SRL'
        },
        '000': {
            '0100000': 'SUB',
            '0000000': 'ADD'
        },
        '111': {
            '0000000': 'AND'
        },
        '110': {
            '0000000': 'OR'
        },
        '100': {
            '0000000': 'XOR'
        }
    }
}

type_I_dict = {             # imm_num = binary_list[0] + binary_list[1]
    '1100111': {
        '000':'JALR'        # signed offsets to register
    },

    '0010011': {
        '000': 'ADDI',      # sign-extended
        '010': 'SLTI'       # sign-extended
    },
    '0000011': {
        '010': 'LW'         # sign-extended signed offsets
    }
}

type_S_dict = {             # imm_num = binary_list[0] + binary_list[4]
    '0100011': {
        '010': 'SW'         # sign-extended signed offsets
    }
}

type_B_dict = {             # imm_num = binary_list[0][0] + binary_list[4][-1]
                            #         + binary_list[0][1:] + binary_list[4][:-1]
                            #         + ’0‘
    '1100011': {
        '000': 'BEQ',       # signed offsets
        '001': 'BNE',       # signed offsets
        '101': 'BGE',       # signed offsets
        '100': 'BLT',       # signed offsets
    },

}

type_U_dict = {
    
}

type_J_dict = {             # imm_num = binary_list[0][0] + binary_list[2]
                            #         + binary_list[3] + binary_list[1][-1]
                            #         + binary_list[0][1:] + binary_list[1][:-1]
                            #         + '0'
    '1101111': 'JAL'        # signed offsets
}