def storageConverter(number):
    byte = 8
    kilobyte = 1024 #bytes
    megabyte = 1024 #kilobyte
    gygabyte = 1024 #megabytes
    telabyte = 1024 #gygabytes
    hexabyte = 1023 #telabytes
    zetabyte = 1024 #hexabytes
    return zetabyte * number,hexabyte * number,telabyte * number ,gygabyte * number ,megabyte * number ,kilobyte*number ,byte * number


number = int(input())

print(storageConverter(number))