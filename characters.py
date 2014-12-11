from decimal import Decimal


def pipe_length():
    fname = raw_input("Enter the Text File Name:")
    fhand = open(fname)
    fdata = fhand.read() 
    repeat_char = {'ch_a':0,'ch_b':0,'ch_c':0,'ch_d':0,'ch_e':0,'ch_f':0,'ch_g':0,'ch_h':0,'ch_i':0,'ch_j':0,'ch_k':0,'ch_l':0,'ch_m':0,'ch_n':0,'ch_o':0,'ch_p':0,'ch_q':0,'ch_r':0,'ch_s':0,'ch_t':0,'ch_u':0,'ch_v':0,'ch_w':0,'ch_x':0,'ch_y':0,'ch_z':0,'ch_A':0,'ch_B':0,'ch_C':0,'ch_D':0,'ch_E':0,'ch_F':0,'ch_G':0,'ch_H':0,'ch_I':0,'ch_J':0,'ch_K':0,'ch_L':0,'ch_M':0,'ch_N':0,'ch_O':0,'ch_P':0,'ch_Q':0,'ch_R':0,'ch_S':0,'ch_T':0,'ch_U':0,'ch_V':0,'ch_W':0,'ch_X':0,'ch_Y':0,'ch_Z':0}
    code_char = {'ch_a':0,'ch_b':0,'ch_c':0,'ch_d':0,'ch_e':0,'ch_f':0,'ch_g':0,'ch_h':0,'ch_i':0,'ch_j':0,'ch_k':0,'ch_l':0,'ch_m':0,'ch_n':0,'ch_o':0,'ch_p':0,'ch_q':0,'ch_r':0,'ch_s':0,'ch_t':0,'ch_u':0,'ch_v':0,'ch_w':0,'ch_x':0,'ch_y':0,'ch_z':0,'ch_A':0,'ch_B':0,'ch_C':0,'ch_D':0,'ch_E':0,'ch_F':0,'ch_G':0,'ch_H':0,'ch_I':0,'ch_J':0,'ch_K':0,'ch_L':0,'ch_M':0,'ch_N':0,'ch_O':0,'ch_P':0,'ch_Q':0,'ch_R':0,'ch_S':0,'ch_T':0,'ch_U':0,'ch_V':0,'ch_W':0,'ch_X':0,'ch_Y':0,'ch_Z':0}
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    compressed_data = " "
#    ch_a=0; ch_b=0; ch_c=0; ch_d=0; ch_e=0; ch_f=0; ch_g=0; ch_h=0; ch_i=0; ch_j=0; ch_k=0; ch_l=0; ch_m=0; ch_n=0; ch_o=0; ch_p=0; ch_q=0; ch_r=0; ch_s=0; ch_t=0; ch_u=0; ch_v=0; ch_w=0; ch_x=0; ch_y=0; ch_z=0;
    ch =0
    while ch < len(fdata):
        if fdata[ch]==alphabet[0]:
            repeat_char['ch_a'] += 1
             
        elif fdata[ch]==alphabet[1]:
            repeat_char['ch_b'] += 1
             
        elif fdata[ch]==alphabet[2]:
            repeat_char['ch_c'] += 1
             
        elif fdata[ch]==alphabet[3]:
            repeat_char['ch_d'] += 1
             
        elif fdata[ch]==alphabet[4]:
            repeat_char['ch_e'] += 1
             
        elif fdata[ch]==alphabet[5]:
            repeat_char['ch_f'] += 1
             
        elif fdata[ch]==alphabet[6]:
            repeat_char['ch_g'] += 1
                   
        elif fdata[ch]==alphabet[7]:
            repeat_char['ch_h'] += 1
             
        elif fdata[ch]==alphabet[8]:
            repeat_char['ch_i'] += 1
             
        elif fdata[ch]==alphabet[9]:
            repeat_char['ch_j'] += 1
             
        elif fdata[ch]==alphabet[10]:
            repeat_char['ch_k'] += 1
             
        elif fdata[ch]==alphabet[11]:
            repeat_char['ch_l'] += 1
             
        elif fdata[ch]==alphabet[12]:
            repeat_char['ch_m'] += 1
                           
        elif fdata[ch]==alphabet[13]:
            repeat_char['ch_n'] += 1
             
        elif fdata[ch]==alphabet[14]:
            repeat_char['ch_o'] += 1
             
        elif fdata[ch]==alphabet[15]:
            repeat_char['ch_p'] += 1
             
        elif fdata[ch]==alphabet[16]:
            repeat_char['ch_q'] += 1
             
        elif fdata[ch]==alphabet[17]:
            repeat_char['ch_r'] += 1
             
        elif fdata[ch]==alphabet[18]:
            repeat_char['ch_s'] += 1
              
        elif fdata[ch]==alphabet[19]:
            repeat_char['ch_t'] += 1
             
        elif fdata[ch]==alphabet[20]:
            repeat_char['ch_u'] += 1
             
        elif fdata[ch]==alphabet[21]:
            repeat_char['ch_v'] += 1
             
        elif fdata[ch]==alphabet[22]:
            repeat_char['ch_w'] += 1
             
        elif fdata[ch]==alphabet[23]:
            repeat_char['ch_x'] += 1
             
        elif fdata[ch]==alphabet[24]:
            repeat_char['ch_y'] += 1
               
        elif fdata[ch]==alphabet[25]:
            repeat_char['ch_z'] += 1
              
        elif fdata[ch]==alphabet[26]:
            repeat_char['ch_A'] += 1
             
        elif fdata[ch]==alphabet[27]:
            repeat_char['ch_B'] += 1
             
        elif fdata[ch]==alphabet[28]:
            repeat_char['ch_C'] += 1
             
        elif fdata[ch]==alphabet[29]:
            repeat_char['ch_D'] += 1
             
        elif fdata[ch]==alphabet[30]:
            repeat_char['ch_E'] += 1
             
        elif fdata[ch]==alphabet[31]:
            repeat_char['ch_F'] += 1
             
        elif fdata[ch]==alphabet[32]:
            repeat_char['ch_G'] += 1
                   
        elif fdata[ch]==alphabet[33]:
            repeat_char['ch_H'] += 1
             
        elif fdata[ch]==alphabet[34]:
            repeat_char['ch_I'] += 1
             
        elif fdata[ch]==alphabet[35]:
            repeat_char['ch_J'] += 1
             
        elif fdata[ch]==alphabet[36]:
            repeat_char['ch_K'] += 1
             
        elif fdata[ch]==alphabet[37]:
            repeat_char['ch_L'] += 1
             
        elif fdata[ch]==alphabet[38]:
            repeat_char['ch_M'] += 1
                           
        elif fdata[ch]==alphabet[39]:
            repeat_char['ch_N'] += 1
             
        elif fdata[ch]==alphabet[40]:
            repeat_char['ch_O'] += 1
             
        elif fdata[ch]==alphabet[41]:
            repeat_char['ch_P'] += 1
             
        elif fdata[ch]==alphabet[42]:
            repeat_char['ch_Q'] += 1
             
        elif fdata[ch]==alphabet[43]:
            repeat_char['ch_R'] += 1
             
        elif fdata[ch]==alphabet[44]:
            repeat_char['ch_S'] += 1
              
        elif fdata[ch]==alphabet[45]:
            repeat_char['ch_T'] += 1
             
        elif fdata[ch]==alphabet[46]:
            repeat_char['ch_U'] += 1
             
        elif fdata[ch]==alphabet[47]:
            repeat_char['ch_V'] += 1
             
        elif fdata[ch]==alphabet[48]:
            repeat_char['ch_W'] += 1
             
        elif fdata[ch]==alphabet[49]:
            repeat_char['ch_X'] += 1
             
        elif fdata[ch]==alphabet[50]:
            repeat_char['ch_Y'] += 1
               
        elif fdata[ch]==alphabet[51]:
            repeat_char['ch_Z'] += 1
        ch +=1 
       
#    for key, value in sorted(repeat_char.iteritems(), key=lambda (k,v): (v,k)):
#        print "%s: %s" % (key, value)
    
################################################################################
################################################################################

    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1'
#    print code_char
    del repeat_char[max_value]
   
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '10'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '11'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '000'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '001'
#    print code_char
    del repeat_char[max_value]            
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '010'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '011'
#    print code_char
    del repeat_char[max_value]
   
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '100'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '101'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '110'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '111'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0000'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0001'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0010'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0011'
#    print code_char
    del repeat_char[max_value]
   
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0100'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0101'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0110'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '0111'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1000'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1001'
#    print code_char
    del repeat_char[max_value]        
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1010'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1011'
#    print code_char 
    del repeat_char[max_value]          #end of lower case letters
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1100'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1101'
#    print code_char
    del repeat_char[max_value]
   
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1110'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '1111'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00000'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00001'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00010'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00011'
#    print code_char
    del repeat_char[max_value]            
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00100'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00101'
#    print code_char
    del repeat_char[max_value]
   
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00110'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '00111'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01000'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01001'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01010'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01011'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01100'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01101'
#    print code_char
    del repeat_char[max_value]
   
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01110'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '01111'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '10000'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '10001'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '10010'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '10011'
#    print code_char
    del repeat_char[max_value]        
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '10100'
#    print code_char
    del repeat_char[max_value]
    
    max_value =  max(repeat_char, key=repeat_char.get)
#    print max_value
    code_char[max_value] = '10101'
    print code_char
    del repeat_char[max_value]     
    
###########################################################################
########################################################################### 
    
    ch = 0
    while ch < len(fdata):
        if fdata[ch]==alphabet[0]:
            compressed_data += code_char['ch_a']    
            
        elif fdata[ch]==alphabet[1]:
            compressed_data += code_char['ch_b']
             
        elif fdata[ch]==alphabet[2]:
            compressed_data += code_char['ch_c']
             
        elif fdata[ch]==alphabet[3]:
            compressed_data += code_char['ch_d']
             
        elif fdata[ch]==alphabet[4]:
            compressed_data += code_char['ch_e']
             
        elif fdata[ch]==alphabet[5]:
            compressed_data += code_char['ch_f']
             
        elif fdata[ch]==alphabet[6]:
            compressed_data += code_char['ch_g']
                   
        elif fdata[ch]==alphabet[7]:
            compressed_data += code_char['ch_h']
             
        elif fdata[ch]==alphabet[8]:
            compressed_data += code_char['ch_i']
             
        elif fdata[ch]==alphabet[9]:
            compressed_data += code_char['ch_j']
             
        elif fdata[ch]==alphabet[10]:
            compressed_data += code_char['ch_k']
             
        elif fdata[ch]==alphabet[11]:
            compressed_data += code_char['ch_l']
             
        elif fdata[ch]==alphabet[12]:
            compressed_data += code_char['ch_m']
                           
        elif fdata[ch]==alphabet[13]:
            compressed_data += code_char['ch_n']
             
        elif fdata[ch]==alphabet[14]:
            compressed_data += code_char['ch_o']
             
        elif fdata[ch]==alphabet[15]:
            compressed_data += code_char['ch_p']
             
        elif fdata[ch]==alphabet[16]:
            compressed_data += code_char['ch_q']
             
        elif fdata[ch]==alphabet[17]:
            compressed_data += code_char['ch_r']
             
        elif fdata[ch]==alphabet[18]:
            compressed_data += code_char['ch_s']
              
        elif fdata[ch]==alphabet[19]:
            compressed_data += code_char['ch_t']
             
        elif fdata[ch]==alphabet[20]:
            compressed_data += code_char['ch_u']
             
        elif fdata[ch]==alphabet[21]:
            compressed_data += code_char['ch_v']
             
        elif fdata[ch]==alphabet[22]:
            compressed_data += code_char['ch_w']
             
        elif fdata[ch]==alphabet[23]:
            compressed_data += code_char['ch_x']
             
        elif fdata[ch]==alphabet[24]:
            compressed_data += code_char['ch_y']
               
        elif fdata[ch]==alphabet[25]:
            compressed_data += code_char['ch_z']
            
        elif fdata[ch]==alphabet[26]:
            compressed_data += code_char['ch_A']    
            
        elif fdata[ch]==alphabet[27]:
            compressed_data += code_char['ch_B']
             
        elif fdata[ch]==alphabet[28]:
            compressed_data += code_char['ch_C']
             
        elif fdata[ch]==alphabet[29]:
            compressed_data += code_char['ch_D']
             
        elif fdata[ch]==alphabet[30]:
            compressed_data += code_char['ch_E']
             
        elif fdata[ch]==alphabet[31]:
            compressed_data += code_char['ch_F']
             
        elif fdata[ch]==alphabet[32]:
            compressed_data += code_char['ch_G']
                   
        elif fdata[ch]==alphabet[33]:
            compressed_data += code_char['ch_H']
             
        elif fdata[ch]==alphabet[34]:
            compressed_data += code_char['ch_I']
             
        elif fdata[ch]==alphabet[35]:
            compressed_data += code_char['ch_J']
             
        elif fdata[ch]==alphabet[36]:
            compressed_data += code_char['ch_K']
             
        elif fdata[ch]==alphabet[37]:
            compressed_data += code_char['ch_L']
             
        elif fdata[ch]==alphabet[38]:
            compressed_data += code_char['ch_M']
                           
        elif fdata[ch]==alphabet[39]:
            compressed_data += code_char['ch_N']
             
        elif fdata[ch]==alphabet[40]:
            compressed_data += code_char['ch_O']
             
        elif fdata[ch]==alphabet[41]:
            compressed_data += code_char['ch_P']
             
        elif fdata[ch]==alphabet[42]:
            compressed_data += code_char['ch_Q']
             
        elif fdata[ch]==alphabet[43]:
            compressed_data += code_char['ch_R']
             
        elif fdata[ch]==alphabet[44]:
            compressed_data += code_char['ch_S']
              
        elif fdata[ch]==alphabet[45]:
            compressed_data += code_char['ch_T']
             
        elif fdata[ch]==alphabet[46]:
            compressed_data += code_char['ch_U']
             
        elif fdata[ch]==alphabet[47]:
            compressed_data += code_char['ch_V']
             
        elif fdata[ch]==alphabet[48]:
            compressed_data += code_char['ch_W']
             
        elif fdata[ch]==alphabet[49]:
            compressed_data += code_char['ch_X']
             
        elif fdata[ch]==alphabet[50]:
            compressed_data += code_char['ch_Y']
               
        elif fdata[ch]==alphabet[51]:
            compressed_data += code_char['ch_Z']
              
        ch +=1   
        
    file_size = len(fdata)*8    
    print "uncompressed file: ",file_size
    print "compressed data: ",len(compressed_data)
    compression_ratio = Decimal(file_size)/Decimal(len(compressed_data))
    ans = (1- 1/Decimal(compression_ratio))*100
    print "Compression ratio: ",compression_ratio
    print "Compression ratio in %: ", ans
 
########################################################################
########################################################################    