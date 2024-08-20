# Zendesk View Exporter

## Description
This script exports into CSV or Excel the list of issues part of a Zendesk view using the API:

## How to install

```
# Install required libraries
pip3 install requests openpyxl pandas

# replace the <...> with the actual values 
python3 zendesk-view-request.py <your_email>/token <password> <zendesk_view_id> <output_file_name>

```

## References 
[How to create a view in Zendesk](https://support.zendesk.com/hc/en-us/articles/4408888828570-Creating-views-to-build-customized-lists-of-tickets)