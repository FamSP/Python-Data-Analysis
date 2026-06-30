import pandas as pd

# country = pd.read_csv(r"C:\Users\tame_\OneDrive\Desktop\Data Analyst\Python\Python-Data-Analysis\Pandas\Datafile\countries of the world.csv", header = None, names = ['Country' , 'Region'])
#df mean DataFrame And r mean rawtext
df = pd.read_csv(r"C:\Users\tame_\OneDrive\Desktop\Data Analyst\Python\Python-Data-Analysis\Pandas\Datafile\countries of the world.csv")
# print(df)

#separater
# dfTXT = pd.read_csv(r"C:\Users\tame_\OneDrive\Desktop\Data Analyst\Python\Python-Data-Analysis\Pandas\Datafile\countries of the world.txt", sep ='\t')
#can user read_table instade of csv it will auto saperate 
dfTXT = pd.read_table(r"C:\Users\tame_\OneDrive\Desktop\Data Analyst\Python\Python-Data-Analysis\Pandas\Datafile\countries of the world.txt")

# print(dfTXT)

# you can use table in csv file but you have to sep , in it
# dfTXT1 = pd.read_table(r"C:\Users\tame_\OneDrive\Desktop\Data Analyst\Python\Python-Data-Analysis\Pandas\Datafile\countries of the world.csv",sep =',')
# print(dfTXT1)


dfJson = pd.read_json(r"C:\Users\tame_\OneDrive\Desktop\Data Analyst\Python\Python-Data-Analysis\Pandas\Datafile\json_sample.json")
print(dfJson)
