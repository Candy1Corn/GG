
name = input("請輸入網址：")    #www.nowcoder.com, https://www.nowcoder.com , ac.nowcoder.com

if "https://" in name:
    f1 = name.split("//")[1]
    f2 = f1.split(".")[0]
    if f2 == "www":
        print("NewCoder!")
    elif f2 == "ac":
        print("Ac!")
    else:
        print("Nothing")
else:
    f3 = name.split(".")[0]
    if f3 == "www":
        print("NewCoder!")
    elif f3 == "ac":
        print("Ac!")
    else:
        print("Nothing")
"""
a = {"P":["python", "php"],"l":["lua", "linux"]}
print(a["P"][1])
"""