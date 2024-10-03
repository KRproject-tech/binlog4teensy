import numpy as np

def load_bin(file_name, dtype):
    # Open the file in binary read mode
    with open(file_name, 'rb') as file:
        # Read the entire file into a numpy array with specified dtype
        data = np.fromfile(file, dtype=dtype)
    
    # 数値データ行数カウント (Count the number of columns)
    idx = 1
    while data[idx] != data[0]:
        idx += 1
    N_col = idx - 1
    
    # 数値データ配列生成 (Generate the data matrix)
    N_data = len(data)
    N_row = N_data // (1 + N_col)
    
    # Reshape the data to form rows and columns
    out = data[:N_row * (1 + N_col)].reshape(N_row, 1 + N_col)
    
    # Remove the first column (header column) and return the result
    out = out[:, 1:]
    
    return out
