def handler(event, context):
    return "Polo" if event['name'] == "Marco" else "NA"
