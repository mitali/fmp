'''
Created on Jun 9, 2015

@author: Mitali
'''

# TODO: Make this work.

# takes txt file with shot number & seconds, parses it, saves it into 3d array
# and calculates length of each shot, saving that in separate array

def save_shot_details(video):
    
    my_dir = '/Users/Mitali/Desktop/IndividualProject/fmp/FilmAudioProgram/video/videos/'+video
    shots_file = my_dir + '/shots/shots_file.txt'
    my_file = open(shots_file, 'r')
    
    big_array=[]
    new_array=[]

    for line in my_file:
        
        line_array = line.split(' ')
        line_array[1]=line_array[1].replace('\n', '')
        
        big_array.append(line_array)
        
        for i in range(0, len(big_array)):
            
            # check the mod so can skip every alternate row
            if i%2==0 and i+1<=len(big_array):# and big_array[i][0]==big_array[i+1][0]:
                
                shot_len=big_array[i+1][1]-big_array[i][1]
                
                temp_array=[]
                temp_array.append(shot_len)
                temp_array.append(big_array[i][1])
                
                new_array.append(temp_array)
        
        #print "Old array length: " + str(len(big_array))
        #print "New array length: " + str(len(new_array))
        
        #print new_array
    
    return

save_shot_details('shh')
