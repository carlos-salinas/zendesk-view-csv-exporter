# Functionaly: Retrieve the tickets associated to the Mx4PC (Mendix for Private Cloud) view
# on Zendesk and output the response into a CVS file
# Author: Carlos Salinas
# Note: This script in based on a Zendesk example 
# https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/exporting-a-ticket-view-to-a-csv-file-with-python/

import requests, csv, sys

if len(sys.argv) != 4:
	print('The list of parameters is invalid. Please pass <email>/token, <password> and <zendesk_view_id> in that order')

auth = sys.argv[1], sys.argv[2]
view_id = sys.argv[3]
view_tickets = []

print(f'Getting tickets from view with ID {view_id}')
url = f'https://mendixsupport.zendesk.com/api/v2/views/{view_id}/tickets.json'
while url:   
	response = requests.get(url, auth=auth)
	page_data = response.json()
	tickets = page_data['tickets']
	view_tickets.extend(tickets)
	url = page_data['next_page']

# Initialize rows with an initial header row
rows = [('Ticket ID', 'Subject', 'Description', 'Organization', 'Created', 'Priority', 'Status', 'Satisfaction', 'URL')]

# Define a row per ticket and append
for ticket in view_tickets:
	# Retrieve organization name
	org_id = ticket['organization_id']
	org_name = ""

	if org_id != None:
		url = f'https://mendixsupport.zendesk.com/api/v2/organizations/{org_id}'
		response = requests.get(url, auth=auth)
		org_details = response.json()
		org_name = org_details['organization']['name']		

	row = (
		ticket['id'],
	    ticket['subject'],
	    ticket['description'],
	    org_name,	
	    ticket['created_at'],
	    ticket['priority'],
	    ticket['status'],
	    ticket['satisfaction_rating']['score'],
	       f'https://mendixsupport.zendesk.com/agent/tickets/{ticket["id"]}'
	) 
	rows.append(row)

# Create csv file to ouput the queried data
with open('export-tickets.csv', mode='w', newline='') as csv_file:
	report_writer = csv.writer(csv_file, dialect='excel')
	for row in rows:
	    report_writer.writerow(row)