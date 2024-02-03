from hume import HumeBatchClient
from hume.models.config import FaceConfig
from hume.models.config import ProsodyConfig

client = HumeBatchClient("130VUokCECUiWliyfsZDdrNOpImkLWv60RrPSVPAl1RycIWk")
# urls = ["https://storage.googleapis.com/hume-test-data/video/armisen-clip.mp4"]
filepaths = ["\user_data\video1124829211.mp4"]
configs = [FaceConfig(identify_faces=True), ProsodyConfig()]
# job = client.submit_job(urls, configs)
job = client.submit_job(None, [configs],file=filepaths)

print(job)
print("Running...")

details = job.await_complete()
job.download_predictions("predictions.json")
print("Predictions downloaded to predictions.json")

job.download_artifacts("artifacts.zip")
print("Artifacts downloaded to artifacts.zip")