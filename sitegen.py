import os,glob

directory=input("what folder are the files in? \n")
htmls = glob.glob(directory+"/*.html")
#print(htmls)
with open("index.html","w") as file:
    file.write("<!DOCTYPE html>\n")
    for i in range(len(htmls)):
        newline='\t<input type="button" value="'+htmls[i].removeprefix(str(directory+"\\")).removesuffix(".html")+'" onclick="location.href='+"'"+ str(directory)+ "\\\\"+htmls[i].removeprefix(str(directory+"\\"))+"'"+'"/>\n'
        try:
            file.write(newline)
        except UnicodeEncodeError:
            print("illegal character or something idk")
        file.write("\t<br>\n")
