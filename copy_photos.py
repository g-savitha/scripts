from shutil import copyfile
f = open("../../../textfiles/photos_to_copy_list.txt")

li = f.readlines()

new_li =[]
src = "/srcLoc"
dest = "/destLoc"
for i in li:
    new_li.append(i.strip()+".JPG")
for i in new_li:
    copyfile(src+i,dest+i)
    print("Copied: "+i)
f.close()   

