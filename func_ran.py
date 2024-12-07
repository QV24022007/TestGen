from BAckend import generate_ran_char,generate_ran_int,generate_ran_float
import inspect
# def Xuongdong():
#    print()
def Do_dai_phan_tu(start,end):
   return (generate_ran_int(start,end))


def Mang_so(loop, start , end , kt , so_chu_so_thap_phan):
   res = []
   if(kt == False):
      for i in range(loop):
         res.append(generate_ran_int(start,end))
   if(kt == True):
      for i in range(loop):
         res.append(generate_ran_float(start,end,so_chu_so_thap_phan))
   return res
def ran_num(start,end,kt,so_chu_so_thap_phan):
   if(kt == False):
      res = generate_ran_int(start,end)
      return res
   if(kt == True):
      res = generate_ran_float(start,end,3)
      return res


def Ki_tu(arr_value):
   return (generate_ran_char(arr_value))


def Mang_ki_tu(loop , arr_value):
   res = []
   for i in range(loop):
      res.append(generate_ran_char(arr_value))
   return res

def So_bo_truy_van(start,end):
   return (generate_ran_int(start,end))


def Xau(loop , arr_value):
   for i in range(loop):
      res= res + generate_ran_char(arr_value)
   return res

