function generate() {
    var hexValues = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e"];
    var randomColor1 = "hsl(" + 360 * Math.random() + ',' + (75 + 20 * Math.random()) + '%,' + (45 + 5 * Math.random()) + '%, 1)',
    randomColor2 = "hsl(" + 360 * Math.random() + ',' + (75 + 20 * Math.random()) + '%,' + (45 + 5 * Math.random()) + '%, 1)'

    var angle = Math.round( Math.random() * 360 );
    
    var gradient = "linear-gradient(" + angle + "deg" + ", " + randomColor1 + ", " + randomColor2 + ")";
    
    return gradient
}

$(document).ready(function() {
    $('.prodContainer').each(function () {
        var output = generate();
        console.log(output)
        $(this).css("background", output);
    });
});
/* function generate() {
    var hexValues = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e"];
    
    function populate(a) {
      o = ''
      for ( var i = 0; i < 6; i++ ) {
        var x = Math.round( Math.random() * 14 );
        var y = hexValues[x];
        console.log(y)
        o += y;
      }
      return a + o;
    }
    
    var newColor1 = populate('#');
    var newColor2 = populate('#');
    var angle = Math.round( Math.random() * 360 );
    
    var gradient = "linear-gradient(" + angle + "deg, " + newColor1 + ", " + newColor2 + ")";
    
    return gradient
}

$(document).ready(function() {
    $('.prodContainer').each(function () {
        var output = generate();
        console.log(output)
        $(this).css("background", output);
    });
}); */