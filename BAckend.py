import random
list1 = ["0","1","2","3","4","5","6","7","8","9"
         ,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
         ,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
         ,"!","@","#","$","%","^","&","*","(",")",",",".","?","/","\\","|"
        ]
list_limit = []
# val = [
#       {"name" : "Xuống dòng" , "ham"  }, 
#       {"name" : "Số phân tử (độ dài)", "ham" },
#       {"name" : "Mảng số (nguyên/thực)", "ham"},
#       {"name" : "Số ngẫu nhiên","ham"},
#       {"name" : "Kí tự" }
# ]
# for code
def resize(lst, new_size, default_value=None):
    current_size = len(lst)
    if new_size < current_size:
        return lst[:new_size]
    elif new_size > current_size:
        return lst + [default_value] * (new_size - current_size)
    else:
        return lst
list_limit = resize(list_limit,len(list1),1)


# random for app
def generate_ran_char(arr_value):
    return random.choice(arr_value)


def generate_ran_int(start , end):
    res = random.randint(start,end)
    return res


def generate_ran_float(start, end , so_chu_so):
    random_float = random.uniform(start, end)
    rounded_float = round(random_float, so_chu_so)
    return rounded_float

