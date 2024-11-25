# # def funargs(*args):
# #     print(type(args))
# #     for i in args:
# #         print(i)

# # har=["Harry","Garry","Larry","Heena","Sudarshan"]
# # funargs(*har)

# # def funargs(normal,*args):
# #     print(normal)
# #     for i in args:
# #         print(i)

# # har=["Harry","Garry","Larry","Heena","Sudarshan"]
# # normal="This is a normal argument"
# # funargs(normal,*har)


# def funargs(normal,*args,**kwargs):
#     print(normal)
#     for i in args:
#         print(i)
#     for key,value in kwargs.items():
#         print(f"{key} is a {value}")

# har=["Harry","Garry","Larry","Heena","Ramesh"]
# normal="This is a normal argument"
# kw={"Sudarshan":"owner","Sourabh":"CEO","Tanish":"Manager"}

# funargs(normal,*har,**kw)


def funargs(*args):
    for items in args:
        print(items)


har=["Harry","Garry","Larry","Sofia"]
funargs(*har)