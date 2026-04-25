def substr (string, start_index, end_index):
    #returns a substring that starts from the start_pos and goes upto end_pos , inclusive of end_pos 
    #substr(1, 2, 'apple') returns 'pp'
    #note : both are indexes and not positions. so to get first character, index => 0
    # throws exception when an index is out of range 

    if start_index < 0 : 
        raise IndexError ("Starting index should be a non negative value")
    if end_index >= len (string) :
        raise IndexError ("Ending index out of bound")
    else : 
        new_string = ''
        current_index = start_index
        while current_index <= end_index :
            new_string += string[current_index]
            current_index += 1
        return new_string


def test() : 
    string = 'Spongebob SquarePants'

    if substr(string, 2, 4 ) == 'ong' : 
        print("Success")
    else : print("Oops something went wrong")
    
if __name__ == "__main__" :
    test()


    
    
