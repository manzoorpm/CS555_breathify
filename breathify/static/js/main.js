function start() {
    var val = document.getElementById('level').getAttribute('data-value');
    userID = document.getElementById('userID').innerHTML;
    console.log(userID);

    let inhaleTimings;
    let holdTimings;
    let exhaleTimings;
    let allTimings;
    let totalTimings;
    let flag = 0;
    let levelName;
    let finalScore;

    if (val == 1) { //level One Timings
        inhaleTimings = [3000, 4000, 3000, 5000];
        holdTimings = [1000, 2000, 2000, 3000];
        exhaleTimings = [2000, 3000, 4000, 2000];
        allTimings = [3000, 1000, 2000, 4000, 2000, 3000, 3000, 2000, 4000, 5000, 3000, 2000];
        totalTimings = [5000, 9000, 9000, 10000];
        lenAll = allTimings.length;
        lenTot = totalTimings.length;
    }

    let score = 0;
    var elem = document.getElementById("score");
    var steps;

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
        totalTime = totalTimings[i];

        inhale(inhaleTime);
        hold(holdTime);
        exhale(exhaleTime);
    }

    var j = 0;

    function myLoop() {
        score = score + 100;
        setTimeout(function () {
            elem.innerHTML = score;
            j++;
            if (j < lenTot) {
                myLoop();
            }
            else {
                displayScore();
            }
        }, totalTimings[j])
    }

    myLoop();
    k = 2;
    l = 1;
    m = 0;

    function stepsLoop() {
        setTimeout(function () {
            document.getElementById(l).classList.remove("task-selected");
            document.getElementById(k).classList.add("task-selected");
            m++;
            k++;
            l++;
            if (m < lenAll) {
                stepsLoop();
            }
        }, allTimings[m])
    }

    stepsLoop();

    function displayScore() {
        var scoreBox = document.getElementById("score-box");
        scoreBox.style.display = "flex"
    }

}

function stop() {
    return;
}

function saveScore() {
    levelName = document.getElementById('levelName').innerHTML;
    finalScore = document.getElementById('score').innerHTML;
    document.getElementById('user').value = userID;
    document.getElementById('levelNameForm').value = levelName;
    document.getElementById('latestScoreForm').value = finalScore;
    var form = document.getElementById("postScore");
    form.submit();
}
