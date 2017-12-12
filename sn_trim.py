
def main():
    #reads this file
    #make sure correct file name
    f = open("raw_sns.log")

    #screen name always has "contacts_" before it
    #sets key to use "contacts_"
    key = "contacts_"

    #screen name list
    sns = []

    #loop to iterate through each line within the textfile
    #that was created by the javascript > save log
    for line in f:

        #clears line of "\n" so it will not be saved after parsing
        line = line.strip()

        #if it finds key, splits line to before key, key itself and then after key
        before_keyward, keyword, after_keyword = line.partition(key)
        
        #if after key has value, then true
        if after_keyword:
            
            #checks if string already in screen name list
            #if screen name not in list, appends the screen name
            if after_keyword not in sns:
                sns.append(after_keyword)

    #print number of screen names logged
    print len(sns)

    #writes to filename of "trim_sns.txt"
    with open("trim_sns.txt", "w") as myfile:

        #iterates through screen name list
        #each iteration will use screen_name as variable
        #writes a new line each iteration that contain screen name
        for screen_name in sns:
            myfile.write("{}\n".format(screen_name))

    #to indicate we complete the file
    print ("End of file")

main()