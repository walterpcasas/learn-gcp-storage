import os
from google.cloud import storage
import pandas as pd
from datetime import datetime
import config

# Set the environment variable with the path to the credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "wpc-credentials.json"

def main(request):

    time = datetime.now()

    # Create DataFrame Pandas
    df = pd.DataFrame({'A':[3,4],'B':[5,6]})
    
    # Connection to GCP Bucket
    bucket_name = config.BUCKET_NAME
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    # List objects from bucket
    filename = 'archivo' + str(time) + '.csv'
    filepath = os.path.join(config.BUCKET_PATH, filename)
    blob = bucket.blob(filepath)
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')
    return 'DONE!'

if __name__ == "__main__":
    print(main("request"))