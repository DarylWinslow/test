
#Find Average function
def find_average(num_people, total):
    avg=total/num_people
    return int(avg)


#####################keith function#######

def data(f):
    
    #Database / dictionarys
    workclass = {}
    id_num = {}
    education = {}
    education_number = {}
    marital_status = {}
    occupation = {}
    relationship = {}
    race = {}
    sex = {}
    capital_gain = {}
    capital_loss = {}
    hours_per_week = {}
    native_county = {}

    # Temp string to hold line
    temp_line = ''

    # reset file back to line one
    f.seek(0,0)

    # Go through file
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

                if temp_line[12] in hours_per_week:
                    hours_per_week[temp_line[12]] +=1 
                else:
                    hours_per_week[temp_line[12]] =1 

            except IndexError:
                break
            
    #Dictionary to return
    data = {'workclass':workclass, 'id_num':id_num, 'education':education,
            'education_number':education_number, 'marital_status':marital_status,
            'occupation':occupation, 'relationship':relationship, 'race':race, 'sex':sex,
            'capital_gain':capital_gain, 'capital_loss':capital_loss,
            'hours_per_week':hours_per_week, 'native_county':native_county              }
        
    print("\n----------Debug Test---------------")

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

######################end keith################
###########################################




###############################################

#########***MAIN***############################

###############################################

#open database
fh=open("myfile.txt", 'r')

#Create higher/lower databases
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


        

print("Total number of people is", total_pop)

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
print("Average hours/week of the poor is", find_average(lesser_pop, lesser_hpw))

#Create high/low dictionaries
high_dictionary=data(highfile) #call keith's function
low_dictionary=data(lowfile)

print (high_dictionary['workclass'])
print (low_dictionary['workclass'])

print(high_dictionary['workclass']['Private'])
#Self-emp-inc = (dictionary['workclass'][' Private'])
#private = (dictionary['workclass'][' Private'])










###############################################

#########***END MAIN***########################

###############################################
