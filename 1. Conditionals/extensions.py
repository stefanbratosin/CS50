def main():
    # Take file type input from user and sanitize
    text = input("Enter file type: ").lower().strip()
    get_media_type(getFileExtension(text))

def getFileExtension(fileName: str):
    # List will always have 2 results are we are splitting only once from the right
    extension = fileName.rsplit(".", 1)[1]
    return extension

def get_media_type(extension: str):
    match extension:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()
