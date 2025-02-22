import argparse

from antistealer import make_request


parser = argparse.ArgumentParser(description="Получение пути для видео")
parser.add_argument("--path", required=True, help="Укажите путь к видеофайлу")
args = parser.parse_args()

print(f"Была ли запечатлена кража на этом видео? {make_request(args.path)}")
