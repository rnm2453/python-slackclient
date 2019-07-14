def isincluded(input, regex):
    keywords = regex.split("#")
    for i in range(len(keywords)):
        if keywords[i] in needle:
            print(needle)

needle = "Hey there! how are you doing"

haystack = "Hello#Hi#Hodqy#i am#Hey"
isincluded(needle, haystack)

