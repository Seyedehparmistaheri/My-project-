def main():
    #gereftan voroodi az karbar
    matn = input('matn ra vared konid:')
    convert(matn)



#tabdil imoji be sticker
def convert(i):
    i = i.replace(":)", "🙂")
    i = i.replace(":(", "🙁")
    print(i)

main()
