from socket import *
def Socketing(URL):
    contentType = ""    # define an empty var
    extension = URL.split(".")  # Splitting the URl to take the extension
    if(len(extension) > 1): # Here we check the extension to determine the content type
        if(extension[1] == "png"):
            contentType = "image/png"
        elif (extension[1] == "jpg"):
            contentType = "image/jpg"
        elif (extension[1] == "css"):
            contentType = "text/css"
        else:
            contentType = "text/html"
    else:
        contentType = "text/html"
    # Routing according to the user input at the suburl
    if(URL == "" or URL == "en" or URL == "index.html"):
        URL = "main_en.html"
    elif(URL == "ar"):
        URL = "main_ar.html"

    return [contentType, URL.strip()]

def main():
    serverPort = 6060    # port number
    ser = socket(AF_INET, SOCK_STREAM)
    ser.bind(('', serverPort))  # here getting the socket
    ser.listen(1)   # the server is listening
    print('The server is listening ...')
    while True:
        Socketconn, client_address = ser.accept()
        senc = Socketconn.recv(1024).decode()
        token = senc.split("/")
        print(token[1]+">>>>>>>>>>>>>>>>")
        if len(token)>=2:
            URL = token[1].split(" ")   #here to get the pure URl(no sapces in it)
        contentType, fileName = Socketing(URL[0])
        print(senc)
        print("*******************************************************")
        # client_address[0] this means to store client IP in ip var
        ip = client_address[0] # ip of the client
        port = client_address[1] # port of the client
        try:
                    if (fileName=="so"):
                        Socketconn.send(bytes("HTTP/1.1 307 Temporary Redirect \r\n", "UTF-8"))
                        Socketconn.send(bytes("location: https://stackoverflow.com \r\n", "UTF-8"))
                        Socketconn.send(bytes("\r\n", "UTF-8"))
                        Socketconn.close()
                    elif (fileName=="itc"):
                        Socketconn.send(bytes("HTTP/1.1 307 Temporary Redirect \r\n", "UTF-8"))
                        Socketconn.send(bytes("location: https://itc.birzeit.edu/ \r\n", "UTF-8"))
                        Socketconn.send(bytes("\r\n", "UTF-8"))
                        Socketconn.close()
                    else:
                        with open(fileName, "rb") as f:
                            fileContent = f.read()
                        Socketconn.send(bytes("HTTP/1.1 200 OK\r\n", "UTF-8"))
                        Socketconn.send(bytes("Content-Type:" + contentType + "\r\n", "UTF-8"))
                        Socketconn.send(b"\r\n")
                        Socketconn.send(fileContent)
                        Socketconn.close()
        except IOError:
             # There is an html code in case there is an error in the request so this will appear to the user 404 not found page
                fileContent = '<!DOCTYPE html><html><head><title>Error 404</title> </head><body><h1 style="color:red;">The file is not found</h1><p id=par>Basil Hijaz 1200503 &emsp;<br>Mohammad AbuSaleh 1203331 &emsp;<br>Bahaa Salah 1181234  <style >p#par{font-weight: bold;}</style></p>   <p>The IP is &#8594 ' + str(ip)+'</p> <p>The Port number is &#8594 '+str(port)+'</p></body></html>'
                Socketconn.send(bytes("HTTP/1.1 404 Not Found \r\n", "UTF-8"))
                Socketconn.send(bytes("Content-Type: text/html\r\n", "UTF-8"))
                Socketconn.send(bytes("\r\n", "UTF-8"))
                Socketconn.send(bytes(fileContent, "UTF-8"))
                Socketconn.close()

main()