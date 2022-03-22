function start() {
    $(function () {
        let inhaleTimings = [3000, 4000, 3000, 5000]
        let holdTimings = [1000, 2000, 2000, 3000]
        let exhaleTimings = [2000, 3000, 4000, 2000]
        let score = 0;
        function inhale(x) {
            $('.breatheRed').animate({
                height: 1,
            }, x);
        };

        function hold(x) {
            $('.breatheRed').animate({
                height: 1,
            }, x);
        };

        function exhale(x) {
            $('.breatheRed').animate({
                height: 500,
            }, x)
        };

        for (let i = 0; i < 4; i++) {

            inhaleTime = inhaleTimings[i];
            holdTime = holdTimings[i];
            exhaleTime = exhaleTimings[i];

            setTimeout(inhale(inhaleTime));
            setTimeout(hold(holdTime));
            setTimeout(exhale(exhaleTime));
        }

    });

}
function stop() {
    return;
}
