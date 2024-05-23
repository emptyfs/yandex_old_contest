class RacketManager:

    @staticmethod
    def get_times(racket_info):
        racket_info = sorted(racket_info, key=lambda s: tuple(map(int, s.split()[:3])))
        log_dict = {}

        for racket in racket_info:
            splited_info = racket.split()
            racked_id = splited_info[3]
            racket_status = splited_info[4]

            temp_list = splited_info[:3]

            if not racked_id in log_dict:
                temp_list.append('0')
                log_dict[racked_id] = temp_list
            elif racket_status == 'A':
                temp_list.append(log_dict[racked_id][3])
                log_dict[racked_id] = temp_list   
            elif racket_status == 'S' or racket_status == 'C' or racket_status == 'B':
                spended_time = RacketManager.time_counter(log_dict[racked_id][:3], splited_info[:3])
                temp_list.append(str(int(log_dict[racked_id][3]) + spended_time))
                log_dict[racked_id] = temp_list

        log_dict =  dict(sorted(log_dict.items(), key=lambda item: int(item[0]))) 
        return ' '.join([value[-1] for value in log_dict.values()])

    @staticmethod
    def time_counter(time_dict1, time_dict2):
        days = int(time_dict2[0])-int(time_dict1[0])
        hours = int(time_dict2[1])-int(time_dict1[1])
        minutes = int(time_dict2[2])-int(time_dict1[2])

        return days*24*60 + hours*60 + minutes



N = input()
print(RacketManager.get_times([input() for i in range(int(N))]))