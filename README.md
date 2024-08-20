# Zendesk View Exporter

This script exports into CSV or Excel the list of issues part of a Zendesk view using the API:

```
# Install required libraries
pip3 install requests openpyxl pandas

# replace the <...> with the actual values 
python3 zendesk-view-request.py <your_email>/token <password> <zendesk_view_id> <output_file_name>

```