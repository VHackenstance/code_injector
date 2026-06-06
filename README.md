<h3>CODE INJECTOR</h3>
<p>
HTTP only.  
</p>
<h4>Process - Locally</h4>
<ol>
    <li>
        Set IP Table rules using set_iptables.py <br/>
    </li>
    <li>
        Afterwards, flush the iptables
    </li>
    <li>
        Check the tables have been flushed.<br/>
        <b>sudo iptables -L</b>
    </li>
</ol>
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
<p>I am testing against.<br/>
<b>http://testasp.vulnweb.com/</b><br/>
/var/www/htlm/index.html
</p>


