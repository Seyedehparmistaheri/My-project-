f = input("esm file ra type konid:")
m = f.lower().strip()



if m.endswith("jpg") or m.endswith("jpeg"):
    print("image/jpeg")
elif m.endswith("gif"):
    print("image/gif")
elif m.endswith("png"):
    print("image/png")
elif m.endswith("txt"):
    print("text/plain")
elif m.endswith("pdf"):
    print("application/pdf")
elif m.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")
