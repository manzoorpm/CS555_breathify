function start(){
$(function(){
    let inhaleTimings =[3000,4000,3000,5000]
    let exhaleTimings =[2000,3000,4000,2000]

    function inhale(x){
      $('.breatheRed').animate({
        height: 800,
      }, x);
    };
    function hold(x){
        $('.breatheRed').animate({
            height: 1,
        }, x);
      };
    function exhale(y){
      $('.breatheRed').animate({
        height: 1,
      }, y)
    }
   for (let i = 0; i < 4; i++) {

       inhaleTime= inhaleTimings[i];
       exhaleTime= exhaleTimings[i];

       setInterval(inhale(inhaleTime));
       setInterval(hold(inhaleTime));
       setInterval(exhale(exhaleTime));
}
  
  });

}