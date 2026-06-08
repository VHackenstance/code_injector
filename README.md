<h3>CODE INJECTOR</h3>
    <p>
    HTTP only.  
    </p>
<h3>Testing Online</h3>
    <h4>Before we progress let me state clearly, in the main script code_injector.py</h4>
    <p>We are testing HTTP online against either OWASP Juice Shop, and/or Vulnweb.
        <br/> 
            Both of these site have been designed and hosted as hackable sites.  Fully legal.
        <br/>
            <b>http://juice-shop.herokuapp.com/#/</b>
        <br />
            <b>http://testasp.vulnweb.com/</b>
            Let me state again, both these sites are designated af freely hackable sites.

<h3>Testing Locally</h3>
    <h4>I have written a separate script code_inj_https.py to deal with localhost testing...</h4>
        <p> Against OWASP Juice Shop 
            <br/>
                <b>http://127.0.0.1:42000/#/</b>
        </p>
    <h4>The following is a brief install guide to Juice Shop from the terminal in Kali Linux.</h4>
    <p>
        Because the amount of BS and misinformation about how to do this, when it is so 
        simple, is ridiculous.  eg, install Docker, install node, install npm, 
        <br/>download from github.  So, simply put, here his the painfree Linux Rox version:
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
        <li> And just listen to the Angels weep, with laughter.</li>
    </ol>
    




<h4>Modify the data in the RAW layer, more specifically, the HTML code.</h4>
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
        We want to remove Accept-Encoding from the HTTP Request load.
        <br />
        <b>Accept-Encoding: gzip, deflate\r\n </b>
        <li>
            Do this with regex: <b>"Accept-Encoding:.*?\\r\\n"</b>
        </li>
    </li>
</ol>
<h4>Created a separate script code_inj_https, to test against OWASP Juice Shop</h4>
<p>I am testing against.<br/>
<b>http://testasp.vulnweb.com/</b><br/>
/var/www/htlm/index.html
</p>
    <h4>OWASP Webgoat Tested locally does not generate HTTP requests or responses</h4>
    <p>Also the installation is difficult but this is moot because it does not work.</p>
<h4>Created a separate script code_inj_https, to test against OWASP Juice Shop</h4>
<p>Early testing good results, </p>
<ol>
<li>Navigate to: <b>https://github.com/WebGoat/WebGoat/releases</b></li>
<b>Download the <b>webgoat-[version_number].jar</b> file</li>
<li>Navigate to <b>/Downloads directory</b></li>
<li>Run: <b>$ java -jar webgoat-2025.3.jar</b></li>
<li></li>
</ol>


