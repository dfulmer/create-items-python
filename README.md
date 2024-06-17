# create-items-python

## Set up

Clone the repo

```
git clone [copy from above]
cd [directory from above]
```

Add an Alma API key to this line, in between the single quotes:

```
api_key = '[api_key]'
```

If necessary, install the requests library:

```
python -m pip install requests
```

## Run the program

```
python3 add-items.py
```

You will be asked for an MMS ID. After entering a valid MMS ID, you will be asked to choose a holding ID attached to that MMS ID. Then it will take the holdings record you chose and add items to that holdings record. It reports back the barcodes of the new items.