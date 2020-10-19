import pandas as pd

# Dataframe = pandas.read_csv(<path to .csv file>)
df = pd.read_csv('stflow_data/survey_results_public.csv')
print('data:', df)
print('Rows and Columns:', df.shape)
print('Info of all the columns and file: ', df.info())

# To get all the columns in jupyter notebook
pd.set_option('display.max_column', 61)

'''
Any data returned by a function is of type (Series)
'''

'''
Indexers
'''
#To see all the column values for a particular row
#iloc = integer Location
# 0 = index
df.iloc[0]
# for row 0 and 1 and only the 3rd column
df.iloc[[0,1], 2]

#location with definite columns
df.loc[[0,1], 'email']

#Slicing
df.loc[0:2, 'Hobbyist':'Employment']

# top 15 salaries in Dataframe. (This is not sorted.. just 1-15 enteries in the Data we have)
df['ConvertedComp'].head(15)

'''
Index
'''
# this will make 'email' as index column. But not for the entire dataframe
df.set_index('email')

# Inplace=True will make the change effective for entire dataframe
df.set_index('email', inplace=True)

# to see index
df.index

# Now, since index is not integer anymore, loc() and iloc() won't work with integers
# to reset
df.reset_index(inplace=True)

# To make a column from Data as the unque_index value
df = pd.read_csv('stflow_data/survey_results_public.csv', index_col = 'Respondent')
#Now, this will work
df.loc['email']
schema_df.loc['Hobbyist', 'QuestionText']

#Sorting Indexes
# Default ascending
df.sort_index()
#Descending sort
df.sort_index(ascending=False)
#To make sort permanent for the Dataframe
df.sort_index(inplace=True)


'''
Filter
'''
df['last'] == 'Doe'
# This will return a True/False Sequence for the rows that matches the filter
# This is called a 'Mask'.
# To get the data
filt = df['last']=='Doe'
df[filt]
# -> df[df['last']=='Doe'] ... will also work

# This will do the same thing as df[filt] but we can add more filters to the results. Eg: select column
df.loc[filt, 'email']

# Multiple Filters
filt = (df['last']=='Doe') & (filt = df['first']=='John')

filt = (df['last']=='Doe') | (filt = df['last']=='Jones')

# To get 'Not-Filter' result: eeverything outside filter
df.loc[~filt, 'email']

# Select Greater-than
high_salary = df['ConvertedSal']>70000
df.loc[high_salary, [<column names we need to see- List of Strings>]]

# Want results to be filtered as per list entries
countries = ['US', 'UK', 'Canada', 'India']
c_filt = df['country'].isin(countires)
df.loc[c_filt, 'country']

# Check string in a column with multiple strings as value
# na=False will disregard anything that has Nan, None, etc as value
filt = df['LanguageWorkedWith'].str.contains('Python', na=False)


'''
Alter/Update data in rows and columns in DataFrame
'''
# Look at columns
df.columns

# change all column names of a Dataframe
df.columns = ['First_name', 'Last_name', 'Email']
#OR use List Comprehensions as well
df.columns = [x.upper() for x in df.columns]
df.columns = df.columns.str.replace(' ', '_')

# Updating a specific column and make the change permanent for the dataframe.
df.rename(columns={'first_name': 'First', 'last_name': 'Last'}, inplace=True)

# Update data in a row.
df.loc[2]	# OR any other conditional to grab the target value
#df.loc[2] = [<column wise data that we want to have in that row.>]
df.loc[2] = ['John', 'Smith', 'johnsmith@mailinator.com']

# update value for specific column
df.loc[2, ['last', 'email']] = ['Smith', 'johnsmith@mailinator.com']

'''
# apply: apply a function to every value in the series.
# map: works for Series. Used to substitute EACH value in 'Series' with another Value.
#		* If no substitute value provided, the element in Series will be replaced with NaN.
#		* Either give a Subsitute value for all the elements in Series, or we will have 'NaN' as values
#			for those we did not provide values for.
# applymap: only works on Dataframe. Cannot use it for Series.
# replace: works for Series. USed to substitute 'selected' values in 'Series' with 'given' new value
'''

df['email'].apply(len) #-> Will give the length of all elements in the email column.
# apply(callable function as argument)
# the above statement is 'apply(fn)' on each element of the Series returned bt df['email']

# 'apply(fn)' of the entire dataframe will give us data of each column
df.apply(len)

# we can have the function applies row-wise as well. By default, axis=rows
df.apply(len, axis=columns)

# to get the minimum or maximum of a series
df.apply(pd.Series.min)
df.applt(lambda x: x.min()) #-> X is a series here. So, we need to use Series methods

# This will apply 'len' to each value/element in the Entire Dataframe
df.applymap(len)	# We can use any callable for this

#Make entire Dataframe lowercase
df.applymap(str.lower())

# series.map({Current value: New Value})
df['first'].map({'Corey':'Chris', 'Jane': 'Mary'})
# This will make any other value in Column 'First' == NaN

# To not make all the other values NaN
df['first'].replace({'Corey':'Chris', 'Jane': 'Mary'})

'''
Dictionary into Pandas DataFrames
'''
people = {
    'first': ['Corey', 'Delores', 'Jones'],
    'last': ['Stark', 'Rogers', 'Banner'],
    'email': ['cs@mail.com', 'dr@mail.com', 'jb@mail.com']
}
dfp = pd.DataFrame(people)

#Add column to Dataframe
df['fullname'] = df['first']+ ' ' + df['last']

#drop column
df.drop(columns=['first', 'last'], inplace=True)

#drop Row
df.drop(index=4, inplace=True)

# Conditional Drop of row data
# df[...].index 	-> returns indexs of all the rows that matches the condition 
df.drop(index=df[df['last']=='Dou'].index)

# Split column into multiple columns
# Split('') -> will create a list of values after splitting the string
# expand=True -> will make columns as per the lenght of List
# dfp[['first', 'last']] -> will ne new column names. Default is 0,1,2...
dpf[['first', 'last']] = dfp['full_name'].str.split('', expand=True)


'''
1. Adding a row of data in DataFrame
2. Appending 2 DataFrames to create a new DataFrame
'''

# This will add 1 row in DataFrame
# ignore_index= True	-> will put NaN for all the not-given values for the columns.
dfp.append({'first': 'Tony'}, ignore_index=True)

# This will append 2 DataFrames
# ignore_index= True	-> will put NaN for all the unmatched columns.
dfp.append(df_p, ignore_index=True)

# This is not an inplace Append, like we have for Lists in Python
# We nend to assign it to another variable to keep the changes
dfp_f = dfp.append(df_p, ignore_index=True)


'''
Soritng Data
Getting Largest and Smallest
'''

# Default is True but we can do Descennding
# 'by' -> column
dfp_f.sort_values(by='last', ascending=False)

# if there are multiple things we want to sort the data by in case of equalities in 1st column.
#	(in case 2 people have same last_name)
# 2nd column sort happens only for those rows that have same values for the sorted column
dfp_f.sort_values(by=['last', 'first'], ascending=False)
# if we want a different sequence for sorting 2nd column
dfp_f.sort_values(by=['last', 'first'], ascending=[False, True])

# sort_values() can be used for Series as well.
dfp_f['email'].sort_values()

# This will give just the column data
df['ConvertedComp'].nlargest(10)
df['ConvertedComp'].nsmallest(10)

# To see the entire data for the 'nlargest' or 'nsmallest'
df.nlargest(10, 'ConvertedComp')
df.nsmallest(10, 'ConvertedComp')



'''
Aggregation: Combining multiple pieces of Data and form a Result.
	-> Mean, Median, Mode of a sample-space
	-> Average Salary in a Dataframe
Grouping: Collection of data based on a Criteria
	-> Eg: Grouping is required for - Most popular Social Media in each Country
	
	-> Group By:
		Split the object -> Apply Function -> Combine Results


'''

# Median Salary
dfp_f['ConvertedComp'].median()

dfp_f.median()
# Above will go over entire DataFrame and give out median for all the numberical Columns.

# To see many Statistical values on entire DataFrame Numerical Columns
# We can use this for Series as well
dfp_f.describe()
dfp_f['ConvertedComp'].describe()

#Count: Give total non NaN rows count.
dfp_f['ConvertedComp'].count()

# Value_counts: Gives count for all different values in a column
# Like No. of Yes and No
dfp_f['Hobbyist'].value_counts()
dfp_f['SocialMedia'].value_counts()
#Normalize -> gives percentage people on that value
dfp_f['SocialMedia'].value_counts(normalize=True)

df['Country'].value_counts()


# GROUPING

# groupby(<list of columns to group-on>)
country_gp = df.groupby(['Country'])
# This will return as 'DataFrameGroupBy' Object.
# This onject has a collection of groups.
# To access each group, use: get_group()
country_gp.get_group('United States')

country_gp['SocialMedia'].value_counts()
country_gp['ConvertedComp'].median()

# To see multiple of the Aggregates on Grouped Data
# Returns a DataFrame
country_gp['ConvertedComp'].agg(['median', 'mean'])

# People that said they know Python and are from India
# Basically, Search for a string-match in 1 column for all countries
filt = df['Country']=='India'
df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()

# These types of objects are 'SeriesGroupBy' Objects.
# 'str' operations will not work on it.
# Need to use 'Apply' Method
python_people = country_gp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())

# Percentage of people know Python in each country
# (People know Python)/(Total People from each Country)
people_from_country = df['Country'].value_counts()

# Work with 2 Series.
#	Concatinate
python_df = pd.concat([people_from_country, python_people], axis='columns', sort=False)

python_df.rename(columns={'Country':'Total_People', 'LanguageWorkedWith':'Python_people'}, inplace=True)
python_df['Python_People_Percentage'] = (python_df['Python_people']/python_df['Total_People'])*100
python_df.sort_values(by='Python_People_Percentage', ascending=False)

'''
1. Handle Missing Data
2. Convert Datatypes of the Data
'''

# Drops all the rows that has 'ANY' column as 'NA'/'NaN'/'None'
df.dropna()
# default value of dropna is
df.dropna(axis='index', how='any')

df.dropna() == df.dropna(axis='index', how='any')

#Give all the NA values = 0
df.fillna(0)

#Give True/False for all the elements in DataFrame
df.isna()

# Replace 'Missing' 'NA' with type(NaN) in Manual Data
df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)

# Replace 'Missing' 'NA' with type(NaN) in CSV data
# The list will provide all the values that needs to be replaced with 'NA'
na_vals = ['NA', 'Missing', 'N/A']
df = pd.read_csv('stflow_data/survey_results_public.csv', index_col='Respondent', na_values=na_vals)

# To get all the unique values in a column
df['YearsCode'].unique()

# Column Value Replace
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)

#Convert Column into type(int)
df['age'] = df['age'].astype(int)

# If there is even 1 element in the column as NaN or NA,
# since they are type(float), we need to convert the column to Float
# Or Convert NA to 0.. But depends on Data.. if you are calculating Average, converting is not good
df['age'] = df['age'].astype(float)

# Now we can use operations like 'mean()', 'median()'.. etc
df['age'].mean()


'''
Date and Time in Pandas
'''

# But it might not work, depending on the original format
df['Date'] = pd.to_datetime(df['Date'])

# Provide the format original Data is in to Pandas
# Python Datetime formating: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')

# Day on a date
df.loc[0, 'Date'].day_name()

# To Convert Datetime Columns to Datetime Object while creating the DataFrame while Reading Csv File
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('csvfilepath.csv', parse_dates=['Date'], date_parser=d_parser)

# To run Datetime operations on the entire Series
# This will give Day for all the dates in the column
df['Date'].dt.day_name()

# Filter Data by Dates
filt = (df['Date'] >= 2020)
df.loc[filt]

filt = (df['Date'] >= 2019) & (df['Date'] < 2020)
df.loc[filt]

filt = (df['Date'] >= pd.to_datetime('2019-01-20')) & (df['Date'] < pd.to_datetime('2020-02-19'))
df.loc[filt]

# If we make the Date column as Index, we can use access yearly data like df['2019'] or df.loc['2019']
df.set_index('Date', inplace=True)
df['2019']
df.loc('2019')
df['2019-01-20':'2020-02-19']

# Convert Stock Data from 'Hourly-basis' to 'Daily-basis'
# Get the max of the day
day_max = df['2019-01-01']['High'].max()
day_min = df['2019-01-01']['Low'].min()

# For Resampling: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects
# Get High for the whole column on Day-Basis
# resample.('D').max()	-> we need to tell what to do with the resampled data. Like get max(). min(), mean()
highs = df['High'].resample('D').max()
lows = df['Low'].resample('D').min()

# Get entire DataFrame resampled
df.resample('W').mean()

# Stocks Data
df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})


'''
Reading Different Data Files
'''

###### CSV
# Reading
df_csv_read = pd.read_csv('Full_path_to_csv.csv', index_col='Optional to set Index Column')
# -> Tab Delimited
df_csv_read = pd.read_csv('Full_path_to_csv.csv', index_col='Optional to set Index Column', sep='\t')

# Writing
df_csv_write.to_csv('PAth_to_folder/new_data.csv')
# -> fAB Delimited file
df_csv_write.to_csv('PAth_to_folder/new_data.tsv', sep='\t')


###### EXCEL : pip install xlwt xlrd openpyxl
# Writing
df_excel_write.to_excel('PAth_to_folder/new_data.xlsx')
# -> Write to a Sheet (we can also define which column to start at)
df_excel_write.to_excel('PAth_to_folder/new_data.xlsx', sheet=2)

# Reading
df_excel_read = pd.read_excel('path_to_excel_file.xlsx', index_col='Optional to set Index Column')


###### JSON FILE
# writing
df_json_write.to_json('PAth_to_folder/new_data.json')
# writing as list
df_json_write.to_json('PAth_to_folder/new_data.json', orient='records', lines=True)

# Reading
df_json_read = pd.read_json('Full_path_to_json.json', orient='Optional Argument to fit data')


###### SQL/POSTGRES DATABASE :
# SQL, SQLite: pip install SQLAlchemy
# PostGreSQL (additional to SQL package): pip install psycopg2-binary

from sqlalchemy import create_engine
import psycopg2

# Writing
#DB_Connection
engine = create_enginer('postgresql://dbuser:dbpass@localhost:5432/my_db_name')

# it will get created.
df_sql_write.to_sql('my_table_name', engine)

# If table exist. (if_exists='replace'/'append'/'error (default)')
df_sql_write.to_sql('my_table_name', engine, if_exists='replace')


# Reading
df_sql_read = pd.read_sql('my_table_name', engine, index_col='Optional to set Index Column')

# Run Query and Read Data
df_sql_read_from_query = pd.read_sql_query('SELECT * FROM my_table_name', engine)


###### URL:
# Need to know what kind of Data is going to come from the URL
# Eg: JSON

df_url = pd.read_json('URL_pasted')