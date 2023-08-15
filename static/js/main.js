
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
  }

var texts = new Array();
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");
texts.push(getRandomInt(10))
texts.push(" ");


var point = 0;

function changeText(){
  $('p').html(texts[point]);
  if(point < ( texts.length - 1 ) ){
    point++;
  }else{
    point = 0;
  }
  
}
 
setInterval(changeText, 500); 
changeText();



