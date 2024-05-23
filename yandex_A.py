import string

class Encryption():

    @staticmethod
    def encryption(candidates_info):
        can_list = []

        for candidate in candidates_info:
            splited_info = candidate.split(',')
            uniq_count = Encryption.unique_characters(''.join(splited_info[:3]))
            dig_sum = Encryption.digits_sum(''.join(splited_info[3:5]))
            alp_num = Encryption.alphabet_number(splited_info[0][0])

            encry = hex(uniq_count + dig_sum * 64 + alp_num * 256)[2:]
            encry = '00' + encry
            encry = encry[-3:]
            can_list.append(encry.upper())
            
        return ' '.join(can_list)
    
    @staticmethod
    def alphabet_number(text):
        return int(string.ascii_lowercase.index(text.lower())) + 1

    @staticmethod
    def unique_characters(text):
        set_char = set()
        for j in [i for i in text]:
            set_char.add(j)
        return(len(set_char))

    @staticmethod
    def digits_sum(text):
        return sum(map(int, text))



N = input()
print(Encryption.encryption([input() for i in range(int(N))]))
