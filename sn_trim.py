


f = open("raw_sns.log")
key = "contacts_"
sns = []
count = 0
for line in f:
    line = line.strip()
    before_keyward, keyword, after_keyword = line.partition(key)
    
    if after_keyword:   
        if after_keyword not in sns:
            sns.append(after_keyword)
print len(sns)
with open("trim_sns.txt", "a") as myfile:
    for screen_name in sns:
        myfile.write("{}\n".format(screen_name))
print ("End of file")