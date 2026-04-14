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

<h4>Setting the iptables can now be run by a script</h4>
<h5>sudo python ./Utilities/set_iptables.py -s [True/False/Omit] -n [number/omit] -f [True/False/Omit]</h5>
<ul>
<li>-s, --set, is setiptables, do you want to set iptables True or False
    <br/>
    If you do not want to set just leave blank.
</li>
<li>
-n, --number, is number, specify the table number, default 0
    <br/>
    If you do not want to set just leave blank.
</li>
<li>
-f, --flush, is flush, do you want to flush(unset/clear) iptables True or False
    <br/>
    If you do not want to flush just leave blank.
    <br/>
    Or, you can place of a value of False.
</li>
</ul>





<p></p>
<p></p>
<p></p>
<h4>/h4>
<p></p>
<h3>
</h3>
<h4></h4>

