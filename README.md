<h3>CODE INJECTOR</h3>
    <p>
    HTTP only.  
    </p>
<p>
    This script works fully with:  <b>http://testasp.vulnweb.com/</b>
    <br />
    Modifying Content-Length has made it work better, but still not ideal
    <h4>
        It does work in other sites if you insert the code in an earlier tag.
    </h4>
    <b>http://www.pentest-standard.org/</b>
    <br/>
    Converting load to a string earlier made no difference.
    <br />
    UPDATE:  Works now against the functioning:  <b>http://juice-shop.herokuapp.com/#/</b>
    <br />
    But breaks the site stopping page load, the raw loads.  
    <br />
    Works with </head> tag but also breaks page load.

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


