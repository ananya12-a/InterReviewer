from hume import HumeBatchClient
from hume.models.config import FaceConfig, ProsodyConfig, LanguageConfig

client = HumeBatchClient("130VUokCECUiWliyfsZDdrNOpImkLWv60RrPSVPAl1RycIWk")
# urls = ["https://storage.googleapis.com/hume-test-data/video/armisen-clip.mp4"]
filepaths = ["user_data/video1318490298.mp4"]
configs = [FaceConfig(identify_faces=True, save_faces=True), ProsodyConfig(identify_speakers=True, granularity="conversational_turn"), LanguageConfig(sentiment={},granularity="sentence")]
# job = client.submit_job(urls, configs)
job = client.submit_job(None, configs, files=filepaths)

print(job)
print("Running...")

details = job.await_complete()
job.download_predictions("job_output/predictions.json")
print("Predictions downloaded to predictions.json")

job.download_artifacts("job_output/artifacts.zip")
print("Artifacts downloaded to artifacts.zip")