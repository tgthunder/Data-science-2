def searcher():
    import time 
    # some 4 seconds time consuming task
    book="This is a comic book of marvel cinematic universe"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Text is in the book")

        else:
            print("Text is is not in the book")

search=searcher()
print("search started")
next(search)
search.send("comic")
input("Press any key:")
search.send("comic book")
input("Press any key:")
search.send("as")
input("Press any key:")
search.send("fh")
input("Press any key:")
search.send("univesre")
