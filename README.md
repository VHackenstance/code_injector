<h3>CODE INJECTOR</h3>
<p>
This script does not work with HTTPS sites, which is pretty much every site now.  Even the few 
sites left that are not HTTPS, such as bing.com, it will not work due to HSTS (HTTP Strict Transport Security)
and Certificate Pinning.  I am building it as a scaffold, as with every project here, for when I implement onPath for HTTPS.
</p>
<h4>Process - Locally</h4>
<h4>1. Set the iptables rules</h4>
<ol>
    <li>
        Set IP Table rules <br/>
        <b>sudo iptables -I INPUT -j NFQUEUE --queue-num 0 --queue-bypass
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
</ol>

<h4>Setting the iptables can now be run by a script</h4>
<h4>sudo python ./Utilities/set_iptables.py -s [True/False/Omit] -n [number/omit] -f [True/False/Omit]</h4>
<ul>
    <li><b>-s</b>, --set, is setiptables, do you want to set iptables True or False
        <br/>
            If you do not want to set False or just leave blank.
    </li>
    <li>
    <b>-n</b>, --number, is number, specify the table number, default 0
        <br/>
            If you do not want to set just leave blank.
    </li>
    <li>
    <b>-f</b>, --flush, is flush, do you want to flush(unset/clear) iptables True or False
        <br/>
            If you do not want to flush just leave blank.
        <br/>
            Or, you can place of a value of False.
    </li>
</ul>
<h4>This code as it stands will not work with HTTPS</h4>
<p>I am testing against the only http website I currently know.<br/>
<b>http://testasp.vulnweb.com/Default.asp?</b><br/>
</p>
<h4>index.html file location</h4>
<p>
/var/www/htlm/index.html
</p>


