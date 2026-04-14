<h3>CODE INJECTOR</h3>
<p>
This script does not work with HTTPS sites, which is pretty much every site now.  Even the few 
sites left that are not HTTPS, such as bing.com, it will not work due to HSTS (HTTP Strict Transport Security)
and Certificate Pinning.  I am building it as a scaffold, as with every project here, for when I implement onPath for HTTPS.
</p>
<h4>Process - Locally</h4>
<ol>
<li>
    Run IP Table rules <br/>
    <b>sudo iptables -I INPUT -j NFQUEUE --queue-num 0 --queue-bypass
        <br/>
        <br/>
    sudo iptables -I OUTPUT -j NFQUEUE --queue-num 0 --queue-bypass</b>
</li>
<li>
    Afterwards, clear the iptables
    <br>
    <b>sudo iptables --flush</b>
</li>
<li>
    Check the tables have been flushed.<br/>
    <b>sudo iptables -L</b><br/>
    The chains, or table, of values should be empty.
</li>
<li></li>
</ol>
<p></p>
<p></p>
<p></p>
<h4>/h4>
<p></p>
<h3>
</h3>
<h4></h4>

