## 基于面向对象的设计思想开发
## 图书管理系统实现 增加 查询 修改 删除 集合框
class Book:
    ## 成员属性:[名称、id]
    def __init__(self,bookId,bookName):
        self.bookId = bookId
        self.bookName = bookName

    def toStr(self):
        print(self.bookId,self.bookName)

class Main:
    ## 定义图书的容器 存放多个图书
    books = []
    def addBook(self,bookId,bookName):
        # 1. 拿一本新书
        newBook = Book(bookId, bookName)

        # 2. 展示给用户看
        print("您要增加的书：")
        newBook.toStr()

        # 3. 放到书架上
        append = Main.books.append(newBook)
        print("✅ 添加成功！")
        print("==============")

    ## 查询所有图书信息
    def showBookAll(self):
        for index,book in enumerate(self.books):
            ## 展示每个图书信息
            print("ID:{book.bookId},书籍名称:{book.bookName}")

    ## 根据图书id查询图书信息
    def getByIdBook(self,bookId):
        for index,book in enumerate(self.books):
            if bookId == book.bookId:
                # print(f"bookId:{}")
                return True
            return False


main = Main()                                           # 1. 创建管理系统
main.addBook("001","Python入门到精通")  # 2. 添加一本书
main.showBookAll()                                      # 3. 显示所有图书

print("=================")
rt=print(main.getByIdBook("001"))
print(main.getByIdBook("002"))
if rt:
    print("图书存在")
else:
    print("图书不存在")
