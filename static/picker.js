function generate() {
    var hexValues = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e"];

    colors = ["#628DA8", "#00498E", "#A4DBDE","#96AB50", "#5B7345", "#EFCD61", "#CFB094", "#E5E9E8", "#EBD3C7", "#E36243", "#D03378"]
    // colors = ["#AFB85E", "#E2F0B9", "#D2DEE9",/*  "#A5AD9F", */ "#93B881", "#D0B9A8", "#D3D1C5", "#E5E9E8", "#637F62", "#B8B5A2"]

    var randomColor1 = shadeColor(colors[Math.floor(Math.random() * colors.length)],60),
    randomColor2 = shadeColor(colors[Math.floor(Math.random() * colors.length)],60),
    randomColor3 = shadeColor(colors[Math.floor(Math.random() * colors.length)], 60)

    var angle = Math.round( Math.random() * 360 );
    
    var gradient = "linear-gradient(" + angle + "deg" + ", " + randomColor1 + ", " + randomColor2 + "," + randomColor3 + ")";
    
    
    return gradient
}

function shadeColor(color, percent) {

    var R = parseInt(color.substring(1,3),16);
    var G = parseInt(color.substring(3,5),16);
    var B = parseInt(color.substring(5,7),16);

    R = parseInt(R * (100 + percent) / 100);
    G = parseInt(G * (100 + percent) / 100);
    B = parseInt(B * (100 + percent) / 100);

    R = (R<255)?R:255;  
    G = (G<255)?G:255;  
    B = (B<255)?B:255;  

    var RR = ((R.toString(16).length==1)?"0"+R.toString(16):R.toString(16));
    var GG = ((G.toString(16).length==1)?"0"+G.toString(16):G.toString(16));
    var BB = ((B.toString(16).length==1)?"0"+B.toString(16):B.toString(16));

    return "#"+RR+GG+BB;
}