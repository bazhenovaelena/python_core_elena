def create_time_checker(max_time):

    def checker(real_time):
        if real_time > max_time:
            print("Установленный лимит превышен")
        if real_time < max_time:
            print("Установленный лимит не превышен")

    return checker

create_time_checker(5)(10)
create_time_checker(9)(1)



