from Back_end_version2 import generate_random_numbers,random_string
Combo_list = []
from func_ran import Do_dai_phan_tu,Ki_tu,Mang_ki_tu
def SO_NGAU_NHIEN(limit, decimal_places = None, even = False , odd = False , perfect_square = False , prime = False):
    # RES
    return random_number(min_value = limit[0],max_value = limit[1], decimal_places = decimal_places, perfect_square = perfect_square  , prime = prime ,  even = even , odd = odd)
def XAU_KI_TU(limit,length , spaces_in_middle = 0 , spaces_at_start = 0, forbidden_start_chars = None):
    # RES
    return random_string(list_value = limit , length = length, spaces_in_middle = spaces_in_middle , spaces_at_start= spaces_at_start , forbidden_start_chars = forbidden_start_chars)
def KI_TU(VALUE_ARR):
    # RES
    return Ki_tu(VALUE_ARR)
def MANG_KI_TU(limit,LOOP):
    return Mang_ki_tu(LOOP,limit)
def XUONG_DONG():
    return " "
def SO_PHAN_TU(limit):
    # RES
    return Do_dai_phan_tu(limit[0],limit[1])


value_of_array_in_test = ["0"]
Checkbox_list = []

Func_limit_list = []
class FuncItem:
    def __init__(self, name, gt_graph = None,ham=None, limit=None, gt=None, loop=None, decimal_places=None, unique=None,
                 ascending=None, descending=None, odd_only=None, even_only=None, even=None, odd=None,
                 perfect_square=None, prime=None, length=None, spaces_in_middle=None, spaces_at_start=None,
                 forbidden_start_chars=None, limit1=None, limit2=None, end_line=None, no_zero=None,
                 common_diff_range=None, arithmetic_progression=None, min_word_length=None, max_word_length=None,
                 min_spaces_in_middle=None, max_spaces_in_middle=None, min_spaces_at_start=None, max_spaces_at_start=None,
                 multi_word=None, combine_previous=None, previous_string=None, hide_or_show=None,type = None,vtq_start = None , vtq_end = None,
                 num_vertices = None, num_edges = None, directed = None, allow_self_loops = None, allow_repeated_edges = None,connected = None,weighted = None,min_weight = None,
                 min_num_edges = None, max_num_edges = None,max_weight = None, graph_type = None):
        
        self.gt_graph = gt_graph
        self.num_vertices = num_vertices
        self.num_edges = num_edges
        self.directed = directed
        self.allow_self_loops = allow_self_loops
        self.allow_repeated_edges = allow_repeated_edges
        self.connected = connected
        self.weighted = weighted
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.graph_type = graph_type
        self.vtq_start = vtq_start
        self.vtq_end = vtq_end
        self.name = name
        self.ham = ham
        self.type = type
        self.limit = limit
        self.gt = gt
        self.loop = loop
        self.decimal_places = decimal_places
        self.unique = unique
        self.ascending = ascending
        self.descending = descending
        self.odd_only = odd_only
        self.even_only = even_only
        self.even = even
        self.odd = odd
        self.perfect_square = perfect_square
        self.prime = prime
        self.length = length
        self.spaces_in_middle = spaces_in_middle
        self.spaces_at_start = spaces_at_start
        self.forbidden_start_chars = forbidden_start_chars
        self.limit1 = limit1
        self.limit2 = limit2
        self.end_line = end_line
        self.no_zero = no_zero
        self.common_diff_range = common_diff_range
        self.arithmetic_progression = arithmetic_progression
        self.min_word_length = min_word_length
        self.max_word_length = max_word_length
        self.min_spaces_in_middle = min_spaces_in_middle
        self.max_spaces_in_middle = max_spaces_in_middle
        self.min_spaces_at_start = min_spaces_at_start
        self.max_spaces_at_start = max_spaces_at_start
        self.multi_word = multi_word
        self.combine_previous = combine_previous
        self.previous_string = previous_string
        self.hide_or_show = hide_or_show


Func_list = [
    FuncItem(name="Xuống dòng", gt = "\n"),
    FuncItem(name="Số phân tử (độ dài)", limit=None, gt=None,hide_or_show = None, ham=SO_PHAN_TU),
    FuncItem(name="Mảng số (nguyên/thực)", limit=None, loop=None, decimal_places=None, unique=None, 
             ascending=None, descending=None, odd_only=None, even_only=None,end_line = None, no_zero = None,
             common_diff_range = None , arithmetic_progression = None,
             ham=generate_random_numbers, gt=[]),
    FuncItem(name="Số ngẫu nhiên", limit=None, even=None, odd=None, perfect_square=None, prime=None, decimal_places = None,
             ham=SO_NGAU_NHIEN, gt=None),
    FuncItem(name="Xâu kí tự", limit = None,length = None , ham = random_string ,min_word_length = None , max_word_length = None, 
            min_spaces_in_middle = None, max_spaces_in_middle = None, min_spaces_at_start = None ,max_spaces_at_start = None, forbidden_start_chars = None ,
            multi_word = None, combine_previous = None, previous_string = None),
    FuncItem(name="Kí tự", limit=None, ham=KI_TU, gt=""),
    FuncItem(name="Mảng kí tự", limit=None, loop=None, ham=MANG_KI_TU, gt=[]),
    FuncItem(name="Số bộ truy vấn", limit=[None, None]),
    FuncItem(name="Bắt đầu truy vấn", limit=[None, None]),
    FuncItem(name="Kết thúc truy vấn", limit=[None, None]),
]