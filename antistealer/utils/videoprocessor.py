import io
import cv2
import base64


def extract_frames(
        video_path: str,
        max_fps: int = -1
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
    frame_base64 = []

    while cap.isOpened():
        is_success, frame = cap.read()

        if not is_success:
            break

        if counter % frame_interval == 0:
            _, buffer = cv2.imencode(".jpg", frame)
            frame_bytes = io.BytesIO(buffer).getvalue()
            frame_base64.append(base64.b64encode(frame_bytes).decode("utf-8"))
        counter += 1

    cap.release()

    return frame_base64
