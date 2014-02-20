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

    # reset file
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

######################end keith################
###########################################


f=open('myfile.txt', 'r')

whatev=data(f)

print(whatev)
