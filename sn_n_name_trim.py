
def main():
    #reads file
    #make sure correct file name
    f = open("raw_sns_n_display.log")

    #screen name always has "contacts_" before it
    #sets key to use "contacts_"
    key_sn = "contacts_"

    #screen name and display lists
    sns = []
    display = []

    #loop to iterate through each line within the textfile
    #that was created by the javascript > save log
    for line in f:

        #clears line of "\n" so it will not be saved after parsing
        line = line.strip()

        #checks to make sure first 2 characters are "VM" on the line
        #all the screen names and display names are on lines that begin with "VM"
        if line[:2] == "VM":

            #splits up "VM" line if it finds the key_sn
            #if it finds key, splits line to before key_sn, key_sn itself and then after key_sn
            before_contact, contact, after_contact = line.partition(key_sn)
            
            #if after key_sn has value, then true
            if after_contact:   

                #checks if string already in screen name list
                #if screen name not in list, appends the screen name
                if after_contact not in sns:
                    sns.append(after_contact)

            #else statement for other "VM" lines that contain the display name
            else:

                #splits line by ":". we will want the string after the colon
                get_display = line.split(":")

                #trims down the string to remove first 2 character which are a number and whitespace
                #also trims down last 3 characters which is "AIM"
                #overwrites the variable
                get_display[1] = get_display[1][2:-3]

                #checks if string already in display name list
                #if display name not in list, appends the display name
                if get_display[1] not in display:
                    display.append(get_display[1])       

    #print number of screen names logged
    print len(sns)

    #writes to filename of "trim_sns_display.txt"
    with open("trim_sns_display.txt", "w") as myfile:

        #loops through the length of screen names
        #writes a new line each iteration that contain display name and screen name
        for i in range(len(sns)):
            myfile.write("{} : {}\n".format(display[i], sns[i]))

    #to indicate we completed the file
    print ("End of file")

main()