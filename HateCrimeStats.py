# Data Analysis of Hate Crimes in USA
# Analyze the Data to discover and Visualize TRENDS

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV Data into Pandas Dataframe

df_HateCrime = pd.read_csv('hate_crime/hate_crime.csv')

#pd.set_option("display.max_columns",None)

# Drop Unimportant Columns
df_HateCrime = df_HateCrime.drop(['ORI', 'PUB_AGENCY_NAME', 'PUB_AGENCY_UNIT',
       'AGENCY_TYPE_NAME','DIVISION_NAME',
       'REGION_NAME', 'POPULATION_GROUP_CODE','INCIDENT_DATE','ADULT_OFFENDER_COUNT',
       'JUVENILE_OFFENDER_COUNT','MULTIPLE_OFFENSE',
       'MULTIPLE_BIAS','INCIDENT_ID','POPULATION_GROUP_DESC'], axis=1)
#print(df_HateCrime.columns)


############################################
# Hate-Crime Trend Over Time(Yearly 1991 - 2020)
############################################

# Data Re-Grouped Yearly
Data_by_Year = df_HateCrime.groupby(['DATA_YEAR'])

HateCrimePerYear = {}
for syn, group in Data_by_Year:
    HateCrimePerYear.__setitem__(syn, group.count()[1])

# Print the Data
# for i in HateCrimePerYear:
#     print(f"<>Year: {i} Incidents of HateCrimes: {HateCrimePerYear[i]}", end='\t\n')


# HateCrimes(Values) By Year(keys)
CrimeYear = list(HateCrimePerYear.keys())
Occurrence = list(HateCrimePerYear.values())

# Plot Data
plt.figure(1)
plt.bar(CrimeYear,Occurrence,color='black',edgecolor='blue')
plt.plot(CrimeYear,Occurrence, color='orange')
plt.xlabel("Individual Years")
plt.ylabel("Number Of Hate Crimes")
plt.title('Hate Crime Incidents (1991 - 2020)',fontweight='bold')


############################################
# Top 10 Years For HateCrime
############################################
plt.figure(2)
explode=(0.07,0.1,0,0,0,0,0,0,0,0)
(pd.value_counts(df_HateCrime['DATA_YEAR']).head(10)).plot.pie(autopct='%1.1f%%',shadow=True, startangle=90,explode=explode)
plt.ylabel("")
plt.title('Top 10 Years for Hate Crime',fontweight='bold')


############################################
#Crime Type Per Year
############################################
Df_Crime = df_HateCrime[['DATA_YEAR','BIAS_DESC']]

# Group By HateCrime
Df_Crime_Grouped = Df_Crime.groupby(['BIAS_DESC'])

CrimeGroup = {}
for group,value in Df_Crime_Grouped:
    if Df_Crime_Grouped.get_group(group).value_counts(sort=False).max() > 50:
        CrimeGroup.__setitem__(group, Df_Crime_Grouped.get_group(group).value_counts(sort=False))
crime = list(CrimeGroup.keys())
data = list(CrimeGroup.values())

# plot top 20 Crime Data
#for i in range(20,CrimeGroup.__len__()):
    #data[i].plot.line(label=crime[i],xticks=())
    #pass

# Data per HateCrime Category
CrimeType = CrimeGroup['Anti-Asian']

# Plot the Graph
plt.figure(3)
plt.bar(CrimeYear,CrimeType,color='gray',edgecolor='blue')
plt.plot(CrimeYear,CrimeType,color='red', label="Anti-Asian")
plt.legend(loc='best')
plt.xlabel("Years")
plt.ylabel("Number Of Hate Crimes ")
plt.title('Anti-Asian Hate Crime over 1991 - 2020)',fontweight='bold')


############################################
# Plot Comparison between Total HateCrime and Individual HateCrime
############################################
fig, ax1 = plt.subplots()
plt.figure(4)
colorax1 = 'black'
ax1.bar(CrimeYear,Occurrence,color=colorax1,label="Overall HateCrimes")
ax1.set_ylabel("No. OverAll HateCrimes")
ax1.legend(loc='best')

ax2 = ax1.twinx()

colorax2 = 'red'
ax2.plot(CrimeYear, CrimeType, color=colorax2, label="Anti-Asian")
ax2.set_ylabel('No. Anti-Asian',color=colorax2)
ax2.tick_params(axis='y', labelcolor=colorax2)
ax2.legend(loc='best')

plt.title('Anti-Asian Hate Crimes {VS} Overall Hate Crimes',fontweight='bold')


############################################
# Number of Crime Per state
############################################
Df_CrimePerState = df_HateCrime[['DATA_YEAR','STATE_NAME']]
#StateName = ['Alaska','New Jersey','California']

# Data of 2020
HateCrime2020 = Df_CrimePerState[Df_CrimePerState['DATA_YEAR'] == 2020]

# Instances of Hate Crime in per State
HateCrimePerState = HateCrime2020['STATE_NAME'].value_counts()

print("AVERAGE ",np.average(HateCrimePerState))
print(HateCrimePerState)
print(HateCrimePerState.describe())

# Plot Data
plt.figure(5)
HateCrimePerState.plot.bar(label='No. Hate Crimes')
plt.legend(loc='best')
plt.xlabel("States")
plt.ylabel("Number Of Hate Crimes ")
plt.title('2020 Hate Crime Per State',fontweight='bold')



############################################
# Top 10 States 2020 for Hate-Crime
############################################
TopState = HateCrimePerState.head(10)
plt.figure(6)
TopState.plot.pie(autopct='%1.1f%%',shadow=True, startangle=90,explode=(0.1,0,0,0,0,0,0,0,0,0),pctdistance=0.85)
plt.ylabel("")
plt.title('Top 10 State for Hate Crime 2020',fontweight='bold')


############################################
# Top 10 States for all time Hate-Crime
############################################
plt.figure(7)
(pd.value_counts(df_HateCrime['STATE_NAME']).head(10)).plot.pie(autopct='%1.1f%%',shadow=True, startangle=90,explode=(0.1,0,0,0,0,0,0,0,0,0),pctdistance=0.85)
plt.ylabel("")
plt.title('Top 10 State for Hate Crime 1991 - 2020',fontweight='bold')


############################################
# Types of Crime in 2020
############################################
Df_TypeofCrime = df_HateCrime[ ['DATA_YEAR','BIAS_DESC'] ]
# Segregate According to Year(2020)
Df_TypeofCrime2020 = Df_TypeofCrime[Df_TypeofCrime['DATA_YEAR']==2020]

# plot Data
plt.figure(8)
explode=(0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07,0.07)
Df_TypeofCrime2020['BIAS_DESC'].value_counts().head(10).plot.pie(autopct='%1.1f%%',explode=explode,pctdistance=0.85)
plt.ylabel("")
plt.axis('equal')
plt.title('Top 10 Hate Crime 2020',fontweight='bold')

#draw Circle
center_circle = plt.Circle((0,0),0.75,fc='white')
circleFig = plt.gcf()
circleFig.gca().add_artist(center_circle)
plt.show()














