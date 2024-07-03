# GCP Storage

Codigo para guardar archivos csv generados por Pandas (Python) en los buckets de GCP Storage.

Para poder generar nuestras credenciales y conectarnos a nuestro bucket debemos seguir los siguientes pasos:

1. Crear una Service Account que se logge desde el VSCode.
2. Darle permisos de `Storage Admin` en IAM a nuestra Service Account.
3. Luego en la lista de Service Accounts, ubica la tuya y selecciona del menu _Manage Keys_.
4. Crea una nueva key, seleccionando por defecto JSON y se descargara el archivo que debes guardar en una ruta segura y no compartirla.