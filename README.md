<h3>CODE INJECTOR</h3>
    <p>
    HTTP only.  
    </p>
<p>
    This script works fine but only with the following site 
    <br />
    <b>http://testasp.vulnweb.com/</b>
    <br />
    For larger sites it breaks the payload download, and my testing has yet to 
    discover why this is the case.  At this point I am going to progress my learning
    and hope I stumble upon a solution, or revisit the issue in the future.
    <h4>It does work in other sites but only if you insert the code in an earlier tag.
    </h4>
    A specific example of this is 
    <br/><b>http://www.pentest-standard.org/</b>
    <br/>
    I also tested converting load to a string earlier but this made no difference.
    <br />
    UPDATE:  Also tested now against the functioning.  
    <br />
    <b>http://juice-shop.herokuapp.com/#/</b>
    <br />
    And it also breaks the site by somehow stopping the page loading, the raw loads
    being delivered, midway.  Works with </head> tag but also breaks page load.

<h3>Testing Online</h3>
    <h4>Before we progress let me state clearly, in the main script code_injector.py</h4>
    <p>We are testing HTTP online against OWASP Juice Shop, and/or Vulnweb.
        <br/> 
            Both of these site have been designed and hosted as hackable sites.  Fully legal.
        <br/>
            <b>http://juice-shop.herokuapp.com/#/</b>
        <br />
            <b>http://testasp.vulnweb.com/</b>
        <br/>
            Let me state again, both these sites are designated af freely hackable sites.

<h3>Testing Locally</h3>
    <h4>I have written a separate script code_inj_https.py to deal with localhost testing...</h4>
        <p> Against OWASP Juice Shop 
            <br/>
                <b>http://127.0.0.1:42000/#/</b>
        </p>
    <h4>The following is a brief install guide to Juice Shop from the terminal in Kali Linux.</h4>
    <p>
        Because there is misinformation about how to do this, when it is 
        simple.  
        <br/>
        eg, install Docker, install node, install npm, eg... 
        download from github.  So, simply put, here his the painfree <b>Linux Rox</b> version:
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


