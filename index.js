var term;
const btnRun = document.getElementById("button");
const textArea = document.getElementById("terminal");

btnRun.addEventListener("click", function () {
    var term = new Terminal({
        cols: 80,
        rows: 24
    });
    term.open(document.getElementById('terminal'));
    term.writeln('Running startup command: python3 run.py');
    term.writeln('');

    var ws = new WebSocket(location.protocol.replace('http', 'ws') + '//' + location.hostname + ((location.port) ? (':' + location.port) : '') + '/');

    ws.onopen = function () {
        new attach.attach(term, ws);
    };

    ws.onerror = function (e) {
        console.log(e);
    };
});
```

---

### **📄 FILE 9: Update `requirements.txt`**

Add Flask to your requirements. Your `requirements.txt` should include:
```
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
numpy==1.24.3
gspread==5.10.0
google-auth==2.22.0
google-auth-oauthlib==1.0.0
google-auth-httplib2==0.1.0
Flask==2.3.2