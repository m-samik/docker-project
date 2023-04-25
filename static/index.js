function myoutput() {
    var cname=document.getElementById("cname").value;
    var iname=document.getElementById("iname").value;
    var ping= new XMLHttpRequest();
    ping.open("GET", "http://192.168.1.11/cgi-bin/dockerstart.py?iname="+iname+"&cname="+cname, true);
    ping.send();
    ping.onload = function() { 
        var output = ping.responseText;
        console.log(output);
        document.getElementById("ch2").innerHTML = output;
    } 
}
function myoutput2() {
    var cmd=document.getElementById("cmd").value;
    var ping= new XMLHttpRequest();
    ping.open("GET", "http://192.168.1.11/cgi-bin/dockerstatus.py?cmd="+cmd, true);
    ping.send();
    ping.onload = function() { 
        var output = ping.responseText;
        console.log(output);
        document.getElementById("ch2").innerHTML = output;
    } 
}
function myoutput3() {
    var dstop=document.getElementById("dstop").value;
    var ping= new XMLHttpRequest();
    ping.open("GET", "http://192.168.1.11/cgi-bin/dockerstop.py?dstop="+dstop, true);
    ping.send();
    ping.onload = function() { 
        var output = ping.responseText;
        console.log(output);
        document.getElementById("ch2").innerHTML = output;
    } 
}
    i=0;
    document.onload(anim());
        function anim(){
			var r1 = document.getElementById("anim");
			r1.style.left=i + "px";
			i++;
            if (i==1550){
                //r1.style.backgroundImage="url('../static/images/laod.gif')";
                i=0;
            }
			setTimeout(anim , 10);
         }
        
        function dark(){
            
            bgelement = document.getElementById("bg");
            bgelement.style.backgroundColor="#222222";
            bgelement.style.color="white";
        }  
        function white(){
            bgelement = document.getElementById("bg");
            bgelement.style.backgroundColor="wheat";
            bgelement.style.color="black";
        } 