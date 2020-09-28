import multiprocessing
import subprocess

# echo | set /p="pw" > app.pw

def runWinCmd(secs, cap):
    subprocess.run(["timeout", secs], capture_output=cap)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=runWinCmd, args=["5", False])
    p2 = multiprocessing.Process(target=runWinCmd, args=["10", False])
    p1.start()
    p2.start()
    p1.join()
    #p2.join()
    p2.kill()
