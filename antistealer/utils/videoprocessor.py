import io
import cv2


def extract_frames(
        video_path: str,
        max_fps: int = -1
) -> list[bytes]:
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
    frame_bytes = []

    while cap.isOpened():
        is_success, frame = cap.read()
        if is_success and counter % frame_interval == 0:
            _, buffer = cv2.imencode(".jpg", frame)
            frame_bytes.append(io.BytesIO(buffer).getvalue())
        counter += 1

    cap.release()

    return frame_bytes
