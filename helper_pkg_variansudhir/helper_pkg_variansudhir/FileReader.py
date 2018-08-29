def ReadAllText(file_name):
    file_content=""
    with open(file_name, "r+") as original_file:           
            file_content=original_file.read()    
    return str(file_content)
