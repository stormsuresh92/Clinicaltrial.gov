import requests
import pandas as pd
from time import sleep
from tqdm import tqdm

'''
https://ClinicalTrials.gov/api/query/full_studies?expr=heart+attack
https://ClinicalTrials.gov/api/query/study_fields?expr=heart+attack&fields=NCTId,Condition,BriefTitle
https://ClinicalTrials.gov/api/query/field_values?expr=heart+attack&field=Condition
https://clinicaltrials.gov/api/query/study_fields?fmt=json&expr=NCT05058196&fields=NCTId,CentralContactRole,CentralContactName,CentralContactPhone,CentralContactEMail,LocationContactRole,LocationContactName,LocationFacility,LocationContactPhone,LocationContactEMail,LocationStatus,LocationCity,LocationState,LocationZip,LocationCountry,OverallOfficialRole,OverallOfficialName,OverallOfficialAffiliation,ResponsiblePartyInvestigatorFullName,ResponsiblePartyInvestigatorAffiliation,ResponsiblePartyInvestigatorTitle,ResponsiblePartyType
'''


payload={}
headers = {
  'Cookie': 'CTOpts=Qihzm6CLCi1zKQhihyUgzw-R98Fk3R4i4B1l; Psid=vihzm6CLCi1zKQhihyz3FQ7V9gCkkKhy56CBa6CJa60jOgzqaBFG5K4HCD8V',
  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'
}

print('API calling...')
alldata = []
file = open('nctids.txt', 'r')
ids = file.readlines()
for nct in tqdm(ids):
	start = "https://clinicaltrials.gov/api/query/study_fields?fmt=json&expr="
	end = "&fields=NCTId,CentralContactRole,CentralContactName,CentralContactPhone,CentralContactEMail,LocationContactRole,LocationContactName,LocationFacility,LocationContactPhone,LocationContactEMail,LocationStatus,LocationCity,LocationState,LocationZip,LocationCountry,OverallOfficialRole,OverallOfficialName,OverallOfficialAffiliation,ResponsiblePartyInvestigatorFullName,ResponsiblePartyInvestigatorTitle"
	response = requests.get(start+str(nct.strip())+end, headers=headers, data=payload)
	json_data = response.json()
	for value in json_data['StudyFieldsResponse']['StudyFields']:
		dic = {
			'NCTId':value['NCTId'],
			'CentralContactRole':value['CentralContactRole'],
			'CentralContactName':value['CentralContactName'],
			'CentralContactPhone':value['CentralContactPhone'],
			'CentralContactEMail':value['CentralContactEMail'],
			'LocationContactRole':value['LocationContactRole'],
			'LocationContactName':value['LocationContactName'],
			'LocationFacility':value['LocationFacility'],
			'LocationContactPhone':value['LocationContactPhone'],
			'LocationContactEMail':value['LocationContactEMail'],
			'LocationStatus':value['LocationStatus'],
			'LocationCity':value['LocationCity'],
			'LocationState':value['LocationState'],
			'LocationZip':value['LocationZip'],
			'LocationCountry':value['LocationCountry'],
			'OverallOfficialRole':value['OverallOfficialRole'],
			'OverallOfficialName':value['OverallOfficialName'],
			'OverallOfficialAffiliation':value['OverallOfficialAffiliation'],
			'ResponsiblePartyInvestigatorFullName':value['ResponsiblePartyInvestigatorFullName'],
			'ResponsiblePartyInvestigatorTitle':value['ResponsiblePartyInvestigatorTitle']
		}
		alldata.append(dic)
		sleep(1)


df = pd.DataFrame(alldata)
df.to_csv('ClinicalTrial_Output.csv', index=False)
print('API Calling Done')




