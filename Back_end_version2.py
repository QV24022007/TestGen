import random
import string


import random

import random

import random

def random_string(list_value, length, min_word_length=1, max_word_length=5, 
                  min_spaces_in_middle=0, max_spaces_in_middle=0, min_spaces_at_start=0, max_spaces_at_start=0, 
                  forbidden_start_chars=None, multi_word=False, combine_previous=False, previous_string=""):
    
    # Đặt giá trị mặc định nếu các biến là None
    if min_word_length is None:
        min_word_length = 1
    if max_word_length is None:
        max_word_length = 5
    if min_spaces_in_middle is None:
        min_spaces_in_middle = 0
    if max_spaces_in_middle is None:
        max_spaces_in_middle = 0
    if min_spaces_at_start is None:
        min_spaces_at_start = 0
    if max_spaces_at_start is None:
        max_spaces_at_start = 0
    if list_value is None or not list_value:
        list_value = list('abcdefghijklmnopqrstuvwxyz')  # Sử dụng bảng chữ cái nếu không có danh sách nào
    
    # Randomize the spaces at start
    spaces_at_start = random.randint(min_spaces_at_start, max_spaces_at_start)
    
    # Remove forbidden start characters if applicable
    available_chars = list_value
    if forbidden_start_chars:
        available_chars = [c for c in available_chars if c not in forbidden_start_chars]
    
    # Start the result with spaces at the start
    result = ' ' * spaces_at_start
    
    # Handle multi-word case
    if multi_word:
        words = []
        total_length = 0
        
        # Generate multiple words until total length is reached
        while total_length < length:
            word_length = random.randint(min_word_length, max_word_length)
            word = ''.join(random.choice(available_chars) for _ in range(word_length))
            words.append(word)
            total_length += len(word) + 1  # Adding 1 for the space
            
            if total_length >= length:
                break
        
        # Remove the last space if it exceeds the specified length
        if total_length > length:
            words[-1] = words[-1][:len(words[-1]) - (total_length - length)]
        
        # Add spaces between words
        num_spaces_in_middle = random.randint(min_spaces_in_middle, max_spaces_in_middle)
        result += (' ' * num_spaces_in_middle).join(words)
    
    else:
        # Single word case
        result += ''.join(random.choice(available_chars) for _ in range(length))
    
    # Combine with previous string if specified
    if combine_previous:
        result = previous_string + result
    
    return result



# list_value = list("abcdefghijklmnopqrstuvwxyz")
# for i in range(2):
#     print(random_string(list_value, length=20, min_word_length=3, max_word_length=6, 
#                     min_spaces_in_middle=1, max_spaces_in_middle=2, 
#                     multi_word=True, combine_previous=True, previous_string="\n"))



# Ví dụ sử dụng hàm:
length = 10  # Độ dài của chuỗi
spaces_in_middle = 0  # Số khoảng trắng ngẫu nhiên ở giữa
spaces_at_start = 0  # Số khoảng trắng ở đầu
forbidden_start_chars = ['a', 'b', 'c']  # Các ký tự không được phép bắt đầu chuỗi
list1 = ["0","1","2","3","4","5","6","7","8","9"
     ,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
     ,"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
     ,"!","@","#","$","%","^","&","*","(",")",",",".","?","/","\\","|"
    ]
# generated_string = random_string(list1,length,spaces_in_middle,  spaces_at_start , forbidden_start_chars)
# print("Chuỗi ngẫu nhiên tạo ra:", repr(generated_string))
# # # import random

import random

def generate_random_numbers(
    loop,                      # Kích thước mảng
    one_per_line=False,         # True nếu muốn mỗi phần tử trên 1 dòng
    decimal_places=None,        # Số chữ số thập phân (None = số nguyên)
    unique=False,               # True nếu không được trùng lặp
    ascending=False,            # True nếu mảng tăng dần
    descending=False,           # True nếu mảng giảm dần
    odd_only=False,             # True nếu chỉ toàn số lẻ
    even_only=False,            # True nếu chỉ toàn số chẵn
    no_zero=False,              # True nếu không có số 0 trong mảng
    arithmetic_progression=False,# True nếu mảng theo cấp số cộng
    common_diff_range=(1, 10),  # Khoảng giá trị cho công sai khi cấp số cộng
    min_value=1,                # Giá trị nhỏ nhất của số
    max_value=100               # Giá trị lớn nhất của số
):
    numbers = set() if unique else []

    # Hàm hỗ trợ để đảm bảo mảng không có số 0 nếu yêu cầu
    def is_valid(num):
        if no_zero and num == 0:
            return False
        return True

    # Xử lý nếu yêu cầu cấp số cộng
    if arithmetic_progression:
        first_term = random.randint(min_value, max_value)
        common_diff = random.randint(*common_diff_range)
        numbers = [first_term + i * common_diff for i in range(loop)]
        if unique:
            numbers = list(set(numbers))  # Loại bỏ trùng lặp nếu cần
    else:
        # Tạo số ngẫu nhiên dựa trên các điều kiện
        while len(numbers) < loop:
            if decimal_places is not None:
                num = round(random.uniform(min_value, max_value), decimal_places)
            else:
                if odd_only:
                    num = random.choice(range(min_value | 1, max_value + 1, 2))  # Chọn số lẻ
                elif even_only:
                    num = random.choice(range(min_value + (min_value % 2), max_value + 1, 2))  # Chọn số chẵn
                else:
                    num = random.randint(min_value, max_value)
            
            # Kiểm tra nếu yêu cầu không có số 0 và trùng lặp
            if not is_valid(num):
                continue
            
            if unique and num in numbers:
                continue  # Nếu yêu cầu không trùng lặp, bỏ qua số đã có

            if unique:
                numbers.add(num)
            else:
                numbers.append(num)

    # Chuyển từ set sang list nếu unique=True
    if unique and not arithmetic_progression:
        numbers = list(numbers)

    # Sắp xếp nếu yêu cầu tăng/giảm dần
    if ascending:
        numbers.sort()
    elif descending:
        numbers.sort(reverse=True)

    # Nếu yêu cầu in mỗi số trên 1 dòng thì lưu chúng dưới dạng chuỗi
    if one_per_line:
        numbers = [str(num) for num in numbers]

    return numbers




# # Ví dụ sử dụng:
# size = 3  # Kích thước của mảng
# decimal_places = None  # Số chữ số thập phân (None nếu muốn số nguyên)
# one_per_line = False  # In ra mỗi phần tử 1 dòng
# unique = False  # Không cho phép trùng lặp
# ascending = False  # Không sắp xếp tăng dần
# descending = False  # Sắp xếp giảm dần
# odd_only = False  # Không giới hạn chỉ số lẻ
# even_only = False  # Toàn số chẵn
# no_zero = False 
# common_diff_range = False
# generate_random_numbers(no_zero = True,size = 5, one_per_line = one_per_line, decimal_places = None, unique = False, ascending = True, descending = False, odd_only = False, even_only = False,common_diff_range = (2,3),arithmetic_progression = True )



# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Hàm random số với các ràng buộc
def random_number(
    decimal_places=None,  # Số chữ số thập phân (None = số nguyên)
    even=False,           # True nếu chỉ muốn số chẵn
    odd=False,            # True nếu chỉ muốn số lẻ
    perfect_square=False, # True nếu muốn số chính phương
    prime=False,          # True nếu muốn số nguyên tố
    min_value=1,          # Giá trị nhỏ nhất
    max_value=100         # Giá trị lớn nhất
):
    if prime:
        # Sinh số nguyên tố
        while True:
            num = random.randint(min_value, max_value)
            if is_prime(num):
                break
    elif perfect_square:
        # Sinh số chính phương
        min_root = math.ceil(math.sqrt(min_value))
        max_root = math.floor(math.sqrt(max_value))
        if min_root > max_root:
            raise ValueError("Không có số chính phương trong khoảng cho trước.")
        num = random.randint(min_root, max_root) ** 2
    else:
        if decimal_places is not None:
            # Sinh số thực
            num = round(random.uniform(min_value, max_value), decimal_places)
        else:
            # Sinh số nguyên
            if even:
                num = random.choice(range(min_value + (min_value % 2), max_value + 1, 2))  # Số chẵn
            elif odd:
                num = random.choice(range(min_value | 1, max_value + 1, 2))  # Số lẻ
            else:
                num = random.randint(min_value, max_value)  # Số nguyên bất kỳ
    
    return num



def random_edge_count(num_vertices, min_edges, max_edges, directed=False, graph_type="random"):
    """
    Generate a random number of edges for a graph based on constraints.
    
    Parameters:
        num_vertices (int): Number of vertices in the graph.
        min_edges (int): Minimum number of edges allowed.
        max_edges (int): Maximum number of edges allowed.
        directed (bool): Whether the graph is directed.
        graph_type (str): Type of graph ("random", "tree", "grid", "cycle").
    
    Returns:
        int: Randomly generated number of edges.
    """
    # Calculate the theoretical limits for edges
    if directed:
        max_possible_edges = num_vertices * (num_vertices - 1)  # Directed graph
    else:
        max_possible_edges = num_vertices * (num_vertices - 1) // 2  # Undirected graph

    # Adjust the range for valid edge counts
    min_edges = max(min_edges, 0)
    max_edges = min(max_edges, max_possible_edges)

    # Graph type adjustments
    if graph_type == "tree":
        # A tree has exactly (num_vertices - 1) edges
        edge_count = max(0, num_vertices - 1)
    elif graph_type == "grid":
        # Estimate edges for a grid graph
        side_length = int(num_vertices**0.5)  # Assume roughly square grid
        edge_count = max(0, (2 * side_length * (side_length - 1)))
    elif graph_type == "cycle":
        # A cycle has exactly num_vertices edges
        edge_count = num_vertices if num_vertices > 2 else 0
    else:  # "random" or unspecified type
        # Generate a random number of edges within the range
        edge_count = random.randint(min_edges, max_edges)

    # Ensure the edge count does not exceed limits
    edge_count = max(min_edges, min(edge_count, max_edges))
    return edge_count






def generate_graph(
    num_vertices,                  # Số đỉnh
    num_edges,                     # Số cạnh
    directed=True,                 # True nếu là đồ thị có hướng
    allow_self_loops=False,        # True nếu cho phép cạnh nối đỉnh với chính nó
    allow_repeated_edges=False,    # True nếu cho phép nhiều cạnh giữa 2 đỉnh
    connected=False,               # True nếu yêu cầu đồ thị liên thông
    weighted=False,                # True nếu đồ thị có trọng số
    min_weight=1,                  # Trọng số nhỏ nhất
    max_weight=10,                 # Trọng số lớn nhất
    graph_type="random"            # Loại đồ thị: "random", "tree", "grid", "cycle"
):
    edges = []

    def add_edge(u, v):
        """Thêm cạnh (u, v) vào đồ thị."""
        if weighted:
            weight = random.randint(min_weight, max_weight)
            edges.append([u, v, weight])
        else:
            edges.append([u, v])

    # Điều chỉnh số cạnh phù hợp với dạng đồ thị
    if graph_type == "tree":
        num_edges = num_vertices - 1
    elif graph_type == "cycle":
        num_edges = num_vertices
    elif graph_type == "grid":
        grid_size = int(num_vertices ** 0.5)
        if grid_size ** 2 != num_vertices:
            raise ValueError("Grid graph requires num_vertices to be a perfect square.")
        num_edges = 2 * num_vertices - 2 * grid_size  # Công thức tính số cạnh lưới

    # Tạo đồ thị dạng cây
    if graph_type == "tree":
        for i in range(1, num_vertices):
            u = i
            v = random.randint(0, i - 1)
            add_edge(u, v)

    # Tạo đồ thị dạng chu trình
    elif graph_type == "cycle":
        for i in range(num_vertices):
            add_edge(i, (i + 1) % num_vertices)

    # Tạo đồ thị dạng lưới
    elif graph_type == "grid":
        grid_size = int(num_vertices ** 0.5)
        for i in range(grid_size):
            for j in range(grid_size):
                current = i * grid_size + j
                if i < grid_size - 1:
                    add_edge(current, current + grid_size)  # Dòng dọc
                if j < grid_size - 1:
                    add_edge(current, current + 1)  # Dòng ngang

    # Tạo đồ thị ngẫu nhiên
    else:
        edge_count = 0
        while edge_count < num_edges:
            u = random.randint(0, num_vertices - 1)
            v = random.randint(0, num_vertices - 1)
            if u == v and not allow_self_loops:
                continue
            if not allow_repeated_edges and [u, v] in edges:
                continue
            add_edge(u, v)
            edge_count += 1

    # Đảm bảo đồ thị liên thông nếu yêu cầu
    if connected:
        parent = list(range(num_vertices))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for i in range(1, num_vertices):
            u = i
            v = random.randint(0, i - 1)
            if find(u) != find(v):
                add_edge(u, v)
                union(u, v)
    return edges
def random_vertices_edges(min_vertices, max_vertices, min_edges, max_edges, directed):
    """
    Hàm random số đỉnh và số cạnh cho đồ thị với ràng buộc min-max.
    
    Args:
        min_vertices (int): Số đỉnh tối thiểu.
        max_vertices (int): Số đỉnh tối đa.
        min_edges (int): Số cạnh tối thiểu.
        max_edges (int): Số cạnh tối đa.
        directed (bool): True nếu là đồ thị có hướng, False nếu là đồ thị vô hướng.
    
        Returns:
        tuple: (số đỉnh, số cạnh)
    """
    # Random số đỉnh
    num_vertices = random.randint(min_vertices, max_vertices)
    
    # Tính số cạnh tối đa thực sự dựa trên số đỉnh và loại đồ thị
    if directed:
        max_possible_edges = num_vertices * (num_vertices - 1)  # Không tính self-loop
    else:
        max_possible_edges = (num_vertices * (num_vertices - 1)) // 2  # Vô hướng

    # Điều chỉnh giá trị min_edges và max_edges để nằm trong khoảng hợp lệ
    min_edges = max(0, min_edges)
    max_edges = min(max_possible_edges, max_edges)
    
    if min_edges > max_edges:
        raise ValueError("Không thể random số cạnh thỏa mãn điều kiện min_edges và max_edges.")
    
    # Random số cạnh
    num_edges = random.randint(min_edges, max_edges)
    
    return num_vertices, num_edges

# generate_graph(
#     num_vertices = 10,                  # Số đỉnh
#     num_edges = 7,                     # Số cạnh
#     directed=False,                # True nếu là đồ thị có hướng
#     allow_self_loops=False,        # True nếu cho phép cạnh nối đỉnh với chính nó
#     allow_repeated_edges=False,    # True nếu cho phép nhiều cạnh giữa 2 đỉnh
#     connected=False,               # True nếu yêu cầu đồ thị liên thông
#     weighted=False,                # True nếu đồ thị có trọng số
#     min_weight=1,                  # Trọng số nhỏ nhất
#     max_weight=10,                 # Trọng số lớn nhất
#     graph_type="cycle")
# print(generate_graph(
#     num_vertices = 10,                  # Số đỉnh
#     num_edges = 7,                     # Số cạnh
#     directed=False,                # True nếu là đồ thị có hướng
#     allow_self_loops=False,        # True nếu cho phép cạnh nối đỉnh với chính nó
#     allow_repeated_edges=False,    # True nếu cho phép nhiều cạnh giữa 2 đỉnh
#     connected=False,               # True nếu yêu cầu đồ thị liên thông
#     weighted=True,                # True nếu đồ thị có trọng số
#     min_weight=1,                  # Trọng số nhỏ nhất
#     max_weight=10,                 # Trọng số lớn nhất

# num_vertices=15
# num_edges=8
# directed=False
# graph_type="random"
# weighted=True
# min_weight=10
# max_weight=100
# graph = generate_graph(
#     num_vertices=num_vertices,
#     num_edges=num_edges,
#     directed=directed,
#     graph_type=graph_type,
#     weighted=weighted,
#     min_weight=min_weight,
#     max_weight=max_weight
# )


# for value in graph:
#     for value2 in value:
#         print(value2 , end =" ")
#     print()


# # Hiển thị kết quả
# if weighted:
#     edges, weights = graph
#     print(f"Số đỉnh: {num_vertices}, Số cạnh: {len(edges)}")
    # for (u, v) in edges:
    #     print(f"{u} {v} {weights[(u, v)]}")
# else:
#     edges = graph
#     print(f"Số đỉnh: {num_vertices}, Số cạnh: {len(edges)}")
#     for (u, v) in edges:
#         print(f"{u} {v}")