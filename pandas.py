'''============data frame using dictionary assigning the dictionaries are column wise============='''

# import pandas as pa
# a={'s no':[1,2,3,4,5],'name':['goutham','raju','umesh','ravi','manoj'],'loc':['hyd','bng','hyd','chennai','wgl']}
# b=pa.DataFrame(a)
# print(b)

#output
'''   s no     name      loc
   0     1  goutham      hyd
   1     2     raju      bng
   2     3    umesh      hyd
   3     4     ravi  chennai
   4     5    manoj      wgl '''

# print(b.head(2))

#output
'''
   s no     name  loc
0     1  goutham  hyd
1     2     raju  bng

'''
# print(b.tail(2))

#output
'''
   s no   name      loc
3     4   ravi  chennai
4     5  manoj      wgl
'''

'''==================dataframe using list assigning the values is row wise===================='''

# import pandas as pa
# list=[[101,'goutham','may'],[102,'babu','jun'],[103,'niharika',],[104,'ravi','jun'],[105,'shahid','jul'],[106,'pravalika','jul']]
# l=pa.DataFrame(list,columns=['sid','sname','doj'])
# # print(l)
#output
'''   sid      sname   doj
    0  101    goutham   may
    1  102       babu   jun
    2  103   niharika  None
    3  104       ravi   jun
    4  105     shahid   jul
    5  106  pravalika   jul'''
# shape written the size of the table (rows,columns)
# print(l.shape) #(6,3)
'''==========================================='''

# f=pa.read_csv("pandas_demo.csv")
# print(f)
# print(f.shape)#(8, 4)

'''========================================================='''
# a=pa.read_csv("E:\excel\pandas_demo1.csv")
# print(a)
#output
'''   Emp ID      Ename       Role      Sal  experience
0   13516    goutham    manager  1500000           8
1   13517       rana  developer   800000           6
2   13518     nithin  developer   800000           6
3   13519   raviteja    testing   700000           6
4   13520    mahesh     testing   700000           6
5   13521        ntr   database   800000           6
6   13522  ramcharan   database   800000           6
'''


'''======================================================'''
# head() gives first 5 records it is default
# tail() gives last 5 records it is default
# f=pa.read_csv("pandas_demo.csv")
# print(f.head())
# print(f.tail())

# print(f.head(6))
# print(f.head(3))
# print(f.head(8))
# print(f.tail(3))
# print(f.tail(6))
# print(f.tail(9))


'''================printing of rows using slicing============='''
# import pandas as pa
# doc=pa.read_csv('pandas_demo.csv')

# print(doc[ : ])# print the total coloumn and row information

# print(doc[3:5]) #print the 3 and 4th record  total information

# print(doc[9:21])#print the 9 to 20 th record total information

# print(doc.columns) #print the only column information
                   # Index(['SID', 'SNAME', 'DOJ', 'course'], dtype='object')

# print(doc.course) # it gives particular column information

# print(doc[['course','SNAME']]) #we can print multiple column information

'''============for aggrigate data information like max,min,count,mean,median========='''

# d=pa.read_csv("pandas_demo.csv")

# print(d)
# print(d['fee'].max()) # 15000
# print(d['fee'].min()) # 2563
# print(d['fee'].count()) #8
# print(d['fee'].value_counts()) #value_counts() gives count of repeated values
# print(d['fee'].mean()) #6960.25 
# print(d['fee'].median()) #5488.0 
# print(d['fee'].std()) #5129.809318372091

# print(d.describe())

#output

'''
             SID           fee
count    8.00000      8.000000
mean   104.50000   6960.250000
std      2.44949   5129.809318
min    101.00000   2563.000000
25%    102.75000   3390.750000
50%    104.50000   5488.000000
75%    106.25000   8172.000000
max    108.00000  15000.000000
'''

# d=pa.read_csv("pandas_demo.csv")
''' by mentioning like d[d.fee < 2999] check the condition and  we get total record information'''
# print(d[d.fee < 2999])

# output
'''
    SID   SNAME  DOJ       course   fee
 3  104   manoj  may  Datascience  2563
 6  107  shahid  aug         Java  2589
'''

'''if [d.fee < 2999] check the condition and gives only true or false'''

# print([d.fee < 2999])

# output
'''
[0    False
1    False 
2    False 
3     True 
4    False
5    False
6     True
7    False
Name: fee, dtype: bool]
'''


# print(d[d.course=='python'])

# output
'''
   SID   SNAME  DOJ  course    fee
0  101  goutam  feb  python  15000
7  108  venkat  sep  python   3658
'''


'''================================='''
# import pandas as pa
# a=pa.read_csv('pandas_demo.csv')

# print([a.SNAME])#give only names

# print(a['SNAME'][a.fee>10000])#0     goutam
                              # 1    sathwik

# print(a[a.fee>10000])#we get the total information bout the person whose fee greater than 10000

# print(a[a.fee==a.fee.max()])

# output
'''
   SID    SNAME  DOJ     course    fee
0  101   goutam  feb     python  15000
1  102  sathwik  mar  Fullstack  15000
'''
# print(a.shape) #(8, 5)

# print(a.loc[6])  #we get the 6th record information

'''
SID          107      
SNAME     shahid      
DOJ          aug      
course      Java      
fee         2589      
Name: 6, dtype: object
'''
''' To keep the SID as the index number or any column name as index number use--> set_index()'''
# print(a)
# print(a.set_index('SID'))
# print(a.set_index('SNAME'))

'''method available in pandas'''
# print(dir(pa))
'''to read excel file we need install openpyxl pakage'''
# excel=pa.read_excel('pandas_excel_demo.xlsx')
# print(excel)
'''to read html file we need install beautifulsoup4 pakage'''
# html=pa.read_html('studentlogin.html')
# print(html)


'''to read CSV file install xlrd pakage'''

'''for data visualization install matplotlib'''
