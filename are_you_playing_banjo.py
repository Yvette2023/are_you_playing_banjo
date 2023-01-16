def are_you_playing_banjo(name):
    if name[0]=="R" or name[0]=="r":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"

    if name[0]=="Y" or name[0]=="s":
        return name + " plays guitar" 
    else:
        return name + " does not play guitar"
    
print(are_you_playing_banjo("pop"))

print(are_you_playing_banjo("pop"))