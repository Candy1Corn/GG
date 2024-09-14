import json, time, os

預設每個人可以借幾天書 = 7      #暫時預設每個人可以藉七天書，也可以用input做出個性設定
沒找到 = 1
LibraryIndexJson = os.path.join(os.getcwd(), "LibraryIndex.json")

def 新書紀錄():     #以添加越女劍為例
    with open (LibraryIndexJson, "r", encoding="UTF-8") as JsonFile:
        FileData = json.load(JsonFile)
    newbookdata = {}
    newbookdata['name'] = input("請輸入新書的書名：")
    newbookdata['author'] = input("請輸入作者名：")
    newbookdata['ID'] = int(input("請輸入書本的ID或索引碼："))
    newbookdata['state'] = ["未借出", "無", 0, 0]
    FileData.append(newbookdata)
    with open (LibraryIndexJson, "w", encoding="UTF-8") as JsonFile:
        JsonFile = json.dump(FileData, JsonFile, ensure_ascii=False, indent = 5)
    print("登記成功！")

def 書籍丟失(沒找到):
    JsonFile = open(LibraryIndexJson, "r", encoding="UTF-8")
    a = json.load(JsonFile)

    丟失書籍 = input("請輸入丟失的書名：")

    for i in range(0, len(a)):
        try:
            x = list((a[i]).keys())[list((a[i]).values()).index(丟失書籍)]
            確認丟失書籍 = input(f"請確認丟失的書籍是否如下：\n書名：{a[i]["name"]}，作者：{a[i]["author"]}，書籍ID：{a[i]["ID"]}，借還狀態：{a[i]["state"][0]}，借閱人：{a[i]["state"][1]}　a.正確  b.重來：")
            書本ID = int(input("為避免同名書請確認書本ID："))
            if 確認丟失書籍 == "a" and a[i]["ID"] == 書本ID:
                del a[i]
                with open (LibraryIndexJson, "w", encoding="UTF-8") as JsonFile:
                    JsonFile = json.dump(a, JsonFile, ensure_ascii=False, indent = 5)
                print("成功註銷該書！")
                break
            else:
                print("已取消操作")
                break
        except ValueError:
                沒找到 += 1
                if 沒找到 == len(a)+1:
                    print("書籍已不存在，或檢查是不是打錯字了喔！")
                else:
                    continue

def 借書(沒找到):
    JsonFile = open(LibraryIndexJson, "r", encoding="UTF-8")
    a = json.load(JsonFile)

    所找書籍 = input("請問你想找甚麼書呢？")

    for i in range(0, len(a)):
        try:
            y = list((a[i]).values()).index(所找書籍)
            是否借書 = input(f"想要借這本書嗎？\n書名：{a[i]["name"]}，作者：{a[i]["author"]}，書籍ID：{a[i]["ID"]}，借還狀態：{a[i]["state"][0]}，借閱人：{a[i]["state"][1]}\n  a.是  b.否：")
            if 是否借書.lower() == "a":
                書本ID = int(input("為避免同名書請確認書本ID："))
                if a[i]["state"][0] == "未借出":
                    if a[i]["ID"] == 書本ID:
                        借書人名 = input("請輸入你的名字：")
                        a[i]["state"][0] = "已借出"
                        a[i]["state"][1] = 借書人名
                        借書時間 = str(time.localtime()[1])+"月"+str(time.localtime()[2])+"號"
                        預計還書時間 = str(time.localtime()[1])+"月"+str(time.localtime()[2]+7)+"號"
                        a[i]["state"][2] = 借書時間
                        a[i]["state"][3] = 預計還書時間
                        with open (LibraryIndexJson, "w", encoding="UTF-8") as JsonFile:
                            JsonFile = json.dump(a, JsonFile, ensure_ascii=False, indent = 5)
                        print("借書成功！")
                        break
                    else:
                        print(f"書名與ID不符合，再試一次吧！")
                        break
                else:
                    print(f"好書被搶先啦～{a[i]["state"][3]}再來吧！")
                    break
            else:
                print("好書不可錯過，歡迎下次來借這本書喔！")
                break
        except ValueError:
                沒找到 += 1
                if 沒找到 == len(a)+1:
                    print("請檢查是不是打錯字了喔！")
                else:
                    continue

def 還書(沒找到):
    JsonFile = open(LibraryIndexJson, "r", encoding="UTF-8")
    a = json.load(JsonFile)

    所還書籍 = input("請輸入歸還的書名：")

    for i in range(0, len(a)):
        try:
            z = list((a[i]).keys())[list((a[i]).values()).index(所還書籍)+2]
            是否還書 = input(f"確定歸還以下書籍：\n書名：{a[i]["name"]}，作者：{a[i]["author"]}，書籍ID：{a[i]["ID"]}，借還狀態：{a[i]["state"][0]}，借閱人：{a[i]["state"][1]}\n  a.是  b.否：")
            書本ID = int(input("為避免同名書請確認書本ID："))
            if 是否還書.lower() == "a":
                if a[i]["state"][0] == "已借出" and a[i]["ID"] == 書本ID:
                    a[i]["state"][0] = "未借出"
                    a[i]["state"][1] = "無"
                    a[i]["state"][2] = 0
                    a[i]["state"][3] = 0
                    print("還書中......")
                    with open (LibraryIndexJson, "w", encoding="UTF-8") as JsonFile:
                        JsonFile = json.dump(a, JsonFile, ensure_ascii=False, indent = 5)
                    print("還書成功！")
                    break
                else:
                    print("該書已經歸還，如有疑問請找圖書管理員")
                break
            else:
                print("要記得在借書七天內歸還書籍喔！")
                break
        except ValueError:
                沒找到 += 1
                if 沒找到 == len(a)+1:
                    print("請檢查是不是打錯字了喔！")
                else:
                    continue

def main():
    執行 = input("需要做甚麼呢？  a.新書紀錄  b.借書  c.還書  d.書籍遺失登記  :  ")
    if 執行.lower() == "a":
        新書紀錄()
    elif 執行.lower() == "b":
        借書(沒找到)
    elif 執行.lower() == "c":
        還書(沒找到)
    elif 執行.lower() == "d":
        書籍丟失(沒找到)
    else:
        print("似乎輸入錯了，再來一次吧！")


main()

"""
製作時我想到應該還有借還書的日期(不用精確到時間)，雖然因為時間比較短，不是很完善，但還是寫進程式，表達一下想法

各種內心獨白
    以前自學python 學得毫無章法，還沒練習過如何處裡json 檔，要不要練習一下呢？可是花時間去研究這個的話會沒時間學go 怎麼辦……
    不然我先用python 寫完再讓AI 幫我翻譯成go 好了
    還有好多邊界條件沒排掉
    不行了不能再改下去了，再改下去會沒時間睡覺，晚睡就會晚起，晚起9/15就會很晚才去辦台灣人居住證，就會沒時間學go了！！
    AI 翻譯成go 之後有錯誤訊息QAQ
    我筆電(筆記本)目前只能打繁體字，人家真的看得懂嗎？
    我第一次只用不到24小時就寫出這麼多程式(相信我，我寫python 的時候沒有用AI)
"""