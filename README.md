First we have to install the pandas library through pip
----------Pip install pandas

Then import the pandas library into our project using import
----------import pandas

What is the use of pands???
Pandas is used for data reading, data manipulation, analysis and cleaning.

Loading data:
1. df = pd.read_csv(‚path name‘)
2. print(df.head(5))--------to print first 5rows on data
3. print(df.tail(5))-----------to print last 5rows of data

Reading data:
4. Print(df.columns) ----------to read headers
5. Print(df[‘Name1’,’city’]) ------to see individual columns
6.Print(df.iloc[1]) ----------print the index row of 1
Iloc means integer location
7. Print(df.iloc[1:4]) ------print the 1 to 3 index rows
Or
For index,row in df.iterrows():
Print(index,row[‘name’])
8.df.loc[df[‘Type1’] == ”Fire”]]---to read only specific condition met I mean I want to see when type1==fire


Sort/describing data:
9.df.sort_values(‘Name’, ascending=False)------------it can sort by name
10. df.sort_values([‘Name’, ‘Hp’], ascending=[1,0])------------name should be ascending means a-z and hp should be descending

Making changes to the data:

11.df[‘Total’]=df[‘HP’]+df[‘Attack’]+df[‘Defense’]+df[‘sp.atk’]---to add new column total
Or
df[‘Total’]=df.iloc[:, 4:8].sum(axis=1)------4:8 is adding columns 4 to 7 vertically(axis=1 is vertical adding)
12.df=df.drop(columns=[‘Total’])-----to delete an column total

13.cols = list(df.columns)
      df=df[cols[0:4]+[cols[-1]]+cols[4:12]]-----changing last column position into 4th position

To save data:
14. df.to_csv(‘modified.csv’, index=False)



Filtering data:
15.df.loc[df[‘Type1’] == Grass & df[‘Type2’] == poison]----we can only get rows where type1 == grass and type2 ==posion.
16. new_df = df.loc[(df[‘Type1’] == Grass | df[‘Type2’] == poison]) & (df[‘Hp’]>70)]-------if we want we can also change it into new variable
17.new_df = new_df.reset_index()----------if we want we can reset the index also
18. new_df.reset_index(inplace=True)----------if we don’t want to assign to variable and we want change inplace itself we can enable inplace = True.
19. df.loc[df[‘Name1’].str.contains(‘Mega’)]-----it will give the strings which contains names with mega
20. df.loc[~df[‘Name1’].str.contains(‘Mega’)]-----it will give the names which does not contain mega


Import re: regular expressions are super powerful to filtering data on certain textual patterns.
21. df.loc[df[‘Type1’].str.contains(‘Fire | Grass’), regex= True)]------The f and g should be capital because must given same as in the table

22. df.loc[df[‘Type1’].str.contains(‘fire | grass’), flags= re.I, regex= True)]------flags=re.I is a ignore case to ignore
23. df.loc[df[‘Name1’].str.contains(‘pi[a-z]*’, flags= re.I, regex= True)]------it will give the names which contains pi
24. df.loc[df[‘Name1’].str.contains(‘^pi[a-z]*’, flags= re.I, regex= True)]------it will give names only begins with pi

Conditional changes:

25. df.loc[df[‘Type1’]== ‘Fire’, ‘Type1’] = ‘Flammer’----where type1 = fire change type1 value to Flammer.
26. df.loc[df[‘Type1’]== ‘Fire’, ‘legendary’] = True---where type1 == fire the legendary will field will changed to true.


To change multiple values at a time when certain condition is met
27. df.loc[df[‘Total’]>500, [‘Type1’,’legendary’] ]= ‘test value’—where total is greater than 500 change type1 and legendary fields to test value

Aggreagate statistics(Groupby):
28. df.groupby([‘Type1’]).mean().sort_values(‘Attack’, ascending=False)--------attack is the field in the database table.it will give the average attacks of type1 in sorted order
29.df.groupby([‘Type1’]).sum()------we can also sum 
30. df.groupby([‘Type1’]).count()------we can count how many type1 itmes are similar
31. df[‘count’]=1----adding the count column
32.df.groupby([‘Type1’].count()[‘count’]---
33. df.groupby([‘Type1’,’Type2’].count()[‘count’]---we can also do it multiple fields like type1 and type2

Working with large data sets:

34.for df in pd.read_csv(‘modified.csv’, chunksize=5):
              Print(df)----it will print the dataframe into chunks of 5 rows each.

35.new_df=pd.DataFrame(columns=df.coulumns)
      for df in pd.read_csv(‘modified.csv’, chunksize=5):
                  results=df.groupby([‘Type1’]).count()
                  new_df=pd.concat([new_df, results])



