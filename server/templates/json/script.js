var gradi = 19;
var max = 34;
var min = 2;

function updateGr(){
  $(".heat").text("" + gradi);
  $(".ext").text("" + gradi);
  $(".number").css("transform", "translate(-50%, -50%) rotate("+ (-180 + gradi * 10)+"deg)");
  $(".shadow").css("transform", "translate(-50%, -50%) rotate("+ (-180 + gradi * 10)+"deg)");
  $(".fill").css("animation", "none");
  $(".shadow").css("animation", "none");
}


$(".minus").mousedown(function(){ 
  if(gradi > min){
    gradi--;
    updateGr();
    if(gradi >= 18){
      $(".fill1").css("transform", "rotate("+ (gradi - 18) * 10 +"deg)").css("transition-delay", "0s");
    }else if(gradi == 17){
      $(".fill2").css("transform", "rotate("+ gradi * 10 +"deg)").css("transition-delay", "0.5s");  
    }else{
      $(".fill2").css("transform", "rotate("+ gradi * 10 +"deg)").css("transition-delay", "0s");
    }
  }
});

$(".plus").mousedown(function(){
  if(gradi < max){
    gradi++;
    updateGr();
    if(gradi > 19){
      $(".fill1").css("transform", "rotate("+ (gradi - 18) * 10 +"deg)").css("transition-delay", "0s");
    }else if(gradi == 19){
      $(".fill1").css("transform", "rotate("+ (gradi - 18) * 10 +"deg)").css("transition-delay", "1s"); 
    }else{
      $(".fill2").css("transform", "rotate("+ gradi * 10 +"deg)").css("transition-delay", "0s");
    }
  }  
});