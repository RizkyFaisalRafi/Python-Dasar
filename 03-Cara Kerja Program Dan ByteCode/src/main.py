""" Multiline Comment
Python adalah Bahasa pemrograman yang interpreter langsung dijalankan 
tanpa compile :
Source Code -> Python / Interpreted -> Terminal / Dijalankan 
"""
import time
start_time = time.time()

print("Hallo Dunia")
print("Aku Ganteng Sekalih")
a = 10
print(a)

print(time.time() - start_time, "Detik")
# Comment
# Jika ingin bisa compile Python Ke yang namanya Byte Code agar program
# dijalankan lebih cepat pakai ini :
# Source Code Byte Code -> Compiled -> Executable Terminal / Dijalankan
# Caranya tuliskan:
# python -m py_compile Main.py
# Kemudian jalankan:
# python __pycache__/Main.cpython-39.pyc
