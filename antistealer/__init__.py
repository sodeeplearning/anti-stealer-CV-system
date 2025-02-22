from .model import model_request
from .utils.videoprocessor import extract_frames


def make_request(video_path: "str") -> str:
    frame_bytes = extract_frames(video_path, max_fps=5)
    response = model_request(images=frame_bytes)
    return response
