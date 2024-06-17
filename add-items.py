import re
import requests
import json

# What this does:
# Run like this: python3 add-items.py
# It will ask you for an MMS ID, then offer you all the holdings attached to that bib record.
# Then it will take the holdings record you chose and add items to that holdings record.

#print("Here is an mms id of a test record: 99187970942906381")

mmsid = input("Please enter the MMS ID number of the bib record to which you would like to add items: ")
mmsid = mmsid.strip()

if re.match('\d{7}', mmsid):
        pass
else:
        print('Not a propertly formatted mms id.')
        exit()

url = f"https://api-na.hosted.exlibrisgroup.com/almaws/v1/bibs/{mmsid}/holdings"

api_key = '[api_key]'

# Create a request
headers = {'Authorization': f'apikey {api_key}', 'content_type': 'application/json', 'Accept': 'application/json'}

# Send the request
r = requests.get(url, headers=headers)

# Handle the response
try:
        # print(r.status_code)
        # print(r.text)
        title = r.json()["bib_data"]["title"]
        # The full response
        # pretty_json = json.dumps(r.json(), indent=4)
        # print(pretty_json)
        # print("Title: ", r.json()["bib_data"]["title"])

except:
        print("There was a problem. Check that this record exists and has at least one holdings.")
        quit()

print(f"The holdings for {title} are:")
reply = r.json()
holding = reply["holding"]
list_of_holdings = []
for hold in holding:
        print("Library code:", hold['library']['value'], "Location code:", hold['location']['value'], "holding id:", hold['holding_id'])
        list_of_holdings.append(hold['holding_id'])

holding_for_items = input("Please enter the holding id number of the holding record to which you would like to add items: ")
holding_for_items = holding_for_items.strip()

if holding_for_items in list_of_holdings:
        pass
else:
        print("That's not a valid holding id.")
        quit()

while True:
        numb = input('Enter the number of items to create: ')
        if numb == 0:
                print("Not creating items, quitting.")
                quit()
        else:
                try:
                        numb = int(numb)
                        break
                except:
                        print("That's not a number.")
                        continue

print("MMS ID:", mmsid, "holding id:", holding_for_items, "Items to create:", numb)

create_item_url = f"https://api-na.hosted.exlibrisgroup.com/almaws/v1/bibs/{mmsid}/holdings/{holding_for_items}/items?generate_description=false"
#print(create_item_url)

request_body = '''
<item link="">
  <holding_data link="">
    <holding_id></holding_id>
    <copy_id></copy_id>
    <in_temp_location></in_temp_location>
    <temp_library></temp_library>
    <temp_location></temp_location>
    <temp_call_number_type></temp_call_number_type>
    <temp_call_number></temp_call_number>
    <temp_call_number_source></temp_call_number_source>
    <temp_policy></temp_policy>
    <due_back_date></due_back_date>
  </holding_data>
  <item_data>
    <barcode></barcode>
    <physical_material_type></physical_material_type>
    <policy></policy>
    <provenance></provenance>
    <po_line></po_line>
    <issue_date></issue_date>
    <is_magnetic></is_magnetic>
    <arrival_date></arrival_date>
    <expected_arrival_date></expected_arrival_date>
    <year_of_issue></year_of_issue>
    <enumeration_a></enumeration_a>
    <enumeration_b></enumeration_b>
    <enumeration_c></enumeration_c>
    <enumeration_d></enumeration_d>
    <enumeration_e></enumeration_e>
    <enumeration_f></enumeration_f>
    <enumeration_g></enumeration_g>
    <enumeration_h></enumeration_h>
    <chronology_i></chronology_i>
    <chronology_j></chronology_j>
    <chronology_k></chronology_k>
    <chronology_l></chronology_l>
    <chronology_m></chronology_m>
    <break_indicator></break_indicator>
    <pattern_type></pattern_type>
    <linking_number></linking_number>
    <description></description>
    <replacement_cost></replacement_cost>
    <receiving_operator></receiving_operator>
    <inventory_number></inventory_number>
    <inventory_date></inventory_date>
    <inventory_price></inventory_price>
    <receive_number></receive_number>
    <weeding_number></weeding_number>
    <weeding_date></weeding_date>
    <alternative_call_number></alternative_call_number>
    <alternative_call_number_type></alternative_call_number_type>
    <alt_number_source></alt_number_source>
    <storage_location_id></storage_location_id>
    <pages></pages>
    <pieces></pieces>
    <public_note></public_note>
    <fulfillment_note></fulfillment_note>
    <internal_note_1></internal_note_1>
    <internal_note_2></internal_note_2>
    <internal_note_3></internal_note_3>
    <statistics_note_1></statistics_note_1>
    <statistics_note_2></statistics_note_2>
    <statistics_note_3></statistics_note_3>
    <physical_condition></physical_condition>
    <committed_to_retain></committed_to_retain>
    <retention_reason></retention_reason>
    <retention_note></retention_note>
  </item_data>
</item>
'''

# Create a request
headers = {'Authorization': f'apikey {api_key}', 'Content-Type': 'application/xml', 'Accept': 'application/json'}

for i in range(numb):
            # Send the request
            c = requests.post(create_item_url, headers=headers, data=request_body)

            #print(c.text)
            #pretty_json = json.dumps(c.json(), indent=4)
            #print(pretty_json)
            response = c.json()
            barcode = response["item_data"]["barcode"]
            print("Just created item with barcode:", barcode)

print("Done.")
