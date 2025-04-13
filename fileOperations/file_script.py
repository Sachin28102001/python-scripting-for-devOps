#Python script to read & write in a particular folder.

def update_server(file_path, key, value):
    #first read operation of the file.
    with open(file_path , 'r') as file:
        #variable line will store each lines of the file
        lines = file.readlines()
        
    #second write operation of the file.
    with open(file_path , 'w') as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            
            else:
                file.write(line)
                
update_server("server.config" , "MAX_CONNECTIONS" , "8000")
                