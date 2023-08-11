p = int(input("Enter the value of p for encryption\n"))
out_file = open("out.txt", "w")
with open("in.txt") as in_file:
    for line in in_file:
        for i in line:
            if i.isalpha() and i.isupper():
                if 65 <= ord(i) <= 90:
                    q = ord(i) + p
                    if q > 90:
                        q -= 26
                    out_file.write(chr(q))
                else:
                    out_file.write(i)
            else:
                out_file.write(i)
out_file.close()
print("out.txt has been created successfully.")
