from flask import Flask, redirect, render_template, request
import platform, socket, re, uuid, json, psutil, logging, time

def getSystemInfo():
    """Get information about the current system

    Returns:
        dict: A dictionnary of system information.
    """
    info={}
    info['platform']=platform.system()
    info['platform-release']=platform.release()
    info['platform-version']=platform.version()
    info['architecture']=platform.machine()
    info['hostname']=socket.gethostname()
    info['ip-address']=get_external_ip()
    info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
    info['processor']=platform.processor()
    info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    info['uptime']=str(int(time.time() - psutil.boot_time())) + " seconds"
    return info


def get_external_ip():
    """Get the IP address used for the default route

    Returns:
        str: IP address used for the default route
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    ext_ip_addr = s.getsockname()[0]
    s.close()
    return ext_ip_addr


app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/ui", code=301)

@app.route('/ui')
def ui():
    return render_template('ui.html')

@app.route('/api')
def sysinfo():
    info = getSystemInfo()
    info["remote_addr"] = request.remote_addr
    if request.headers.getlist("X-Forwarded-For"):
        info['X-Forwarded-For'] = request.headers.getlist("X-Forwarded-For")[0]
    return info