# Belajar Casting / Merubah dari satu tipe ke tipe data lain
# Bisa disebut Konversi Tipe Data
# Tipe Data = int, float, str, bool

# Integer
print("===== Integer =====")
data_int = 9
print("data = ", data_int, " Type = ", type(data_int))
# Operator Casting
data_float  = float(data_int)   # int konversi ke float
data_str    = str(data_int)     # int konversi ke String
data_bool   = bool(data_int)    # int konversi ke boolean
print("data = ", data_float, " Type = ", type(data_float))
print("data = ", data_str, " Type = ", type(data_str))
# hasilnya True karena nilainya 9, 
# kalau nilainya 0 maka menjadi false.
# 0 akan False
# Diluar dari 0 akan True
print("data = ", data_bool, " Type = ", type(data_bool))

# Float
print("\n===== Float =====")
data_float = 9.9
print("data = ", data_float, " Type = ", type(data_float))
# Operator Casting
data_int  = int(data_float)    # float konversi ke int
data_str    = str(data_float)  # float konversi ke String
data_bool   = bool(data_float) # float konversi ke boolean
print("data = ", data_int, " Type = ", type(data_int))
print("data = ", data_str, " Type = ", type(data_str))
print("data = ", data_bool, " Type = ", type(data_bool))

# Boolean
print("\n===== Boolean =====")
data_bool = True
print("data = ", data_bool, " Type = ", type(data_bool))
# Operator Casting
data_int    = int(data_bool)   # boolean konversi ke int
data_str    = str(data_bool)   # boolean konversi ke String
data_float  = float(data_bool) # boolean konversi ke float
print("data = ", data_int, " Type = ", type(data_int))
print("data = ", data_str, " Type = ", type(data_str))
print("data = ", data_float, " Type = ", type(data_float))

# String
print("\n===== String =====")
# String faisal tidak bisa diubah menjadi integer
# String 10 / angka lainnya bisa diubah menjadi integer
data_str = "1"
# Apabila ingin String ke boolean jadi false maka ubah String menjadi kosong
print("data = ", data_str, " Type = ", type(data_str))
# Operator Casting
data_int    = int(data_str)   # String konversi ke int
data_bool    = bool(data_str)   # String konversi ke Boolean
data_float  = float(data_str) # String konversi ke float
print("data = ", data_int, " Type = ", type(data_int))
print("data = ", data_bool, " Type = ", type(data_bool))
print("data = ", data_float, " Type = ", type(data_float))