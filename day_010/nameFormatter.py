def format_name(name, surename):
    firstName = name.lower()
    sureName = surename.lower()
    firstName = firstName[0].upper()+firstName[1:]
    sureName = sureName[0].upper()+sureName[1:]
    return f"{firstName} {sureName}"

print(format_name("guillermo", "escutia"))