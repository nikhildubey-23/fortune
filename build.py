import shutil, os
from app import app

PUBLISH = "publish"
STATIC_SRC = os.path.join(app.root_path, "static")
STATIC_DST = os.path.join(PUBLISH, "static")

if os.path.exists(PUBLISH):
    shutil.rmtree(PUBLISH)

os.makedirs(STATIC_DST, exist_ok=True)

client = app.test_client()
resp = client.get("/")
with open(os.path.join(PUBLISH, "index.html"), "w") as f:
    f.write(resp.data.decode())

for item in os.listdir(STATIC_SRC):
    s = os.path.join(STATIC_SRC, item)
    d = os.path.join(STATIC_DST, item)
    if os.path.isdir(s):
        shutil.copytree(s, d, dirs_exist_ok=True)
    else:
        shutil.copy2(s, d)

print("Build complete → publish/")
