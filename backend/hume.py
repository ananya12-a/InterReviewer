from hume import HumeBatchClient
from hume.models.config import FaceConfig

client = HumeBatchClient("130VUokCECUiWliyfsZDdrNOpImkLWv60RrPSVPAl1RycIWk")
urls = ["https://iep.utm.edu/wp-content/media/hume-bust.jpg"]
config = FaceConfig()
job = client.submit_job(urls, [config])