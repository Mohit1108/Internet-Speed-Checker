import speedtest#pip install speedtest-cli
test = speedtest.Speedtest()
down = test.download()/2000
upload = test.upload()/2000
print(f"Download Speed: {down}")
print(f"Upload Speed : {upload}")
print("Speed In MBPS")


