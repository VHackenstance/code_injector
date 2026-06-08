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
   
    </li>
</ol>
<p>I am testing against.<br/>
<b>http://testasp.vulnweb.com/</b><br/>
/var/www/htlm/index.html
</p>
<h4>OWASP Webgoat Install, for (Kali?) Linux only.</h4>
<p>I am yet to test this <b>Locally</b> against packet_sniffer and replace_downloads
    <br/>
    But I am hoping it will do a better job than OWASP Juice shop - locally.
    <br/>
    Oh, and no Docker, sorry not sorry.  Really do not like it, almost exclusively because of the 
    way it just vomits all over ip_tables.  If it is doing that to ip_tables how is
    is messing up other parts of your code?
</p>
<ol>
<li>Navigate to: <b>https://github.com/WebGoat/WebGoat/releases</b></li>
<b>Download the <b>webgoat-[version_number].jar</b> file</li>
<li>Navigate to <b>/Downloads directory</b></li>
<li>Run: <b>$ java -jar webgoat-2025.3.jar</b></li>
<li></li>
</ol>


