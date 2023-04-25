function dark(){
    txt = document.getElementsByTagName("label");
    for (i=0 ; i<txt.length; i++){
        txt[i].style.color = "white";
    }
    
    bgelement = document.getElementById("bg");
    bgelement.style.backgroundColor="#222222";
}  
function white(){
    txt = document.getElementsByTagName("label");
    for (i=0 ; i<txt.length; i++){
        txt[i].style.color = "black";
    }
    bgelement = document.getElementById("bg");
    bgelement.style.backgroundColor="wheat";
} 
function mydata() {
    var load = document.getElementById("load");
    window.setTimeout("document.getElementById('load').style.display='inline-block';", 100)
    window.setTimeout("document.getElementById('load').style.display='none';", 2500)
    var xhr = new XMLHttpRequest();
    // kepps on checking the output parallay
    var phone = document.getElementById("ph").value 
    xhr.open("GET", "http://127.0.0.1:5002/get_phone?phone="+phone , true)
    xhr.send();
    xhr.onload = function() { 
        var output = xhr.responseText;
        document.getElementById("d1").innerHTML = output;
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
