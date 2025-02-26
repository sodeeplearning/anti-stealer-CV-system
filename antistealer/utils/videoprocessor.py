import io
import cv2
import base64
from PIL import Image

from ..config import default_max_fps


def extract_frames(
        video_path: str,
        max_fps: int = default_max_fps
) -> list[str]:
    """Get image frames from video.

    :param video_path: Path to a video.
    :param max_fps: Limit FPS of video
    :return: list of image frames' bytes.
    """
    if max_fps == -1:
        max_fps = 1e9

    cap = cv2.VideoCapture(video_path)

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = int(min(fps, max_fps))

    counter = 0
    frames = []

    while cap.isOpened():
        is_success, frame = cap.read()

        if not is_success:
            break

        if counter % frame_interval == 0:
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            frames.append(base64.b64encode(buffered.getvalue()).decode("utf-8"))
        counter += 1

    cap.release()

    return frames
