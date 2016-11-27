output = raw_input("Please enter File Output Name: ")
print ""
input = raw_input("Please enter File Input Name: ")
output = output + ".txt"
write = open(output , 'w')
write.write('-------------------TELNET OUTPUT------------------------\n\n')
def check():
        datafile = file(input)
        found = False 
        for line in datafile:
            if '#' in line:
                print "Hit" + ": " "is in line : " + line
                write.write(line)
         
           



print check()
write.close()
