import pandas as pd
import numpy as np
import statistics

teams_data = pd.read_csv('./baseballdatabank-2022.2/baseballdatabank-2022.2/core/Teams.csv', usecols=['yearID','teamID'])

people_data = pd.read_csv('./baseballdatabank-2022.2/baseballdatabank-2022.2/core/People.csv', usecols=['playerID','birthYear'])
people_data['birthYear'].replace('', np.nan, inplace=True)
people_data['birthYear'].replace([], np.nan, inplace=True)
people_data.dropna(subset=['birthYear'], inplace=True)
print(people_data)

pitch_data = pd.read_csv('./baseballdatabank-2022.2/baseballdatabank-2022.2/core/Pitching.csv', usecols=['playerID','yearID','teamID','ERA'])
pitch_data['ERA'].replace('', np.nan, inplace=True)
pitch_data.dropna(subset=['ERA'], inplace=True)

print('median era')

med_era = {}

for index, row in pitch_data.iterrows():
	if row['yearID'] in med_era:
		if row['teamID'] in med_era[row['yearID']]:
			med_era[row['yearID']][row['teamID']]['eras'].append(float(row['ERA']))
		else:
			med_era[row['yearID']][row['teamID']] = {}
			med_era[row['yearID']][row['teamID']]['eras'] = [float(row['ERA'])]
	else:
		med_era[row['yearID']] = { row['teamID']:{} }
		med_era[row['yearID']][row['teamID']]['eras'] = [float(row['ERA'])]

for year in med_era:
	for team in med_era[year]:
		#print(teams_data.loc[(teams_data['yearID'] == year) & (teams_data['teamID'] == team)].index)
		team_med_era = statistics.median(med_era[year][team]['eras'])
		team_index = teams_data.loc[(teams_data['yearID'] == year) & (teams_data['teamID'] == team)].index
		teams_data.loc[team_index, 'medianERA'] = team_med_era

print(teams_data)

print('avg pitcher age')

avg_age = {}

print('processing')

for index, row in pitch_data.iterrows():
	if row['playerID'] in people_data['playerID'].values:
		pitcher_age = int(row['yearID']) - int(people_data.loc[people_data['playerID'] == row['playerID']]['birthYear'])
		if row['yearID'] in avg_age:
			if row['teamID'] in avg_age[row['yearID']]:
				avg_age[row['yearID']][row['teamID']]['ages'].append(pitcher_age)
			else:
				avg_age[row['yearID']][row['teamID']] = {}
				avg_age[row['yearID']][row['teamID']]['ages'] = [pitcher_age]
		else:
			avg_age[row['yearID']] = { row['teamID']:{} }
			avg_age[row['yearID']][row['teamID']]['ages'] = [pitcher_age]
	else:
		print(f"{row['playerID']} not found in people_data")

print('filling in team data')

for year in avg_age:
	for team in avg_age[year]:
		team_avg_age = statistics.mean(avg_age[year][team]['ages'])
		team_index = teams_data.loc[(teams_data['yearID'] == year) & (teams_data['teamID'] == team)].index
		teams_data.loc[team_index, 'pitcherAverageAge'] = team_avg_age

print(teams_data)
