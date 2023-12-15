# ws-data-vault-databricks-na-pratica
Construindo um Data Vault no Data Lakehouse com Databricks e Delta Lake na Prática

### .env
```shell
export PAYMENTS_FILES='src/objects/payments.csv'
export RIDES_FILES='src/objects/rides.csv'
export VEHICLE_FILES='src/objects/vehicle.csv'

export BLOB_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=??;AccountKey=??==;EndpointSuffix=core.windows.net"
export LANDING_CONTAINER_NAME='owshq-stg-files'
```

### star schema
https://dbdiagram.io/d/workshop-dv-relational-dm-6577399256d8064ca0cf08c9

### data vault
https://dbdiagram.io/d/workshop-data-vault-model-657a198c56d8064ca0fb4ab5
