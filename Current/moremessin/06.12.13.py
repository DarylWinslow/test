
# Function to creata a training file (allow user to choose percentage)
def training_file():
    
    count = 0
    i = 0    
    percent = 0 
    
    # open files
    f = open('myfile.txt','r')  #sampledata.txt
    fw = open('training_file.txt','w')

    while (percent == 0):
        try:
            percent = int (input("\n\nEnter in the percent of the file you want for training"
                            "\nShould be above 50%\n: "))        

        #Invalid input check    
        except ValueError:
            print ("\nPlease Enter a number. Try Again\n\n")
            
    # Line counter          
    for line in f:
        count = count + 1
                 
    # Dividing file into user's % choice for training file
    count = int(count) / 100 * int(percent)

    f.seek(0, 0)
    
    # Write training file
    for line in f:
        i = i + 1 
        fw.write(line)
        
        if i > count: #break when specified line is reached
            break

    f.close()
        
# End Of Training Function ##########



#Find Average function
def find_average(num_people, total):
    avg=total/num_people
    return int(avg)


########dictionary of non-numerical values function#######

def data(f):
    
    #Database / dictionarys
    workclass = {}
    education = {}
    marital_status = {}
    occupation = {}
    relationship = {}
    race = {}
    sex = {}

    # Temp string to hold line
    temp_line = ''

    # reset file
    f.seek(0,0)

    for line in f:

            # Split line up to be able to read each individual word
            temp_line = line.split(', ')

            # Add data to dictionarys
            try:
                
                if temp_line[1] in workclass:
                    workclass[temp_line[1]] += 1
                else:
                    workclass[temp_line[1]] = 1

                if temp_line[3] in education:
                    education[temp_line[3]] += 1
                else:
                    education[temp_line[3]] = 1

                if temp_line[5] in marital_status:
                    marital_status[temp_line[5]] += 1
                else:
                    marital_status[temp_line[5]] = 1

                if temp_line[6] in occupation:
                    occupation[temp_line[6]] += 1
                else:
                    occupation[temp_line[6]] = 1

                if temp_line[7] in relationship:
                    relationship[temp_line[7]] += 1
                else:
                    relationship[temp_line[7]] = 1

                if temp_line[8] in race:
                    race[temp_line[8]] += 1
                else:
                    race[temp_line[8]] = 1

                if temp_line[9] in sex:
                    sex[temp_line[9]] +=1
                else:
                    sex[temp_line[9]] = 1

            except IndexError:
                break
            
    #Dictionary to return
    data = {'workclass':workclass,'education':education, 'marital_status':marital_status,
            'occupation':occupation, 'relationship':relationship, 'race':race, 'sex':sex, }

        
    #print("\n----------Debug Test---------------")
    #print(workclass.values())
    #print(workclass,'\n')
    #print(education,'\n')
    #print(marital_status,'\n')
    #print(occupation,'\n')
    #print(relationship,'\n')
    #print(race,'\n')
    #print(sex,'\n')
    #print(hours_per_week,'\n')
    #GET RID OF COMMENTS TO TEST DEBUG

    return data

#######   end dictionary function  ########
###########################################




###############################################

#########***MAIN***############################

###############################################

#Call training file
training_file()

#open database
fh=open("training_file.txt", 'r')

#Create higher/lower databases for numerical values
highfile=open("highfile.txt", 'w+')
lowfile=open("lowfile.txt", 'w+')


total_pop=0

lines=fh.readlines()

for line in lines:
    total_pop+=1

greater_total_age = 0
lesser_total_age = 0

greater_pop = 0
lesser_pop = 0

greater_edu_num = 0
lesser_edu_num = 0

greater_cap_gain = 0
lesser_cap_gain = 0

greater_cap_loss = 0
lesser_cap_loss = 0

greater_hpw = 0
lesser_hpw = 0

for line in lines:
    if '>50K' in line:
        temp_line = line
        temp_line= temp_line.split(',')
        highfile.write(line)
        greater_pop+=1
        greater_total_age = greater_total_age + int(temp_line[0])
        greater_edu_num = greater_edu_num + int(temp_line[4])
        greater_cap_gain = greater_cap_gain + int(temp_line[10])
        greater_cap_loss = greater_cap_loss + int(temp_line[11])
        greater_hpw = greater_hpw + int(temp_line[12])

for line in lines:
    if '<=50K' in line:
        temp_line = line
        temp_line= temp_line.split(',')
        lowfile.write(line)
        lesser_pop+=1
        lesser_total_age = lesser_total_age + int(temp_line[0])
        lesser_edu_num = lesser_edu_num + int(temp_line[4])
        lesser_cap_gain = lesser_cap_gain + int(temp_line[10])
        lesser_cap_loss = lesser_cap_loss + int(temp_line[11])
        lesser_hpw = lesser_hpw + int(temp_line[12])


#numerical midpoint values
mid_age = (find_average(greater_pop, greater_total_age)+find_average(lesser_pop, lesser_total_age))/2
mid_edu_num = (find_average(greater_pop, greater_edu_num)+find_average(lesser_pop, lesser_edu_num))/2
mid_cap_gain = (find_average(greater_pop, greater_cap_gain)+find_average(lesser_pop, lesser_cap_gain))/2
mid_cap_loss = (find_average(greater_pop, greater_cap_loss)+find_average(lesser_pop, lesser_cap_loss))/2
mid_hpw = (find_average(greater_pop, greater_hpw)+find_average(lesser_pop, lesser_hpw))/2

#print("Age midpoint is ", mid_age)
#print("Edu number midpoint is", mid_edu_num)
#print("Cap gain mid is", mid_cap_gain)
#print("Cap loss mid is", mid_cap_loss)
#print("Hours/week mid is", mid_hpw)


        
#Test numerical values 
"""print("Total number of people is", total_pop)

print("\nTotal number of people earning over 50K is",greater_pop)
print("Total number of people earning under 50K is",lesser_pop)

print("\nAverage age of person earning over 50K is", find_average(greater_pop, greater_total_age))
print("Average age of person earning under 50K is", find_average(lesser_pop, lesser_total_age))

print("\nAverage Education Number of the wealthy is", find_average(greater_pop, greater_edu_num))
print("Average Education Number of the poor is", find_average(lesser_pop, lesser_edu_num))

print("\nAverage Cap-Gain of the wealthy is", find_average(greater_pop, greater_cap_gain))
print("Average Cap-Gain of the poor is", find_average(lesser_pop, lesser_cap_gain))

print("\nAverage Cap-Loss of the wealthy is", find_average(greater_pop, greater_cap_loss))
print("Average Cap-Loss of the poor is", find_average(lesser_pop, lesser_cap_loss))

print("\nAverage hours/week of the wealthy is", find_average(greater_pop, greater_hpw))
print("Average hours/week of the poor is", find_average(lesser_pop, lesser_hpw)) """



#Create high/low dictionaries for non-numerical values
high_dictionary=data(highfile) #call dictionary function
low_dictionary=data(lowfile)

#Dictionary of dictionaries testing#
"""print("")
print (high_dictionary['workclass'])
print("")
print (low_dictionary['workclass'])
print("")
print(high_dictionary['workclass']['Private'])

print("\nNumber of entries in high workclass dictionary is", len(high_dictionary['workclass'])) """


#go through dictionaries to find and compare values
#add keys with more high/lows to high/low list
high_list=[]
low_list=[]

for key in high_dictionary:
    temp=key

    try:

        if temp in low_dictionary:
            for key in high_dictionary[temp]:
                temp_new=key

                #assign key to list depending on propertional value
                if (high_dictionary[temp][temp_new])/(greater_pop)*(100) >= (low_dictionary[temp][temp_new])/(lesser_pop)*(100): 
                    #print(temp_new, "is rich")
                    high_list.append(temp_new)

                if (high_dictionary[temp][temp_new])/(greater_pop)*(100) < (low_dictionary[temp][temp_new])/(lesser_pop)*(100):
                    #print(temp_new, "is poor")
                    low_list.append(temp_new)

    except KeyError:
        break


        
    




########## CLASSIFIER ###########
    
f = open('myfile.txt','r')

f.seek(0, 0)
#lines_new=f.readlines()

rich=0
poor=0


for line in f:
    temp_line_new = line.split(', ')
    #temp_line_new = line.strip()
    score=0


    try:
        #numerical score assignment 
        if mid_age <= float(temp_line_new[0]):
            #print("HELLO")
            score+=1
        else:
            score-=1

        if mid_edu_num <= float(temp_line_new[4]):
            score+=1
        else:
            score-=1

        if mid_cap_gain <= float(temp_line_new[10]):
            score+=1
        else:
            score-=1

        if mid_cap_loss <= float(temp_line_new[11]):
            score+=1
        else:
            score-=1

        if mid_hpw <= float(temp_line_new[12]):
            score+=1
        else:
            score-=1

        #non numerical score assignment
        i=0
        while i<len(temp_line):
            j=0
            while j<len(high_list):
                if temp_line[i] in high_list[j]:
                    score+=1
                    #print("Rich fella here")
                j+=1
            i+=1


        i=0
        while i<len(temp_line):
            j=0
            while j<len(low_list):
                if temp_line[i] in low_list[j]:
                    score-=1
                    #print("Poor lad here")
                    #print(score)
                j+=1
            i+=1
            
            
        
        


        if score >= 0: #rich counter
            rich+=1
        else:
            poor+=1 #poor counter

    except IndexError:
        break

    
print("\nTotal population is",total_pop)
print("\nTotal rich people is", greater_pop)
print("Total poor people is", lesser_pop)

print("\nBased on classifier, total rich is",rich)
print("Based on classifier, total poor is",poor)

print("\nMargin of error is", (greater_pop-rich), "people out of", total_pop, "ie->", ((greater_pop-rich)/total_pop)*100,"%")





###############################################

#########***END MAIN***########################

###############################################
