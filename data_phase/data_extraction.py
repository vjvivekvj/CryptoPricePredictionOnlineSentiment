import datetime
import requests
import csv


def list_snapshots():
	print("Fetching history")
	history = requests.get('https://api.senticrypt.com/v1/history/index.json')
	return history.json()


def collect_data(link):
	print("Extracted data till "+ link)
	result = requests.get('https://api.senticrypt.com/v1/history/' + link)
	return result.json()

def create_csv(result):
	print("Adding values to csv")
	f = open("dataset.csv", "w", newline = '')
	writer = csv.writer(f)
	for entry in result:
		data = []
		for i in sorted(entry.keys()):
			if i=="timestamp":
				data.append(datetime.datetime.fromtimestamp(entry[i]).strftime('%Y-%m-%d %H:%M:%S'))
			else:
				data.append(entry[i])
		writer.writerow(data)
	f.close()

if __name__ == "__main__":
	history = list_snapshots()
	count = 0
	for hour_data in history:
		if hour_data == "index.json" or count > 1000:
			break 
		result = collect_data(hour_data)
		create_csv(result)
		count += 1
