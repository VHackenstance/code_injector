<h3>CODE INJECTOR</h3>
<p>
HTTP only.  
</p>
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
<p>I am testing against.<br/>
<b>http://testasp.vulnweb.com/</b><br/>
/var/www/htlm/index.html
</p>
    <h4>OWASP Webgoat Install.  Tested locally does not generate HTTP requests or responses</h4>
<ol>
<li>Navigate to: <b>https://github.com/WebGoat/WebGoat/releases</b></li>
<b>Download the <b>webgoat-[version_number].jar</b> file</li>
<li>Navigate to <b>/Downloads directory</b></li>
<li>Run: <b>$ java -jar webgoat-2025.3.jar</b></li>
<li></li>
</ol>


